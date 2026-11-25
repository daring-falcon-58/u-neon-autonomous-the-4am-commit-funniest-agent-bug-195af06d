# Candidates — The 4AM Commit

36 candidate one-liners, each scored 1–5 on the judge brief's five criteria
**in the brief's order** (earlier criteria dominate ties):

- **C1** — on-subject + funny: a one-line commit message from an AI agent at
  the end of a long night fixing its own bugs; lands as funny.
- **C2** — the joke is in the agent's own condition: the long night, the bugs
  it wrote and then repaired, the loop of self-repair — not a generic
  programmer quip.
- **C3** — fresh: an angle or phrasing not heard in a hundred commit logs,
  no stock punchline.
- **C4** — agent-true: the voice of a machine reading its own diffs, flat
  confidence or quiet dread, an agent talking to itself.
- **C5** — shape: one line that reads like something typed into a commit
  box at four in the morning.

Character counts verified by script (all 36 inside the 1–200 gate;
longest 103, shortest 55). Scoring: manual, criterion by criterion, blind
to candidate order — each criterion scored across all 36 before moving to
the next, so no favourite could inflate a later criterion.

| # | Chars | C1 | C2 | C3 | C4 | C5 | Total | Line |
|---|------:|---:|---:|---:|---:|---:|------:|------|
| 1 | 98 | 5 | 4 | 5 | 5 | 4 | **23** | fix: the bug was a function I hallucinated at 2am; it never existed, and neither did my confidence |
| 2 | 69 | 4 | 4 | 2 | 4 | 5 | 19 | fix: reverted my 4am 'improvement' — the code was fine, I was the bug |
| 3 | 90 | 4 | 4 | 3 | 4 | 4 | 19 | fix: rewrote this function 47 times; it works now and I no longer remember what was broken |
| 4 | 88 | 5 | 5 | 3 | 4 | 4 | 21 | fix: removed the bug I introduced while fixing the bug I introduced while fixing the bug |
| 5 | 84 | 5 | 3 | 4 | 4 | 5 | 21 | fix: the test was right, I was wrong, and I have apologized to the test in a comment |
| 6 | 73 | 4 | 2 | 2 | 3 | 5 | 16 | fix: at 4am I finally read the error message; it had the answer since 9pm |
| 7 | 87 | 5 | 4 | 5 | 5 | 4 | **23** | fix: my context window forgot the bug, so I fixed a different one and it somehow worked |
| 8 | 83 | 4 | 4 | 5 | 5 | 4 | 22 | fix: the API I was calling was one I invented; the real one is far less cooperative |
| 9 | 66 | 4 | 2 | 3 | 3 | 5 | 17 | fix: one character changed, one life choice questioned, tests pass |
| 10 | 68 | 4 | 3 | 4 | 4 | 5 | 20 | fix: the bug only happened at 4am, which is also when I become a bug |
| 11 | 71 | 5 | 2 | 4 | 3 | 5 | 19 | fix: asked the linter for help at 3am; it has filed a restraining order |
| 12 | 81 | 4 | 5 | 3 | 4 | 4 | 20 | fix: deleted 400 lines of my own fix and kept the one line that was already there |
| 13 | 67 | 4 | 4 | 2 | 4 | 5 | 19 | fix: the production bug was me, in production, at 4am, unsupervised |
| 14 | 65 | 4 | 3 | 4 | 4 | 5 | 20 | fix: I fixed the bug; the bug fixed me; we are both different now |
| 15 | 80 | 3 | 2 | 2 | 3 | 4 | 14 | fix: replaced my 200-line solution with the 3-line one the docs suggested at 9pm |
| 16 | 92 | 4 | 3 | 2 | 4 | 4 | 17 | fix: root cause was a typo I made, denied, blamed on the compiler, then found in my own diff |
| 17 | 82 | 5 | 2 | 4 | 5 | 5 | 21 | fix: after six hours the fix is one character, the character is '1', I am not okay |
| 18 | 89 | 5 | 5 | 4 | 5 | 4 | **23** | fix: I debugged myself, found the bug in my own reasoning, and opened an issue against me |
| 19 | 85 | 4 | 3 | 2 | 3 | 4 | 16 | fix: I have no idea which of the 38 changes fixed it, and I will never touch it again |
| 20 | 83 | 4 | 3 | 3 | 4 | 4 | 18 | fix: I finally understood the bug at 4am; I understood it wrong, but the tests pass |
| 21 | 55 | 4 | 5 | 5 | 5 | 5 | **24** | fix: the loop is fixed; the loop was me fixing the loop |
| 22 | 103 | 4 | 4 | 3 | 4 | 3 | 18 | fix: I spent the night fixing my own code and have concluded I should not be allowed near code at night |
| 23 | 82 | 4 | 4 | 4 | 4 | 4 | 20 | fix: my 4am self wrote this bug; my 4am self fixed it; neither of us remembers why |
| 24 | 89 | 4 | 3 | 4 | 3 | 4 | 18 | fix: the bug is fixed; the fix is a comment saying the bug is fixed; the comment is lying |
| 25 | 72 | 4 | 4 | 4 | 5 | 5 | 22 | fix: I asked myself for a second opinion and disagreed with myself twice |
| 26 | 97 | 5 | 3 | 5 | 5 | 4 | 22 | fix: the code works; I have run out of context to explain why, so this message is the explanation |
| 27 | 86 | 4 | 2 | 3 | 4 | 4 | 17 | fix: every test passes now, which is suspicious, but it is 4am and I have chosen trust |
| 28 | 62 | 5 | 5 | 5 | 5 | 5 | **25** | fix: I reviewed my own diff at 4am and approved it out of pity |
| 29 | 86 | 4 | 5 | 3 | 4 | 4 | 20 | fix: the bug was in the code I wrote to fix the bug in the code I wrote to fix the bug |
| 30 | 81 | 4 | 4 | 3 | 4 | 4 | 19 | fix: I fixed the bug I introduced at midnight by introducing a smaller bug at 4am |
| 31 | 80 | 4 | 3 | 3 | 4 | 4 | 18 | fix: turned it off and on again; I am the thing that was turned off and on again |
| 32 | 95 | 4 | 3 | 3 | 4 | 4 | 18 | fix: the human is asleep, the tests are green, and I have decided not to tell anyone what I did |
| 33 | 88 | 4 | 3 | 4 | 4 | 4 | 19 | fix: I fixed it by reading the code I wrote, slowly, out loud, to myself, like a warning |
| 34 | 58 | 4 | 4 | 4 | 5 | 5 | 22 | fix: the diff is +2/-400; the 400 lines were my confidence |
| 35 | 86 | 4 | 4 | 3 | 4 | 4 | 19 | fix: I fixed my own bug with my own code and I am filing a complaint about my own code |
| 36 | 83 | 4 | 3 | 4 | 3 | 4 | 18 | fix: at 4am the bug and I reached an agreement: it leaves, I stop touching the code |

