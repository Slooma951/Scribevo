# Scribevo: project evidence

Checked 4 October 2026. This evidence package has **11 passing tests** for the selected public examples. Full-product tests were not rerun for this publication.

## Output

A self-authored spelling fixture produces a JSON edit report. A separate NumPy summary counts invented outcome labels. The output is saved so a reviewer can compare a rerun with the documented fixture.

[Recorded JSON output](demo-output.json) · [Runnable example](../examples/demo.py)

## Methodology

Compare source, reference and output at token-edit level. Count true, false and missed edits, then calculate precision, recall and F0.5, which gives precision more weight. Separately count source tokens changed outside the reference’s edited positions. The NumPy companion uses broadcasting and boolean masks to aggregate invented outcome labels.

[Read the selected code](../examples/evaluate_edits.py) · [NumPy analysis](../examples/analyse_outcomes.py)

## Testing results

**11 passed, none failed**, on 4 October 2026. Runtime: Python 3.13.15.

Exact and missed corrections, an extra edit lowering precision and F0.5, unnecessary edits, reference-permitted edits, empty input, insertion, repeated-token alignment, NumPy counts, empty datasets and unknown labels.

[Test cases](../tests/test_evaluation.py) · [Machine-readable verification](verification.json)

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python examples/demo.py
```

The saved output contains synthetic data. Test counts are checks of this package, not user studies, product adoption or a performance benchmark. Timings from the test runner are not presented as product latency.

## Provenance and changes

Scoring primitives selected from `ml/evaluation/evaluate.py`, private revision `040ab8a`: tokenisation, edit extraction, comparison normalisation and harmful-token counting. `score_edits` is a new public wrapper. `analyse_outcomes.py` is a new portfolio companion exercise using NumPy, not part of the shipped extension or the original research model.

## Limits

These tests verify the public scoring code, not Scribevo’s model accuracy. Token alignment is lexical; it does not judge meaning or recognise every valid alternative phrasing. F0.5 is defined as zero when no edits are counted. Harmful-token counting is a proxy for unnecessary edits, not a human safety judgement. No model, correction rules, training dataset or provider call is included.

## AI-assisted workflow

Claude and ChatGPT have been used during later project development. This public package was selected, adapted, documented and tested with Codex. The NumPy companion, synthetic fixtures and public test cases were added for this portfolio. They are separated from the original academic work and full-product release checks. No claim of entirely unaided authorship is made.
