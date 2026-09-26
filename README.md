# MSS League Scheduler v11.11.83 — New League Setup + Editable Courts

- Adds Start New League. Recommended path keeps playing surfaces, normal availability, Court Groups and general scheduling-rule defaults while clearing league-specific data.
- Clears registrations, divisions/pools, games/results, published schedule, schedule changes, date-specific court exceptions, league name and season dates.
- Completely Blank option still available through the confirmation flow.
- Adds Edit Name beside every Playing Surface. Court internal IDs remain unchanged.
- Renaming a court updates working and published game court-name text while preserving Court Groups and court exceptions by ID.
- Duplicate court names are blocked. Published-schedule renames require confirmation.
- Retains v82.1 multi-court availability, publishing controls, Court Calendar fix and Court/Game print fix.
- No opponent-generation, Re-Optimize, court optimizer or Audit logic changes.


## v11.11.86.16 generator fix
Replaces recursive matchup backtracking with a deterministic bounded constructor to prevent combinatorial browser freezes. Storage schema and league setup data are unchanged.


## v11.11.86.16 generator fix
Fixes a scope regression in v86.4 where the deterministic matchup planner attempted to call a generation-stage UI function that was local to generateSchedule(). The resulting ReferenceError was caught as a generation warning, causing zero games to be saved while the final audit could misleadingly report success. v86.5 passes the stage callback explicitly and preserves the detailed generation summary. No storage schema or league setup fields were changed.


## v11.11.86.16
Post-generation responsiveness hotfix: schedule generation no longer calls full renderAll() after saving/auto-repair. Only the Schedule surface is refreshed during generation; other tabs render when opened. Storage schema unchanged.


## v11.11.86.16
Schedule All Approved / Ready Divisions now runs sequentially, yields to the browser between divisions, shows progress, and avoids full-app renderAll() calls during the batch.


## v11.11.86.16
Schedule All now passes each division scope directly into the proven generator instead of changing/re-reading the Schedule dropdown. A re-entry guard prevents accidental recursive Schedule All calls.


## v11.11.86.16
Hard-minimum guard: nightly minimum and calculated season minimum cannot be worsened by Re-Optimize; audit details now include Division / Pool / Team / Playing Date / actual-required. Partial placement shortages are explicitly production-blocking.


## v11.11.86.16
Capacity diagnostic build. Entire League production audit excludes Draft/unapproved divisions. Odd-team pools correctly allow legal 4th games when minimum=3 and maximum=4. Nightly-minimum failures now show game-events required, legal court/time slots, placed events, unused slots, and active constraints.


## v11.11.86.16
Hard-minimum completion pass. If preference-aware placement cannot complete the exact nightly matchup plan, a bounded final solver uses only immutable constraints (valid court/time, availability, no team/court double-booking). Soft coach/rest/opponent/rematch preferences may be relaxed to preserve the 3-game minimum; the configured maximum of 4 remains enforced by the matchup plan.


## v11.11.86.16
Draft/Preflight consistency fix. Production Preflight now evaluates approved production divisions only, matching Schedule All and Entire League Audit. Draft/unapproved divisions are explicitly reported as skipped rather than producing approval/team/resource/capacity blockers. v86.12 hard-minimum completion behavior is retained.


## v11.11.86.16
Production-scope runtime fix. Introduces one centralized isProductionDivision()/productionDivisionKeys() authority used by Production Preflight, Schedule All Ready Divisions, blocked-division reporting, and Entire League Audit. Draft/unapproved divisions are not production blockers. Preflight visibly identifies itself as `86.14 PREFLIGHT ENGINE` and reports production/skipped counts so browser/runtime mismatches can be detected immediately. Existing saved league data and v86.12 hard-minimum completion logic are unchanged.


## v11.11.86.16
Hard-minimum priority build. Shared-coach overlap is non-controlling for this league because each team is required to have an additional coach. Draft/unapproved divisions are defensively excluded from every Entire League audit target/team path. Three-team and other small pools may repeat opponents as necessary to satisfy the hard minimum of 3 games per playing date and calculated season minimum; configured maximum games per playing date remains hard. Court/time validity, no self-match, no team double-booking, no court double-booking, team availability, nightly minimum, season minimum, and configured maximum remain hard rules.

## v11.11.86.16 — Exact Guarantee Planner
- Replaces greedy nightly matchup construction with an exact degree-sequence planner.
- 3-team / minimum-3 / maximum-4 nights explicitly become 4-3-3 team game counts = 5 actual games.
- Hard nightly counts are placed before rest, rematch, and opponent-sequence preferences.
- Preflight capacity uses the generator's legal court universe rather than the misleading poolSlots-only count.
- Draft/unapproved production exclusion and shared-coach non-controlling behavior from 86.15 are retained.
