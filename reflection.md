# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
when I put in a value, it asked me to guess a value that is lower even if I had to guess a value that was higher
- List at least two concrete bugs you noticed at the start  
it says 'go lower' no matter what
my final score is a negative value
it lets me put in a value that is out of range and tells me to go higher
it doesnt let me play a new game after i win. It still says "you have won" from the previous game
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

guess: 98
| Input | Expected Behavior | Actual Behavior | Console Output / Error |
38| go higher | go lower
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
it suggested that the "too high" and "too low" were interchanged. And it showed me the line number. I verified that it is true by checking the code
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
It didn't mislead me so far.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested whether it is working after each fix. 
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I tested whether the prompt was still accepting inputs that were out of range. 
After the fix, it told me to put a number that is in range. I realized that the code was working.

- Did AI help you design or understand any tests?
 How?
It helped me build test cases based on the bugs I told it. 
I followed instructions to generate test cases in test_game_logic.py using claude
It also helped me generate terminal codes to run

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I might make the correct edits, but they might not be in the right place. 
For example, the edits I made in app.py, claude recommended me to make the edits in logic_utils.py. 
this helps me stay organized
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
commit my changes frequently
I would check if one bug fix introduces another bug
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It is good to use AI as a helper. However, we have to review and understand the changes that are being made.
