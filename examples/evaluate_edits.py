"""Selected scoring functions from Scribevo. This does not correct text or call AI."""

from __future__ import annotations
import difflib


def tokens(text: str) -> list[str]:
    return text.split()


def edit_set(source: str, target: str) -> set[tuple]:
    """
    The set of token-level edits that turn `source` into `target`.

    Represented as (tag, i1, i2, replacement) so two systems proposing the same
    change at the same position produce identical tuples and can be compared.
    """
    a, b = tokens(source), tokens(target)
    matcher = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    return {
        (tag, i1, i2, " ".join(b[j1:j2]))
        for tag, i1, i2, j1, j2 in matcher.get_opcodes()
        if tag != "equal"
    }


def normalise(text: str) -> str:
    """Comparison form: case- and whitespace-insensitive."""
    return " ".join(text.lower().split())


def _touched_source_indices(source: str, other: str) -> set[int]:
    """Which source token positions does `other` alter?"""
    a, b = tokens(source), tokens(other)
    touched: set[int] = set()
    for tag, i1, i2, _j1, _j2 in difflib.SequenceMatcher(
        a=a, b=b, autojunk=False
    ).get_opcodes():
        if tag != "equal":
            touched.update(range(i1, max(i2, i1 + 1)))
    return touched


def harmful_token_count(source: str, reference: str, output: str) -> int:
    """
    Count tokens the system changed that the reference deliberately left alone.

    This is stricter and more meaningful than "the predicted edit span differs
    from the gold edit span". Span comparison punishes a system for making a
    genuinely correct change simply because the reference merged it into a
    wider edit — e.g. correcting `i` to `I` in "i go yesterday" is right, even
    though the gold edit covers "i go" as one span. Only a change to a token
    the reference preserved is real harm.
    """
    gold_touched = _touched_source_indices(source, reference)
    pred_touched = _touched_source_indices(source, output)
    return len(pred_touched - gold_touched)


def score_edits(source: str, reference: str, output: str) -> dict:
    """Public wrapper for inspecting edit decisions on a supplied fixture."""
    gold, predicted = edit_set(source, reference), edit_set(source, output)
    tp, fp, fn = len(gold & predicted), len(predicted - gold), len(gold - predicted)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    denom = 0.25 * precision + recall
    return {
        "true_positive": tp,
        "false_positive": fp,
        "false_negative": fn,
        "precision": precision,
        "recall": recall,
        "f0_5": 1.25 * precision * recall / denom if denom else 0.0,
        "harmful_tokens": harmful_token_count(source, reference, output),
    }
