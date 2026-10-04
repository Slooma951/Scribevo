import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples"))
from evaluate_edits import score_edits, harmful_token_count, edit_set
from analyse_outcomes import summarise


class EvaluationTests(unittest.TestCase):
    def test_exact_correction(self):
        r = score_edits("I saw my freind.", "I saw my friend.", "I saw my friend.")
        self.assertEqual(
            (r["true_positive"], r["false_positive"], r["false_negative"]), (1, 0, 0)
        )
        self.assertEqual(r["f0_5"], 1.0)

    def test_missed_correction(self):
        r = score_edits("my freind", "my friend", "my freind")
        self.assertEqual(r["false_negative"], 1)

    def test_extra_edit_reduces_precision_and_f05(self):
        r = score_edits(
            "I saw freind with tea", "I saw friend with tea", "I saw friend with coffee"
        )
        self.assertEqual(
            (r["true_positive"], r["false_positive"], r["false_negative"]), (1, 1, 0)
        )
        self.assertEqual(r["precision"], 0.5)
        self.assertEqual(r["recall"], 1.0)
        self.assertAlmostEqual(r["f0_5"], 5 / 9)

    def test_unnecessary_edit_is_harmful(self):
        self.assertEqual(
            harmful_token_count("I like tea.", "I like tea.", "I love tea."), 1
        )

    def test_reference_permitted_edit_is_not_harmful(self):
        self.assertEqual(
            harmful_token_count("i go yesterday", "I went yesterday", "I go yesterday"),
            0,
        )

    def test_empty_input_has_defined_score(self):
        self.assertEqual(score_edits("", "", "")["f0_5"], 0.0)

    def test_insertions_are_edits(self):
        self.assertEqual(len(edit_set("I write", "I can write")), 1)

    def test_repeated_tokens_keep_alignment(self):
        self.assertEqual(len(edit_set("the the book", "the book")), 1)

    def test_numpy_counts_each_outcome(self):
        self.assertEqual(
            summarise(["full", "full", "harmful"])["counts"],
            {"full": 2, "partial": 0, "none": 0, "harmful": 1},
        )

    def test_numpy_empty_input(self):
        self.assertEqual(summarise([])["examples"], 0)

    def test_numpy_rejects_unknown_labels(self):
        with self.assertRaises(ValueError):
            summarise(["unknown"])


if __name__ == "__main__":
    unittest.main()