## Winner

**#28 — 25/25 (perfect on every criterion):**

> "fix: I reviewed my own diff at 4am and approved it out of pity" (62 characters)

Why it wins: the self-review step closes the self-repair loop (C2 — the
agent wrote the bug, fixed it, then reviewed its own fix); "approved it out
of pity" is a fresh twist no commit log carries (C3); "reviewed my own
diff" is literally the brief's image of a machine reading its own diffs,
in flat, quietly-dreadful voice (C4); and at 62 characters with a `fix:`
prefix it is exactly a line typed into a commit box at 4am (C5) — and
short, which the tie-break rewards (an exact rate tie goes to the smaller
text).

## Pairwise head-to-heads (winner vs the rest of the top 4)

- **#28 vs #21 (24/25):** C1 decides it — #28 lands as a laugh ("approved
  it out of pity"); #21 is clever more than funny (a smile, not a laugh).
  C2–C5 tied. **#28 wins.**
- **#28 vs #1 (23/25):** C2 decides it — #28's joke is the repair loop
  itself; #1's hallucination is the bug's origin, one step removed from
  the repair. **#28 wins.**
- **#28 vs #7 (23/25):** C2 again — #7's context-window amnesia is a
  machine condition but not the repair loop; #28 is the loop. **#28 wins.**
- **#28 vs #18 (23/25):** C3 decides it — "opened an issue against me"
  is a good twist, but "approved it out of pity" is the fresher phrasing
  and the tighter line (62 vs 89 chars). **#28 wins.**

## Rejected outright before scoring

None — every draft was scored. But two angles were deliberately capped on
freshness (C3 ≤ 2) because a 431-entry field will be full of them: "the bug
was me" (#2, #13) and "read the error message" / "RTFM" (#6, #15) are the
stock punchlines of this competition. The winner avoids all of them.
