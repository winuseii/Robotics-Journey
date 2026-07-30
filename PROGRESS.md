# PROGRESS — Dashboard

**V** · synced **30 Jul 2026** (from live `Robotics_Log` + `/context` sweep of ELE & PRJ chats)
Reference layer: `Robotics_Curriculum_v5_1_1_1.pdf` (Iron Man Protocol — theory order) · `bioroboticsroadmap` (project bank + quality bar) · calendar = `Attendance_Tracker` (Drive)
Detailed session log → `Robotics_Log` (Drive) — high-frequency source of truth

---

## ⏱ COUNTDOWN (from 30 Jul)
- **Midterms — 13 Aug → 14 days**
- Onam build window — 25–30 Aug → 26 days
- **Robowars design freeze — 15 Sept → 47 days** (8-week CAD ramp should be running NOW)
- End sems — 29 Oct · attendance floor 75%

## METHOD
Project-driven. Builds lead; concepts pulled in on demand. BIG gap → route to topic chat. Small → inline.
MAT + DSA on independent drip. Every build ends in a 20-min EXTRACT.
`/context` at session start to sync across chats. **Floor** 20 min/day · **Ceiling** 3 hr.

## ⚠️ ARTIFACT RULE (upgraded)
Every build ships **(1) a NUMBER** (measured, plotted, defensible) **(2) a 40-sec video (3) a public commit.**
Define the metric *before* building. "It works" is not a result.

## TRACKS
| Track | L | Next action |
|---|---|---|
| ELE | 2.5 | ✅ Day 2 (button) DONE. Day 3 not started — or advance via PRJ servo |
| MAT | 2.5 | Eigenvalues (drip ~2×/wk) |
| PRG | 2 | Repo cleanup + first tests (see DEBT) |
| MEC | 2 | **Fusion 360 fundamentals — URGENT (Robowars freeze 15 Sept)** |
| PRJ | 2 | **Day 2 = drive one servo** — ⛔ BLOCKED: servos not arrived |
| DSA | 0 | Big O (drip ~1–2/wk) |
| AIM | 0 | gated on MAT L3–4 |

*L: 0 none · 1 exposed · 2 with help · 3 alone · 4 fluent · 5 can teach*

## CAPABILITY GATES
- **G1 — it moves** (sensor + actuator, filmed) → doorway is the servo build (blocked on hardware)
- **G2 — it thinks** (sense → filter → decide → act) → Sept
- **G3 — it's designed** (CAD'd body) → Oct · **G4 — autonomous** → Sem 4

## BUILDS
- ✅ **Traffic light** (24 Jul) — 3 LEDs, `setState`, filmed, pushed + README.
- ✅ **Button-LED** (23 Jul, ELE) — `day2_button.ino`, internal pull-up, filmed + pushed.
- 🐙 **PRJ SIGNATURE — Octopus tendon-driven soft gripper.** Locked. Tendon-driven (NOT pneumatic). Phases:
  1. **Drive one servo** (PWM, Servo lib, off-board power + common ground) ← next, blocked on servos
  2. Single tendon-driven finger (servo pulls fishing-line tendon)
  3. Multi-finger underactuated gripper
  4. Closed-loop force/contact sensing
  Drip cadence, fabrication targeted at Onam. ⚠️ Servos can't run off Arduino 5V (500–700mA stall) → need off-board 5V + common ground.
- 🔴 **Robowars** — design team. **Freeze 15 Sept.** 8-week CAD ramp committed, fabrication at Onam. Still need: weight class · ruleset · budget · fab access.
- ⭐ **NORTH STAR — SRL extra arms.** Gated until G2. Ladder (from roadmap): EMG front-end → prosthetic hand → single-joint exo.

## DEBT (fix in PRG Day 1)
- [ ] `day3_matrix_advanced.py` — two `__main__` blocks, second clobbers first
- [ ] README stub · [ ] zero tests · [ ] restructure repo by track, delete `Phase 0/`

## ⚠️ PATTERNS — WATCH
- **Voltage/current = flow-of-substance** intuition. Resurfaced 3× (12/13/24 Jul), resolved by end of ELE Day 2. Not dead till it stops returning.
- **Answers the expected question, not the one asked.** Cost marks on both ELE day-tests. New: `delay()` is *blocking*, not just a timer; missed "bounce."
- **Comfort-track gravitation** (did ELE ×2 before touching new tracks) + **over-scoping** (Day 3 broke at 5.5 hr). Force switches; cap scope.

## RECENT LOGS (rolling — full history in Drive)
- **24 Jul · PRJ** — Traffic light built + filmed + README. Voltage/current confusion closed. Conf 4.
- **23 Jul · ELE** — Day 2 button-LED built + filmed. Test 3/5 (delay-as-blocking, bounce weak). Level 2.5.
- **13 Jul · ELE** — Day 1 first artifact, `day1_blink.ino` pushed + filmed.