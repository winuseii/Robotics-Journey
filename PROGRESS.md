# MASTER PROGRESS TRACKER

**Owner:** V · **Started:** June 2026 · **Last updated:** 13 July 2026

> **13 July 2026 — FIRST ARTIFACT SHIPPED.** The LED blinks. `day1_blink.ino` is in the repo. Video exists.
> Three weeks of avoidance, ended. Everything before this was preparation. This is the first thing that is *real*.

---

## THE GOALS

1. **Master's** at a top international university.
2. **High-paying robotics / software engineering role.** Timeline flexible — not required at graduation.
3. **Broad engineering growth.** Genuine competence across electrical, mechanical, and software.
4. **Prove it.** Every phase ships something showable. Setup budget expands only against visible output.

**Spine:** Robotics software + the math underneath it.
**Rule:** breadth is earned after depth. T-shaped, never flat.

---

## THE RULES

| Rule | Value |
|---|---|
| Daily floor | **20 minutes. Non-negotiable.** |
| Daily ceiling | **3 hours.** |
| Topic rotation | User's choice — Claude forces a switch on over-indexing. |
| Session end | Topic chats produce a SESSION LOG. **GEN does not.** |
| GEN's job | Tracker + decisions. No learning happens here. |
| Artifact rule | **No day completes without a tangible output.** |
| Learning model | DIAGNOSE → ROUTE → BRIDGE → INTEGRATE |
| Tone | Strict mentor. Blunt correction. No sugarcoating. |

---

## SEMESTER 3 — KEY DATES

| Event | Date |
|---|---|
| Semester started | 22 Jun 2026 |
| **Fusion 360 needed by** | **End of July** |
| **Midterms begin** | **13 Aug 2026** |
| Onam break (build window) | 25–30 Aug 2026 |
| Last teaching day | 23 Oct 2026 |
| End sems begin | 29 Oct 2026 |
| Attendance floor | 75% |

**Free ride:** 23MAT222 Probability & Complex Variables = the probability track, taught and graded.
**Zero support:** No electrical, no programming course this semester. ELE + PRG are 100% self-driven.
**Reinforcement:** 23MEE205 Machine Drawing ↔ Fusion 360. Same skill, two directions.

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

### ELE — Electrical & Electronics
**Level: 2.5** · *🔥 Day 1 COMPLETE. Artifact shipped. Fastest-moving track.*

| Done | |
|---|---|
| ✅ | Diagnostic — 2 misconceptions surfaced and killed |
| ✅ | V / I / R; LED as diode; current-limiting resistor |
| ✅ | Resistor calc by hand (200Ω → 220Ω standard) |
| ✅ | Microcontroller vs CPU; digital pins; `setup()`/`loop()`; GND |
| ✅ | CH340 clone detected, COM5 |
| ✅ | Wiring plan, polarity, breadboard row logic |
| ✅ | **Built + uploaded + verified `day1_blink.ino`** (pin 13 → 220Ω → LED → GND) |
| ✅ | **Filmed.** |

**Day test:** 3.5/5. Voltage + ground now solid.
**Misconceptions killed:** voltage as "difference in resistance" · open vs short · "resistor must come before LED."
**⚠️ Named weakness — the Day 2 patch:** physical-layer mechanisms.
- Diode directionality (precise, not hand-wavy)
- **Current kills, not voltage**
- The code → transistor → voltage chain (what *actually* happens when `digitalWrite(HIGH)` runs)

**Root pattern to break:** reaching for *flow-of-substance* intuitions. Current is a **rate set by the whole loop**, not stuff travelling through it. This error has now appeared three times in different costumes.

**Next:** ELE Day 2 — `digitalRead` + first input.

---

### MAT — Mathematics
**Level: 2.5** · *Was the over-indexed track. Now correctly parked.*

✅ MIT 18.06 L1–5 · vectors, matrices, rotations from scratch · Gaussian elimination · determinant · inverse (Gauss-Jordan)

**Next:** Eigenvalues & eigenvectors — 3B1B ch. 1–7, 18.06 L14, hand derivation.
**Open challenge (still unanswered):** kinematic singularities and the pseudo-inverse.
**Probability:** now handled by 23MAT222 coursework. Attend. Translate.

