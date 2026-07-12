# MASTER PROGRESS TRACKER

**Owner:** V · **Started:** June 2026 · **Last updated:** 12 July 2026

---

## THE GOALS

1. **Master's** at a top international university.
2. **High-paying robotics / software engineering role.** Timeline flexible — not required at graduation.
3. **Broad engineering growth.** Genuine competence across electrical, mechanical, and software. Refine ambitions as understanding deepens.
4. **Prove it.** Every phase ships something showable. Setup budget expands only against visible output.

**Spine:** Robotics software + the math underneath it.
**Around the spine:** electrical, mechanical, AI.
**Rule:** breadth is earned after depth. T-shaped, never flat.

---

## THE RULES

| Rule | Value |
|---|---|
| Daily floor | **20 minutes. Non-negotiable.** |
| Daily ceiling | **3 hours.** Over-scoping is what broke Day 3. |
| Topic rotation | User's choice — Claude forces a switch on over-indexing. |
| Session end | Every session ends with a SESSION LOG, pasted here. |
| Artifact rule | **No day completes without a tangible, showable output.** |
| Learning model | DIAGNOSE → ROUTE → BRIDGE → INTEGRATE |
| Tone | Strict mentor. Blunt correction. No sugarcoating. |

---

## SEMESTER 3 — KEY DATES

| Event | Date |
|---|---|
| Semester started | 22 Jun 2026 |
| **Midterms begin** | **13 Aug 2026** |
| Onam break (build window) | 25–30 Aug 2026 |
| Last teaching day | 23 Oct 2026 |
| End sems begin | 29 Oct 2026 |
| Attendance floor | 75% |

**Free ride:** 23MAT222 Probability & Complex Variables = the probability track, taught and graded. Attend it.
**Zero support:** No electrical, no programming course this semester. ELE + PRG are 100% self-driven.
**The play:** 23MEE282 Design Thinking (0-0-3-1, Wed 3-hr block) → make the robot the graded project.

---

## LEVEL SCALE

| L | Meaning |
|---|---|
| 0 | Not started |
| 1 | Exposed — watched/read, no output |
| 2 | Can do it with help |
| 3 | Can do it alone, slowly |
| 4 | Fluent — can build with it |
| 5 | Can teach it / defend it in an interview |

---

## TRACK STATUS

### MAT — Mathematics
**Level: 2.5** · *Furthest-along track. Over-indexing risk lives here.*

✅ MIT 18.06 L1–5 · vector ops from scratch · matrix ops from scratch · 2D rotation matrices · Gaussian elimination · determinant · matrix inverse (Gauss-Jordan)

**Next:** Eigenvalues & eigenvectors — 3B1B ch. 1–7, 18.06 L14, hand derivation.
**Open challenge (unanswered):** kinematic singularities and the pseudo-inverse.
**Probability:** now covered by 23MAT222 coursework. Attend. Translate to robotics.

---

### ELE — Electrical & Electronics
**Level: 1.5** · *🔥 STARTED 12 July 2026. Three weeks of avoidance broken.*

| Done | |
|---|---|
| ✅ | Diagnostic — 2 real misconceptions surfaced and corrected |
| ✅ | Voltage / current / resistance (water-tank model) |
| ✅ | LED as a diode; why current-limiting resistors exist |
| ✅ | Resistor calculation by hand (200Ω → 220Ω standard) |
| ✅ | Microcontroller vs. CPU; digital pins; `setup()` / `loop()`; GND |
| ❌ | **Nothing built. Day 1 incomplete.** |

**Misconceptions found:** voltage defined as "difference in resistance" · open vs. short circuit confused.
**Live wobble:** potential vs. flow. *Ground is a reference point, not a drain.* Fix this.

**Next:** Wiring plan → external LED blink → **film it** → push `day1_blink.ino` to `ELE/`.

---

### DSA — Data Structures & Algorithms
**Level: 0** · *Queued. Not begun.*

**Next:** Big O properly. Then Two Sum. Then into Blind 75.
**Why:** every serious company filters on it — and graph search (A\*, Dijkstra) *is* motion planning.

---

### MEC — Mechanical & Dynamics
**Level: 2** · *Coursework-driven. Your edge over CS grads.*

**Sem 3 feeds this directly:** Mechanics of Solids, Thermodynamics, Metallurgy, Manufacturing, Machine Drawing.
**Next:** Stop treating these as courses to pass. Connect Newton–Euler to robot dynamics explicitly.

---

### PRG — Programming & Software Engineering
**Level: 2** · *Real work here — the from-scratch matrix library is genuine.*

**Have:** Python, VS Code, Git/GitHub, `Robotics-Journey` repo live with `Phase 0`.
**Next:** Clean code, testing, project structure. C++ much later. **No MATLAB. Ever.**

---

### AIM — AI / Machine Learning
**Level: 0** · *Correctly not started. The math comes first.*

**Gate:** Do not begin until MAT hits L3–4.
**Note:** the Kalman filter is gated on **ELE**, not on math. It needs a real noisy sensor to be worth anything.

---

### PRJ — Build Projects
**Level: 0** · ⚠️ **STILL THE CRITICAL GAP.**

Nothing physical exists. **This is the track that unlocks the setup budget.** Parents fund proof, not promises.
**Next:** The LED. Small. Ugly. Working. **Filmed.**

---

## HONEST ASSESSMENT — 12 JULY 2026

**What changed:** ELE moved off zero. That matters more than everything in the four planning sessions combined.

**What didn't:** PRJ is still zero. ELE Day 1 is *incomplete* — theory landed, nothing was built. The Arduino is out of the box and still not blinking.

**The diagnostic vindicated itself.** Voltage was wrong. Self-report would have missed it entirely. Keep answering honestly, especially when it stings.

**The standing risk:** comprehension mistaken for progress. Confidence 4 on a zero-artifact day is that exact error, in miniature.

**Verdict:** finish ELE Day 1. Not "learn more." **Build.**

---

## SESSION LOG

*Newest at top.*

### 2026-07-12 · ELE
- Diagnostic (5Q): voltage misconception ("difference in resistance") + open/short confusion — both corrected
- Topic 1: V/I/R via water-tank analogy; LED as diode; current-limiting resistor
- Topic 1 quiz: 3/4. Resistor calc correct (200Ω → 220Ω). Wobble: potential vs. flow / ground
- Topic 2: microcontroller vs. computer; digital pins as code-controlled switches; `setup()`/`loop()`; GND as return path
- **Artifact: NONE — build not started, Day 1 incomplete**
- **Next:** wiring plan → external LED blink → film → push `day1_blink.ino` to `ELE/`
- Confidence: 4

### 2026-07-11 · GEN
- Goals restructured (job timeline flexible, breadth added, artifact rule)
- Chat architecture + codes locked; tracker initialized
- Sem 3 calendar ingested — started 22 Jun, midterms 13 Aug
- Found: 23MAT222 = probability track, free · zero ELE/PRG coursework this sem
- Play identified: 23MEE282 Design Thinking as robot vehicle
- Teaching model replaced: DIAGNOSE → ROUTE → BRIDGE → INTEGRATE
- **Artifact:** PROGRESS.md
- **Next:** ELE Day 1
