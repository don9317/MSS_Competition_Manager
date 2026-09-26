# MSS League Scheduler v11.11.83 — New League Setup + Editable Courts

- Adds Start New League. Recommended path keeps playing surfaces, normal availability, Court Groups and general scheduling-rule defaults while clearing league-specific data.
- Clears registrations, divisions/pools, games/results, published schedule, schedule changes, date-specific court exceptions, league name and season dates.
- Completely Blank option still available through the confirmation flow.
- Adds Edit Name beside every Playing Surface. Court internal IDs remain unchanged.
- Renaming a court updates working and published game court-name text while preserving Court Groups and court exceptions by ID.
- Duplicate court names are blocked. Published-schedule renames require confirmation.
- Retains v82.1 multi-court availability, publishing controls, Court Calendar fix and Court/Game print fix.
- No opponent-generation, Re-Optimize, court optimizer or Audit logic changes.


## v11.11.86.11 generator fix
Replaces recursive matchup backtracking with a deterministic bounded constructor to prevent combinatorial browser freezes. Storage schema and league setup data are unchanged.


## v11.11.86.11 generator fix
Fixes a scope regression in v86.4 where the deterministic matchup planner attempted to call a generation-stage UI function that was local to generateSchedule(). The resulting ReferenceError was caught as a generation warning, causing zero games to be saved while the final audit could misleadingly report success. v86.5 passes the stage callback explicitly and preserves the detailed generation summary. No storage schema or league setup fields were changed.


## v11.11.86.11
Post-generation responsiveness hotfix: schedule generation no longer calls full renderAll() after saving/auto-repair. Only the Schedule surface is refreshed during generation; other tabs render when opened. Storage schema unchanged.


## v11.11.86.11
Schedule All Approved / Ready Divisions now runs sequentially, yields to the browser between divisions, shows progress, and avoids full-app renderAll() calls during the batch.


## v11.11.86.11
Schedule All now passes each division scope directly into the proven generator instead of changing/re-reading the Schedule dropdown. A re-entry guard prevents accidental recursive Schedule All calls.


## v11.11.86.11
Hard-minimum guard: nightly minimum and calculated season minimum cannot be worsened by Re-Optimize; audit details now include Division / Pool / Team / Playing Date / actual-required. Partial placement shortages are explicitly production-blocking.


## v11.11.86.11
Capacity diagnostic build. Entire League production audit excludes Draft/unapproved divisions. Odd-team pools correctly allow legal 4th games when minimum=3 and maximum=4. Nightly-minimum failures now show game-events required, legal court/time slots, placed events, unused slots, and active constraints.
