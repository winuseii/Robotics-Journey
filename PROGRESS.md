# PROGRESS — Dashboard

**V** · synced 26 Jul 2026 (from live `Robotics_Log` in Drive)
Full plan → `Robotics_Curriculum_v5_1_1_1.pdf` (Iron Man Protocol, project files)
Detailed session log → `Robotics_Log` (Google Drive) — the high-frequency source of truth
Claude, the Mentor/Sensei. Vinayak the student.

---

## METHOD
Project-driven. Builds lead; concepts pulled in on demand.
**BIG** knowledge gap → route to the topic chat (chat + exact prompt + what to bring back). **Small** gaps handled inline.
**MAT + DSA** on independent drip (too deep / too unforced to learn reactively).
Every project ends in a **20-min EXTRACT**. **Artifact rule:** filmed, committed, showable.
**Floor** 20 min/day · **Ceiling** 3 hr. `/contexts` at session start to sync across chats.

## TRACKS
| Track | L | Next action |
|---|---|---|
| ELE | 2.5 | Day 2 — `digitalRead` (converges with PRJ button build) |
| MAT | 2.5 | Eigenvalues (drip, ~2×/wk) |
| PRG | 2 | Repo cleanup + first tests (see DEBT) |
| MEC | 2 | Fusion 360 fundamentals |
| **PRJ** | **2** | **Day 2 — button input (pedestrian request) or servo actuation** |
| DSA | 0 | Big O (drip, ~1–2 problems/wk) |
| AIM | 0 | gated on MAT L3–4 |

*L: 0 none · 1 exposed · 2 with help · 3 alone · 4 fluent · 5 can teach*

## CAPABILITY GATES
- **G1 — it moves** (sensor + actuator, filmed) → end July · *PRJ Day 2 servo/button is the doorway*
- **G2 — it thinks** (sense → filter → decide → act) → Sept
- **G3 — it's designed** (CAD'd, fabricated body) → Oct
- **G4 — autonomous** → Sem 4

## BUILDS
- ✅ **Traffic light** (26 Jul) — 3 LEDs pins 8/9/10, 220Ω each, `setState`. `.ino` + video + README pushed. Bonus: traffic-pattern blink.
- 🔴 **ACTIVE — Robowar** (design team). Need: weight class · ruleset · date · budget · fab access.
- ⏸ **ON HOLD — ACM×ASME** (internal team issues).
- ⭐ **NORTH STAR — SRL extra arms.** Gated until G2. Control (EMG/spare-muscle) is the hard part. Load path → pelvis.

## DEBT (fix in PRG Day 1)
- [ ] `day3_matrix_advanced.py` — two `__main__` blocks, second clobbers first
- [ ] README is a stub
- [ ] zero tests anywhere
- [ ] restructure repo by track; delete `Phase 0/`

## SEM 3
Midterms **13 Aug** · Onam build window **25–30 Aug** · End sems **29 Oct** · attendance **75%**
`23MAT222` = free probability track (attend + translate)

## ⚠️ RECURRING PATTERN — WATCH
Voltage/current confusion has now surfaced and been re-closed **three times** (12 Jul, 13 Jul, 24 Jul). Root: *flow-of-substance* intuition — treating current as stuff travelling, not a rate set by the whole loop. It keeps coming back. It is not closed for good until it stops resurfacing. Next ELE session, test it cold.

## RECENT LOGS (rolling — full history in Drive)
- **2026-07-24 · PRJ** — Traffic light built. Voltage/current confusion resurfaced → closed (per-LED current limiting, independence). Backwards-LED failure mode observed (reverse-biased diode blocks current). Artifact: `.ino` + video + README. Conf 4. → PRJ Day 2 (button/servo).
- **2026-07-13 · ELE** — First artifact. `day1_blink.ino` pushed + filmed. Killed "resistor before LED." Conf 4.
- **2026-07-12 · ELE** — V/I/R, LED-as-diode, resistor calc. Voltage misconception found. Artifact NONE (Day 1 incomplete). Conf 4, **gap flag X**.
