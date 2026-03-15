from logic_utils import check_guess, update_score, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_parse_guess_rejects_decimal():
    ok, value, err = parse_guess("12.5")
    assert ok is False
    assert value is None
    assert err == "Please enter a whole number."


def test_update_score_win_gives_points():
    score = update_score(0, "Win", 1)
    assert score == 100


def test_update_score_wrong_guess_loses_points():
    score = update_score(20, "Too High", 2)
    assert score == 15
