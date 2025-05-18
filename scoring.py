# scoring.py

"""
Translation Evaluation Scoring Prototype

This function compares user ratings with expert annotations and returns a score.
The scoring system is based on three levels:
- 100 points: exact match
- 50 points: 1-point difference (partial match)
- 0 points: other cases (mismatch)
"""

def score_dimension(user_score: int, expert_score: int) -> int:
    """Score a single evaluation dimension."""
    if user_score == expert_score:
        return 100
    elif abs(user_score - expert_score) == 1:
        return 50
    else:
        return 0

def evaluate_translation(user_eval: dict, expert_eval: dict) -> dict:
    """
    Compare user and expert scores for all dimensions.

    Returns a score breakdown and total score percentage.
    """
    score_breakdown = {}
    total_points = 0
    max_points = 100 * len(expert_eval)

    for dimension, expert_score in expert_eval.items():
        user_score = user_eval.get(dimension, 0)
        score = score_dimension(user_score, expert_score)
        score_breakdown[dimension] = score
        total_points += score

    total_percentage = round((total_points / max_points) * 100, 2)
    return {
        "score_by_dimension": score_breakdown,
        "total_score_percent": total_percentage
    }

# Example usage
if __name__ == "__main__":
    user = {"fluency": 4, "adequacy": 3}
    expert = {"fluency": 5, "adequacy": 3}
    print(evaluate_translation(user, expert))
