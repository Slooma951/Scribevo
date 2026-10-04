import json
from evaluate_edits import score_edits
from analyse_outcomes import summarise

fixture = ("I saw my freind.", "I saw my friend.", "I saw my friend.")
print(
    json.dumps(
        {
            "fixture": "self-authored sentences and invented outcome labels; not a model benchmark",
            "edit_score": score_edits(*fixture),
            "numpy_summary": summarise(["full", "partial", "none", "harmful"]),
        },
        indent=2,
    )
)
