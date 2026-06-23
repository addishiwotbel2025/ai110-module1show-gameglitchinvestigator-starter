def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Hard":
        return 1, 50
    return 1, 100  # Normal / default


def parse_guess(raw, low=None, high=None):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)

    If low/high are provided, guesses outside [low, high] are rejected.
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        value = int(float(raw)) if "." in raw else int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a number."

    if low is not None and high is not None and (value < low or value > high):
        return False, None, f"Out of range. Pick a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome is one of: "Win", "Too High", "Too Low".
    Both values are coerced to int so a stray string never flips the result.
    """
    guess = int(guess)
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        # Guess is too high -> the player should go LOWER.
        return "Too High", "📉 Go LOWER!"
    # Guess is too low -> the player should go HIGHER.
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number. Never drops below 0."""
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number + 1))
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return max(0, current_score - 5)

    return current_score


def new_game_state(secret: int):
    """Fresh game state for starting (or replaying) a game.

    Resetting status back to "playing" is what lets a user play again
    after they have won or lost.
    """
    return {"secret": secret, "attempts": 0, "score": 100, "status": "playing"}
