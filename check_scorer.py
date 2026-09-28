# check_scorer.py — scratch script, not part of your submission.
# Drop it in your repo root next to scorer.py, questions.py, run_eval.py.
# Delete it once you trust your scorer. It never gets imported by anything else.

from scorer import judge

# ---------------------------------------------------------------------------
# Step 1: fill these in with something REAL.
#   QUESTION and EXPECTS come from an entry in questions.py.
#   REAL_ANSWER comes from actually running:
#       python app.py ask "your question here"
#   and pasting what it printed. Don't paraphrase it yourself — copy it.
# ---------------------------------------------------------------------------

QUESTION = "PASTE ONE QUESTION FROM questions.py HERE"
EXPECTS = "PASTE THAT QUESTION'S expects PHRASE HERE"
REAL_ANSWER = """PASTE THE ACTUAL OUTPUT OF `python app.py ask "..."` HERE"""

# Leave this empty unless your judge() actually reads fields off `results`
# (e.g. distance, sources). A plain substring check doesn't need it.
RESULTS = []

# ---------------------------------------------------------------------------
# Step 2: does judge() agree with what a human would say here?
# ---------------------------------------------------------------------------

print("\n--- Step 2: real answer ---")
print("QUESTION:", QUESTION)
print("EXPECTS: ", EXPECTS)
print("VERDICT: ", judge(QUESTION, EXPECTS, REAL_ANSWER, RESULTS))
print("Expected: True — if REAL_ANSWER above genuinely contains EXPECTS,")
print("this should pass. If it prints False, read REAL_ANSWER again —")
print("either the answer doesn't say what you think, or your judge()")
print("logic has a bug (check for case-sensitivity first).")

# ---------------------------------------------------------------------------
# Step 3: two fake cases, written BY HAND to probe the edges.
# ---------------------------------------------------------------------------

# 3a. Paraphrase: same meaning, different words. A plain substring match
#     should NOT be able to find EXPECTS in here.
PARAPHRASED = REAL_ANSWER.replace(EXPECTS, "[the same fact, worded differently]")

print("\n--- Step 3a: paraphrased answer (should be a FALSE NEGATIVE) ---")
print("VERDICT: ", judge(QUESTION, EXPECTS, PARAPHRASED, RESULTS))
print("Expected: False. The fact is still correct, but your scorer can't")
print("see that — it only checks for the literal phrase. This is the")
print("blind spot: a correct answer this scorer will wrongly fail.")

# 3b. Hallucination: correct fact PLUS an invented sentence tacked on.
#     The phrase is still there, so a substring check will pass it —
#     even though part of the answer is made up.
HALLUCINATED = REAL_ANSWER + " Also, this location is open 24 hours on weekends."

print("\n--- Step 3b: hallucinated answer (should be a FALSE POSITIVE) ---")
print("VERDICT: ", judge(QUESTION, EXPECTS, HALLUCINATED, RESULTS))
print("Expected: True. EXPECTS is still in the string, so your scorer")
print("passes it — even though the second sentence is invented and never")
print("came from your retrieved chunks. This is the OTHER blind spot:")
print("a bad answer this scorer will wrongly pass.")

print("\nIf Step 2 didn't print True, or 3a/3b didn't match what's")
print("described above, don't move on to run_eval.py yet — fix judge()")
print("first. Paste what actually printed and we'll debug it.")