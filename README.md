# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- its purpose is to play a guessing game
- 1. "too high" and "too low" were interchanged
  2. I can't play again after I win, it doesn't reset
  3. It accepts inputs out of range
  4. score is sometimes a negative value

- 1. I interchanged  "too high" and "too low" in app.py (claude did) line 32-47
   2. I made claude check whether the input is in the correct range and return an appropriate text to the user line 14 - 29
   3. Capped the final score to 0. line 50-65
   4. reset "playing" after winning line 134-140


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. secret number: 38
2. enter 5
3. returns "go higher"
4. enter 50
5. returns "go lower"
6. I enter 38
7. returns "you won" and it gives me the score.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
                                                                                                      
tests/test_game_logic.py::test_winning_guess PASSED                                                                     [  6%]
tests/test_game_logic.py::test_guess_too_high_outcome PASSED                                                            [ 12%]
tests/test_game_logic.py::test_guess_too_low_outcome PASSED                                                             [ 18%]
tests/test_game_logic.py::test_too_high_hint_says_go_lower PASSED                                                       [ 25%]
tests/test_game_logic.py::test_too_low_hint_says_go_higher PASSED                                                       [ 31%]
tests/test_game_logic.py::test_string_secret_does_not_flip_result PASSED                                                [ 37%]
tests/test_game_logic.py::test_wrong_guess_does_not_go_below_zero PASSED                                                [ 43%]
tests/test_game_logic.py::test_repeated_wrong_guesses_stay_at_zero PASSED                                               [ 50%]
tests/test_game_logic.py::test_wrong_guess_deducts_when_score_is_positive PASSED                                        [ 56%]
tests/test_game_logic.py::test_win_adds_points PASSED                                                                   [ 62%]
tests/test_game_logic.py::test_in_range_guess_is_accepted PASSED                                                        [ 68%]
tests/test_game_logic.py::test_guess_above_range_is_rejected PASSED                                                     [ 75%]
tests/test_game_logic.py::test_guess_below_range_is_rejected PASSED                                                     [ 81%]
tests/test_game_logic.py::test_non_number_is_rejected PASSED                                                            [ 87%]
tests/test_game_logic.py::test_new_game_state_resets_status_to_playing PASSED                                           [ 93%]
tests/test_game_logic.py::test_new_game_state_resets_counters PASSED  

16 passed in 0.01s ======================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
