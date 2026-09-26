# MSS League Scheduler v11.11.83 — New League Setup + Editable Courts

- Adds Start New League. Recommended path keeps playing surfaces, normal availability, Court Groups and general scheduling-rule defaults while clearing league-specific data.
- Clears registrations, divisions/pools, games/results, published schedule, schedule changes, date-specific court exceptions, league name and season dates.
- Completely Blank option still available through the confirmation flow.
- Adds Edit Name beside every Playing Surface. Court internal IDs remain unchanged.
- Renaming a court updates working and published game court-name text while preserving Court Groups and court exceptions by ID.
- Duplicate court names are blocked. Published-schedule renames require confirmation.
- Retains v82.1 multi-court availability, publishing controls, Court Calendar fix and Court/Game print fix.
- No opponent-generation, Re-Optimize, court optimizer or Audit logic changes.


## v11.11.86.21 generator fix
Replaces recursive matchup backtracking with a deterministic bounded constructor to prevent combinatorial browser freezes. Storage schema and league setup data are unchanged.


## v11.11.86.21 generator fix
Fixes a scope regression in v86.4 where the deterministic matchup planner attempted to call a generation-stage UI function that was local to generateSchedule(). The resulting ReferenceError was caught as a generation warning, causing zero games to be saved while the final audit could misleadingly report success. v86.5 passes the stage callback explicitly and preserves the detailed generation summary. No storage schema or league setup fields were changed.


## v11.11.86.21
Post-generation responsiveness hotfix: schedule generation no longer calls full renderAll() after saving/auto-repair. Only the Schedule surface is refreshed during generation; other tabs render when opened. Storage schema unchanged.


## v11.11.86.21
Schedule All Approved / Ready Divisions now runs sequentially, yields to the browser between divisions, shows progress, and avoids full-app renderAll() calls during the batch.


## v11.11.86.21
Schedule All now passes each division scope directly into the proven generator instead of changing/re-reading the Schedule dropdown. A re-entry guard prevents accidental recursive Schedule All calls.


## v11.11.86.21 — Atomic Nightly Minimum
Built directly from the known-running v86.17 baseline. Absolute Rule #1: every active team must receive at least the configured nightly minimum (3) on every playing date. Failed bounded placements no longer save partial games. A final independent commit gate verifies every target team/date before state.games is changed; any 2-game result blocks the generated scope from being saved. The fully relaxed final placement tier receives a larger bounded search window so soft opponent/rematch/rest preferences yield before the hard minimum. Sequential Schedule All/browser-yield architecture from v86.17 is retained.


## v11.11.86.21 — Scope + Production Preflight Fix
- Fixes Generate Schedule when Schedule / Display Scope is Entire League. The browser MouseEvent is no longer mistaken for a scope override.
- Generate button now explicitly invokes generateSchedule() without forwarding the click event.
- Production Preflight excludes draft/unapproved divisions and filters aggregate capacity blockers to approved production divisions.
- Retains v86.20 atomic hard-minimum commit gate: no generated scope is saved if any active team has fewer than 3 games on a playing date.
