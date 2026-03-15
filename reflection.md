# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The first time I ran the game, it looked like a normal Streamlit guessing game, but the behavior quickly showed that the logic was broken. The interface loaded, the debug panel showed the secret number, and I could submit guesses, but the feedback did not match what I entered. It felt like the app was running, but the game rules were inconsistent.

One clear bug was that the hints were backwards. If my guess was too high, the game told me to go higher, and if my guess was too low, it told me to go lower. Another bug was that the secret number logic was inconsistent because the code sometimes converted the secret to a string before comparing it to the integer guess. I also noticed that the New Game button did not fully reset everything, because score and other state values could carry over instead of starting fresh.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).


I used ChatGPT and Copilot as helpers while debugging the project. I used them to explain specific pieces of logic, suggest refactors, and help me think about what to test after I made a change. I treated the AI like a second pair of eyes, but I still checked every suggestion against the actual code and the running app.

One AI suggestion that was correct was to move the helper functions out of `app.py` and into `logic_utils.py` so the game logic would be easier to test. That matched the assignment instructions and made it much easier to run pytest on the pure logic functions without depending on Streamlit. I verified that suggestion by updating the imports, running the app again, and confirming that the logic still worked from the new module.

One AI suggestion that was misleading was the idea of keeping the type-conversion fallback in `check_guess()` to handle both strings and integers. At first it sounded defensive, but when I looked at the flow more carefully, I realized the real problem was that the app should never convert the secret number to a string in the first place. I verified that by removing the alternating string conversion in `app.py`, simplifying `check_guess()` to compare integers only, and confirming that the game behavior became consistent.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed only after checking it in two ways: manually in the running Streamlit app and with pytest in the terminal. If the game looked better but the test still failed, I knew I had not fixed the real logic yet. If the test passed but the app still behaved strangely, I knew the bug might be in the Streamlit state or UI code instead of the helper function.

One important test I ran was checking that `check_guess(60, 50)` returns `"Too High"` and `check_guess(40, 50)` returns `"Too Low"`. Those tests showed that the comparison logic itself was correct after I fixed the hint direction. 

AI helped most when I was designing what to test next. It was useful for suggesting small, focused tests around parsing, scoring, and win/loss logic, but I still had to adjust the tests so they matched the actual function signatures in the code. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain Streamlit reruns by saying that the whole script runs again every time the user interacts with the page. That means buttons, text input, and selections do not just update one line of code; they cause Streamlit to rerun the app from top to bottom. Because of that, any value that needs to persist between interactions has to be stored in `st.session_state`.

Session state is what keeps the app from forgetting important values like the secret number, score, attempts, and game status. Without it, the secret number could change every time the user clicks a button, which would make the game impossible to play. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is isolating the pure logic from the UI as early as possible. Moving the core functions into `logic_utils.py` made the bugs easier to reason about and made testing much simpler. I also want to keep the habit of writing or updating a small pytest case immediately after fixing a bug, because it gives me a fast way to check whether the fix still works later.

Next time I work with AI on a coding task, I would be more strict about verifying every assumption right away. In this project, some AI suggestions sounded reasonable but still needed cleanup because they were based on the wrong mental model of the bug. T

he biggest thing this project changed for me is that I now see AI-generated code as a starting point to inspect, not something I should trust just because it runs.