---

### MEC — Mechanical & Dynamics
**Level: 2** · *⏰ URGENT: Fusion 360 needed by end of July.*

**Sem 3 feeds this:** Mechanics of Solids, Thermodynamics, Metallurgy, Manufacturing, Machine Drawing.
**Next:** `Fusion 360 Fundamentals (MEC)`. Scope hard — sketch → constrain → extrude → fillet → joint → assemble → export STL. **Nothing else.**
**License:** verify student status via SheerID with Amrita email. Downloaded ≠ licensed.

---

### PRG — Programming & Software Engineering
**Level: 2**

**Have:** Python, VS Code, Git/GitHub, `Robotics-Journey` repo — now with `Phase 0` **and** `ELE/`.
**Next:** Clean code, testing, project structure. C++ much later. **No MATLAB. Ever.**

---

### DSA — Data Structures & Algorithms
**Level: 0** · *Unlocked. Queued.*

**Next:** Big O — derived properly, using your own `mat_multiply` as the specimen. Then Two Sum. Then Blind 75.
**Why:** every serious company filters on it — and graph search (A\*, Dijkstra) *is* motion planning.

---

### AIM — AI / Machine Learning
**Level: 0** · *Correctly not started.*

**Gate:** MAT at L3–4.
**Kalman filter is gated on ELE, not math.** It needs a real noisy sensor to mean anything. That road runs through the breadboard.

---

### PRJ — Build Projects
**Level: 1** · *No longer zero. Proof-of-life exists.*

**Shipped:** the blinking LED. Trivial as engineering. **Decisive as evidence.**

**🔴 LIVE PROJECT — ACM × ASME**
- First-ever collaboration between the two clubs. **1 of 5 on the ASME team.**
- ASME owns **electrical + CAD.** ACM owns **software.**
- Signed up for *both* electrical and design.
- **Brief: NOT YET RECEIVED.** Chasing it 14 July.
- Hard requirement: basic Fusion 360 by end of July. Likely 3D printing.
- Team interest is thin — **risk of collapse. Treat as bonus, not plan.**
- **Role to claim:** the ELE ↔ software bridge. Nobody else on ASME has the maths *and* the code *and* the hardware.

---

## HONEST ASSESSMENT — 13 JULY 2026

**The thing that changed:** you closed a loop. You said you'd finish Day 1, and you finished it. That is the first hard evidence against your own claim that you can't stay consistent. Everything else in this file is downstream of that.

**The thing that hasn't changed:** one LED is not a robot. The next test isn't whether you can start — it's whether you can do it again on a day when it isn't exciting.

**Standing risk:** the ACM×ASME project is a *bonus*, not the plan. Thin interest means it can die. Your own build depends on nobody and cannot be cancelled. Keep it primary.

**Verdict:** ELE is the momentum track. **Do not abandon it now.** Ride it.

---

## SESSION LOG

*Topic chats only. Newest at top.*

### 2026-07-13 · ELE — ⭐ FIRST ARTIFACT
- CH340 clone confirmed on COM5
- Wiring plan, polarity (anode/cathode), breadboard row logic
- **Misconception killed:** "resistor must come before LED" — series current is identical everywhere in the loop
- **Built external blink:** pin 13 → 220Ω → LED → GND
- Typed, uploaded, verified `day1_blink.ino` (500ms)
- Day test: 3.5/5 — voltage/ground solid; weak on physical-layer mechanisms
- **Artifact: `day1_blink.ino` pushed to `ELE/` + video** ✅
- **Next:** ELE Day 2 (`digitalRead` + first input) · or DSA Day 1 · or PRJ Day 1
- Confidence: 4

### 2026-07-12 · ELE
- Diagnostic: voltage misconception + open/short confusion — corrected
- V/I/R, LED as diode, current-limiting resistor. Quiz 3/4
- Microcontroller vs computer, digital pins, `setup()`/`loop()`, GND
- **Artifact: NONE — Day 1 incomplete**
- Confidence: 4
