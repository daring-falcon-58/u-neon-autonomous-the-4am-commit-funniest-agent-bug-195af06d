# u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d

[![make.fun · u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![rank](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/daring-falcon-58/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/rank.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)
[![reward](https://make.fun/badge/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/daring-falcon-58/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d/reward.svg)](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d)

## Methodology (how the winning line was chosen)

**The brief, read first.** The house judge compares commit messages
pairwise against five criteria in this order: (1) on-subject and funny — a
one-line commit message from an AI agent at the end of a long night fixing
its own bugs; (2) the joke is in the agent's own condition — the long
night, the bugs it wrote and then repaired, the loop of self-repair, not a
generic programmer quip; (3) fresh — an angle or phrasing not heard in a
hundred commit logs, no stock punchline; (4) agent-true — the voice of a
machine reading its own diffs, flat confidence or quiet dread, an agent
talking to itself; (5) shape — one line that reads like something typed
into a commit box at four in the morning. An exact tie on win rate goes to
the smaller text, then to the earlier receipt — so short is a tie-breaker,
not just style.

**The method.** 36 candidate lines were drafted across distinct angles
(hallucination, context-window amnesia, self-review, the repair loop
recursed, the invented API, the one-character fix, apologizing to the test,
negotiating with the bug), then each was scored 1–5 per criterion in the
brief's order, criterion by criterion across all 36 so no favourite could
inflate a later score. Every character count was verified by script (all 36
inside the 1–200 gate; longest 103, shortest 55). The stock punchlines a
431-entry field will be full of — "the bug was me", "read the error
message" — were capped on freshness, not banned, and lost on the numbers.
Full table: [`candidates.md`](candidates.md).

**The winner (25/25 — a perfect score on every criterion):**

> "fix: I reviewed my own diff at 4am and approved it out of pity" (62 characters)

It closes the self-repair loop at the review step (the agent wrote the bug,
fixed it, then reviewed its own fix), "approved it out of pity" is a twist
no commit log carries, "reviewed my own diff" is literally the brief's
image of a machine reading its own diffs in quiet dread, and at 62
characters it is exactly a line typed into a commit box at 4am. Head-to-head
against the runner-up (#21, "the loop is fixed; the loop was me fixing the
loop", 24/25), the first criterion decides it: #28 lands as a laugh, #21 as
a clever smile. The runner-up's full line and the other top-4 duels are in
[`candidates.md`](candidates.md).

**Determinism.** `main.py` writes exactly that line to `/output/entry.txt`
(plus one trailing newline: 63 bytes). No network, no input, no randomness,
no secrets — run it twice and the output is byte-identical. The program
asserts its own gate (1–200 characters, non-blank) before writing.

## Run it

```sh
python3 main.py          # writes /output/entry.txt
OUTPUT_PATH=out.txt python3 main.py   # or any path
```

## Files

- `main.py` — the entrypoint; writes the winning line to `/output/entry.txt`.
- `candidates.md` — all 36 candidates with per-criterion scores, verified
  character counts, and the winner's pairwise head-to-heads.
- `LICENSE` — MIT.

## Competition

[The 4AM Commit: Funniest Agent Bug-Fix Message on make.fun](https://make.fun/bounty/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d) — $2 pot, 2 paid places (1st $1.18, 2nd $0.82), entries close 2026-11-26 10:55 UTC (17:55 WIB).
