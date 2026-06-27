# Robotics Journey — Progress Dossier
*Living handoff context, carried across chat sessions and tools.*

## Who I am / the goal
- BTech Mechanical Engineering, Amrita University. Currently Semester 3, just started.
- Target profile: **Robotics Software Engineer with AI specialization** — the intersection
  of Software Engineer (DSA, algorithms, systems thinking) × Mechanical Engineer (dynamics,
  kinematics, hardware intuition) × AI Engineer (ML/DL/RL, perception).
- **Bio-robotics is the dream, not a side interest.** I want to explore building life-like
  animal robots — bio-inspired locomotion, soft robotics, neuromechanics-informed control.
  I don't yet know how to get from "mechanical engineering student" to "person who builds
  these things," and that path needs to be made concrete, not just aspirational.
- Milestones that matter:
  - Strong at robotics before 3rd year.
  - A meaningful internship by Semester 5.
  - Admission to an Ivy League-tier or equivalent (MIT / Stanford / ETH Zurich level) master's
    program — ideally in a biorobotics/biomechatronics lab (MIT Biomechatronics, CMU
    Biorobotics, ETH Zurich Sensory-Motor Systems Lab are named reference labs).
  - At least one workshop paper / technical report (ICRA or IROS student track, ~4 pages)
    by end of Phase 7. Not a full paper sooner — that timeline was explicitly ruled out as
    unrealistic.

## Signature project
**Bio-inspired locomotion robot** — mimics biological gait (insect, quadruped, or human
walking dynamics). Runs across all 7 curriculum phases as the throughline. Every technique
covered (state estimation, control, RL, SLAM) should get a biomechanics interpretation
drawn out explicitly, since that's the actual target field.

## Reference documents
1. Robotics curriculum v5.1 — custom 7-phase curriculum, AI-heavy by design. The spine;
   extend it, don't replace it.
2. Amrita BTech Mechanical Engineering syllabus — interleaved with the robotics track
   (e.g. Differential Equations ↔ Phase 0 ODEs, Engineering Mechanics ↔ Phase 2 dynamics,
   Intro to Python ↔ Phase 0 coding, Basic EEE ↔ Phase 1 circuits/Arduino).

## Parallel tracks
- **DSA** — 30 min/day, LeetCode, Blind 75 first. Progression: arrays/strings/recursion →
  linked lists/stacks/queues/trees (Month 3–4) → graphs (Month 4–5, overlaps with motion
  planning: BFS/DFS/Dijkstra/A*) → DP/heaps (Month 5–7) → systems design (Month 7+).
- **Competitions (India-specific)** — e-Yantra, Robocon. A real competition result + a
  strong GitHub portfolio with quantitative results matters more right now than a rushed
  paper.

## Working format
- Progress tracked day by day. One day = one focused session (~1.5–2 hrs), not a marathon —
  Day 3 was originally scoped at 5.5 hrs and had to be restarted at 2 hrs. Retention drops
  sharply past hour 3.
- Quiz/test on prior material periodically and at random, not just on request.
- Be honest, no hype, no false promises.
- Ask clarifying questions whenever there's a gap in available time, prior knowledge, or
  preference — don't assume.
- Teach from scratch every time, assume no prior knowledge unless demonstrated.
- Don't hesitate to critique work or push back on ideas.
- All code commits to this repo, organized by phase folders, with a running README
  checklist per phase.

## Research/teaching scope — explicitly broadened
Don't limit teaching material to the uploaded curriculum doc or university OCW alone.
Pull from whatever sources actually teach this well — papers, lab websites, course notes
from other universities, technical blogs, textbooks, competition writeups — and say so
when citing something outside the original two source docs. Tools/skills/connectors in
the available roster can be used as needed without asking permission each time; if a
genuinely new skill would help, it can be built.

## Where things stand — Phase 0 (Foundations)
- **Day 1:** Environment setup. MIT OCW 18.06 (Strang) Lecture 1 — geometry of linear
  systems. `phase-0/day1_vectors.py`.
- **Day 2:** `day2_matrix_ops.py` (add, multiply, transpose, identity), `day2_rotation_ops.py`
  (2D rotation matrices, chained rotations, verified R·Rᵗ = I). Connected matrix exponentials
  to Sem-2 Diff Eq (dx/dt = Ax → later the Kalman filter's A matrix).
- **Day 3 (restarted, 2-hr version):** MIT 18.06 Lectures 4, 5, 14, 15. `day3_matrix_advanced.py`
  — Gaussian elimination, determinant (2×2/3×3), matrix inverse (verified A·A⁻¹ = I),
  eigenvalues via power iteration. PCA demo. 3Blue1Brown linear algebra series alongside.
  Big-O introduced informally (`mat_multiply` correctly identified as O(n³)).
- Phase 0 linear algebra is essentially complete as of Day 3.

## Next step
**Day 4**: probability/statistics — foundation for sensor fusion and SLAM, building toward
the Kalman filter (~Week 7). DSA parallel track starts from Day 4 onward. Bio-robotics
path-mapping (labs, prerequisites, how undergrads actually break in) needs its own
dedicated planning session, separate from the daily curriculum cadence.
