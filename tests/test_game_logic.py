from logic_utils import (
    check_guess,
    update_score,
    parse_guess,
    new_game_state,
)


# ---------------------------------------------------------------------------
# Bug 1: "Too High" / "Too Low" outcomes and hint messages
# ---------------------------------------------------------------------------

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high_outcome():
    # guess 60 vs secret 50 -> too high
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low_outcome():
    # guess 40 vs secret 50 -> too low
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_hint_says_go_lower():
    # If you guessed too high, the hint must tell you to go LOWER.
    _, message = check_guess(60, 50)
    assert "LOWER" in message.upper()


def test_too_low_hint_says_go_higher():
    # If you guessed too low, the hint must tell you to go HIGHER.
    _, message = check_guess(40, 50)
    assert "HIGHER" in message.upper()


def test_string_secret_does_not_flip_result():
    # Even if the secret arrives as a string, the comparison stays correct.
    outcome, _ = check_guess(60, "50")
    assert outcome == "Too High"


# ---------------------------------------------------------------------------
# Bug 2: Final score should never go negative
# ---------------------------------------------------------------------------

def test_wrong_guess_does_not_go_below_zero():
    # Starting at 0, a wrong guess must not push the score negative.
    assert update_score(0, "Too Low", 1) == 0
    assert update_score(0, "Too High", 1) == 0


def test_repeated_wrong_guesses_stay_at_zero():
    score = 0
    for attempt in range(1, 6):
        score = update_score(score, "Too Low", attempt)
    assert score == 0


def test_wrong_guess_deducts_when_score_is_positive():
    assert update_score(20, "Too Low", 1) == 15


def test_win_adds_points():
    assert update_score(0, "Win", 1) > 0


# ---------------------------------------------------------------------------
# Bug 3: Out-of-range guesses must be rejected
# ---------------------------------------------------------------------------

def test_in_range_guess_is_accepted():
    ok, value, err = parse_guess("50", 1, 100)
    assert ok is True
    assert value == 50
    assert err is None


def test_guess_above_range_is_rejected():
    ok, value, err = parse_guess("999", 1, 100)
    assert ok is False
    assert value is None
    assert err is not None


def test_guess_below_range_is_rejected():
    ok, value, err = parse_guess("0", 1, 100)
    assert ok is False
    assert err is not None


def test_non_number_is_rejected():
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False


# ---------------------------------------------------------------------------
# Bug 4: A user can replay after winning (status resets to "playing")
# ---------------------------------------------------------------------------

def test_new_game_state_resets_status_to_playing():
    state = new_game_state(42)
    assert state["status"] == "playing"


def test_new_game_state_resets_counters():
    state = new_game_state(42)
    assert state["attempts"] == 0
    assert state["score"] == 100
    assert state["secret"] == 42
