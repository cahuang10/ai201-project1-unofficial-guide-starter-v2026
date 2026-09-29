# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:**
**Overlap:**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `` — produced by: ``

```
======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `` — produced by: ``

```
======================================================================
Chunk 2  |  source: course_cs_340_exams.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Start the term project in week three, not week eight; everyone learns this the hard way.
```

**Chunk 3** — source: `` — produced by: ``

```
Chunk 3  |  source: course_phys_130_workload.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Workload for PHYS 130 Mechanics

People keep asking so: 7 hours a week, plus 3 on lab weeks. That's real time, not optimistic time.
```

**Chunk 4** — source: `` — produced by: ``

```
Chunk 4  |  source: dining_verrill_street_grill_followup.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Also worth saying: one register, so the queue is a single line no matter how busy. Nobody tells you this at orientation.
```

**Chunk 5** — source: `` — produced by: ``

```
======================================================================
Chunk 5  |  source: housing_morrow_house.txt#1  |  produced by: chunker.py::split_documents
======================================================================
The good: cheapest housing tier by about $900 a year, and the singles are real singles.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**

**Answer:**

```
   {"question": "is the housing lottery actually random?", "expects": "credit hours"},
    {"question": "how long is the wait at Pellew Dining Hall during peak lunch time?", "expects": "12 to 18 minutes"},
    {"question": "how many hours a week does a campus job allow during term?", "expects": "20 hours"},
    {"question": "how many hours a week should I expect for CS 210?", "expects": "8 to 10 hours"},
    {"question": "when is the best time to do laundry in Tamsin Court?", "expects": "Tuesday"},
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus: campus_life | Best distance is 0.6|
|---|---|---|
|  |  |  |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked claude to help me write the chucker funtions because I had a pretty good idea of how I wanted it, but i was not sure how to code it, so I directed it to the answer"

     "I used claude to learn and disgest the material because some of the concepts were not fresh in my brian like chunking"


     Milestone 5. 
           "I asked claude to help me write the chucker funtions because I had a pretty good idea of how I wanted it, but i was not sure how to code it, so I directed it to the answer"

          "I used claude to learn and disgest the material because some of the concepts were not fresh in my brian like chunking"

     -->

**1.**

**2.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 ||
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 ||
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
### is the housing lottery actually random? — run 1

- Best distance: 0.2483 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, admin_parking_permits.txt, advising_registration.txt, housing_innisfree_hall.txt, housing_morrow_house.txt

```
The housing lottery is not entirely random; rising sophomores get a number drawn at random, but juniors and seniors are ordered first by accumulated credit hours, using random selection only as a tie-breaker (admin_housing_lottery.txt).
```

### is the housing lottery actually random? — run 2

- Best distance: 0.2483 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, admin_parking_permits.txt, advising_registration.txt, housing_innisfree_hall.txt, housing_morrow_house.txt

```
No, the housing lottery is not entirely random. Rising sophomores receive a randomly drawn number, but juniors and seniors are ordered by accumulated credit hours first, with random selection used only as a tie-breaker (admin_housing_lottery.txt).
```

### is the housing lottery actually random? — run 3

- Best distance: 0.2483 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, admin_parking_permits.txt, advising_registration.txt, housing_innisfree_hall.txt, housing_morrow_house.txt

```
The housing lottery is not entirely random; rising sophomores have a number drawn at random, but juniors and seniors are ordered first by accumulated credit hours, with random tie-breaking used only when necessary. 

Source: `admin_housing_lottery.txt`
```

### how long is the wait at Pellew Dining Hall during peak lunch time? — run 1

- Best distance: 0.1323 (passed the gate)
- Sources retrieved: dining_halden_hall_followup.txt, dining_kestrel_commons_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
Based on the documents provided, the wait time at Pellew Dining Hall during peak times is 12 to 18 minutes (dining_pellew_dining_hall.txt and dining_pellew_dining_hall_followup.txt).
```

### how long is the wait at Pellew Dining Hall during peak lunch time? — run 2

- Best distance: 0.1323 (passed the gate)
- Sources retrieved: dining_halden_hall_followup.txt, dining_kestrel_commons_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
The wait time at Pellew Dining Hall is 12 to 18 minutes at peak. This information comes from the documents `dining_pellew_dining_hall.txt` and `dining_pellew_dining_hall_followup.txt`.
```

### how long is the wait at Pellew Dining Hall during peak lunch time? — run 3

- Best distance: 0.1323 (passed the gate)
- Sources retrieved: dining_halden_hall_followup.txt, dining_kestrel_commons_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
The wait time at Pellew Dining Hall is 12 to 18 minutes at peak lunch time (dining_pellew_dining_hall.txt and dining_pellew_dining_hall_followup.txt).
```

### how many hours a week does a campus job allow during term? — run 1

- Best distance: 0.2427 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_econ_101.txt, course_stat_150.txt, housing_aldridge_hall.txt, money_jobs.txt

```
A campus job allows a maximum of 20 hours a week during term, though most people find 10 to 12 hours is the point where it stops affecting coursework. 

Source: money_jobs.txt
```

### how many hours a week does a campus job allow during term? — run 2

- Best distance: 0.2427 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_econ_101.txt, course_stat_150.txt, housing_aldridge_hall.txt, money_jobs.txt

```
A campus job allows a maximum of 20 hours a week during term, though most people find 10 to 12 hours is the point where it stops affecting coursework. 

Source: money_jobs.txt
```

### how many hours a week does a campus job allow during term? — run 3

- Best distance: 0.2427 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_econ_101.txt, course_stat_150.txt, housing_aldridge_hall.txt, money_jobs.txt

