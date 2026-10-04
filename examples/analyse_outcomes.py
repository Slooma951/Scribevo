"""New portfolio companion example: vectorised analysis of synthetic outcomes.

This is not part of the deployed extension or the original research model.
"""

from collections.abc import Iterable
import numpy as np

CATEGORIES = np.array(["full", "partial", "none", "harmful"])


def summarise(outcomes: Iterable[str]) -> dict:
    values = np.asarray(list(outcomes), dtype=str)
    if not np.isin(values, CATEGORIES).all():
        raise ValueError("Unknown correction outcome")
    counts = (values[:, None] == CATEGORIES[None, :]).sum(axis=0)
    return {
        "examples": int(values.size),
        "counts": {str(k): int(v) for k, v in zip(CATEGORIES, counts, strict=True)},
    }