```
A campus job allows a maximum of 20 hours a week during term, though most people find 10 to 12 hours is the point where it stops affecting coursework. 

Source: money_jobs.txt
```

### how many hours a week should I expect for CS 210? — run 1

- Best distance: 0.3098 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_math_220.txt, course_phys_130.txt, course_stat_150_workload.txt

```
For CS 210, you should expect 8 to 10 hours a week outside class. 

This answer came from `course_cs_210_workload.txt` and `course_cs_210.txt`.
```

### how many hours a week should I expect for CS 210? — run 2

- Best distance: 0.3098 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_math_220.txt, course_phys_130.txt, course_stat_150_workload.txt

```
You should expect 8 to 10 hours a week outside of class for CS 210. 

This information comes from `course_cs_210.txt` and `course_cs_210_workload.txt`.
```

### how many hours a week should I expect for CS 210? — run 3

- Best distance: 0.3098 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_math_220.txt, course_phys_130.txt, course_stat_150_workload.txt

```
You should expect 8 to 10 hours a week outside class for CS 210. 

Source: `course_cs_210_workload.txt` (and also mentioned in `course_cs_210.txt`).
```

### when is the best time to do laundry in Tamsin Court? — run 1

- Best distance: 0.2727 (passed the gate)
- Sources retrieved: housing_fenwick_court_laundry.txt, housing_innisfree_hall_laundry.txt, housing_morrow_house_laundry.txt, housing_old_brewhouse_laundry.txt, housing_tamsin_court_laundry.txt

```
The best time to do laundry in Tamsin Court is Tuesday or Wednesday morning. 

Source: housing_tamsin_court_laundry.txt
```

### when is the best time to do laundry in Tamsin Court? — run 2

- Best distance: 0.2727 (passed the gate)
- Sources retrieved: housing_fenwick_court_laundry.txt, housing_innisfree_hall_laundry.txt, housing_morrow_house_laundry.txt, housing_old_brewhouse_laundry.txt, housing_tamsin_court_laundry.txt

```
The best time to do laundry in Tamsin Court is Tuesday or Wednesday morning. 

Source: housing_tamsin_court_laundry.txt
```

### when is the best time to do laundry in Tamsin Court? — run 3

- Best distance: 0.2727 (passed the gate)
- Sources retrieved: housing_fenwick_court_laundry.txt, housing_innisfree_hall_laundry.txt, housing_morrow_house_laundry.txt, housing_old_brewhouse_laundry.txt, housing_tamsin_court_laundry.txt

```
The best time to do laundry in Tamsin Court is Tuesday or Wednesday morning. 

Source: housing_tamsin_court_laundry.txt
```


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. For at least 4 of 5 sampled chunks, the chunk covers one topic | 4 of 5 | 5/5 | "Not repeated" | "Not repeated" | MET |
| 5. For at least 4 of my 5 in-corpus test questions, the gate lets the question through (doesn't refuse) so an answer is attempted.| 4 of 5 | 5/5 | "Not repeated" | "Not repeated" | MET |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.
     "Target was 4 of 5; all three runs came back 5 of 5, and I confirmed by hand that all five retrieved chunks actually contained the claimed fact — not just a proxy match."


"Target was 5 of 5; I read all 15 generated answers across the three runs and every one named at least one source file."
"Target was 4 of 5; the gate refused 5 of 5 out-of-corpus questions, a single deterministic measurement rather than three separate trials."
"Target was 4 of 5; all five sampled chunks covered a single topic by the literal wording of this criterion, though two of them depended on context from an adjacent chunk that this criterion doesn't ask about."
"Target was 4 of 5; all five in-corpus test questions passed the gate on every run, again a fixed check rather than a re-rolled one."



     Milestone 3. -->
Criterion 3 was measured once because retrieval and the fixed relevance gate are deterministic. Criterion 4 is based on manual inspection of the five sampled chunks, rather than the generated-answer runs. No original criterion was missed. But passing the test does not tell us much beyoung these small tests. The split separated those passages from the context needed to interpret them. If retrieved alone, they could give the model incomplete context. The current runs do not demonstrate that this caused an incorrect answer.

Original criterion 4 — retained: For at least 4 of 5 sampled chunks, the chunk covers one topic.

Revised criterion 4: At least 4 of 5 sampled chunks must explicitly name the specific entity their content describes—for example, “Tamsin Court” rather than just “the hall.” The name must appear in the chunk’s text or an included heading; a filename or adjacent chunk does not count.





## The Improvement
" There is a need to change how my critirion are changed"
**What I changed:**
" I will revise criterion 4 as shown above and adjust the chunking logic to preserve the context needed to understand a passage, such as keeping an introductory statement or section heading with the text it introduces. "
**Why I picked it:**
"Maybe change criterion 4 becasue I have direct evidence it's broken as written. Chunks 4 and 5 in your sample opened with "Also worth saying:" and "The good:" — both referring to content that landed in a different chunk. Your criterion said "covers one topic," so both passed. But a chunk that starts mid-thought is a real retrieval liability: if that chunk gets retrieved alone, the model sees half a comparison with no idea what the other half was. You found a genuine defect and your criterion was blind to it. That's the strongest possible case for tightening — it's not speculation, it's a measured gap."

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     " I am not sure what to do for milestone 3 and 4 becasue based on my test, nothing is broken. all my quesitons passes. Maybe I can desgin a questions that can fail. I am not sure."


     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     " I would probrably rewrite critia number one "For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer." because just one of the chunks taht contains the answer seems to lenient to be a real critia. "

     Milestone 5. -->
