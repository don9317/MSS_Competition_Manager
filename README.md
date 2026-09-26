# MSS League Scheduler v11.11.83 — New League Setup + Editable Courts

- Adds Start New League. Recommended path keeps playing surfaces, normal availability, Court Groups and general scheduling-rule defaults while clearing league-specific data.
- Clears registrations, divisions/pools, games/results, published schedule, schedule changes, date-specific court exceptions, league name and season dates.
- Completely Blank option still available through the confirmation flow.
- Adds Edit Name beside every Playing Surface. Court internal IDs remain unchanged.
- Renaming a court updates working and published game court-name text while preserving Court Groups and court exceptions by ID.
- Duplicate court names are blocked. Published-schedule renames require confirmation.
- Retains v82.1 multi-court availability, publishing controls, Court Calendar fix and Court/Game print fix.
- No opponent-generation, Re-Optimize, court optimizer or Audit logic changes.


## v11.11.86.25 generator fix
Replaces recursive matchup backtracking with a deterministic bounded constructor to prevent combinatorial browser freezes. Storage schema and league setup data are unchanged.


## v11.11.86.25 generator fix
Fixes a scope regression in v86.4 where the deterministic matchup planner attempted to call a generation-stage UI function that was local to generateSchedule(). The resulting ReferenceError was caught as a generation warning, causing zero games to be saved while the final audit could misleadingly report success. v86.5 passes the stage callback explicitly and preserves the detailed generation summary. No storage schema or league setup fields were changed.


## v11.11.86.25
Post-generation responsiveness hotfix: schedule generation no longer calls full renderAll() after saving/auto-repair. Only the Schedule surface is refreshed during generation; other tabs render when opened. Storage schema unchanged.


## v11.11.86.25
Schedule All Approved / Ready Divisions now runs sequentially, yields to the browser between divisions, shows progress, and avoids full-app renderAll() calls during the batch.


## v11.11.86.25
Schedule All now passes each division scope directly into the proven generator instead of changing/re-reading the Schedule dropdown. A re-entry guard prevents accidental recursive Schedule All calls.


## v11.11.86.25 — Atomic Nightly Minimum
Built directly from the known-running v86.17 baseline. Absolute Rule #1: every active team must receive at least the configured nightly minimum (3) on every playing date. Failed bounded placements no longer save partial games. A final independent commit gate verifies every target team/date before state.games is changed; any 2-game result blocks the generated scope from being saved. The fully relaxed final placement tier receives a larger bounded search window so soft opponent/rematch/rest preferences yield before the hard minimum. Sequential Schedule All/browser-yield architecture from v86.17 is retained.


## v11.11.86.25 — Scope + Production Preflight Fix
- Fixes Generate Schedule when Schedule / Display Scope is Entire League. The browser MouseEvent is no longer mistaken for a scope override.
- Generate button now explicitly invokes generateSchedule() without forwarding the click event.
- Production Preflight excludes draft/unapproved divisions and filters aggregate capacity blockers to approved production divisions.
- Retains v86.20 atomic hard-minimum commit gate: no generated scope is saved if any active team has fewer than 3 games on a playing date.


## v11.11.86.25 — Slot Diagnostic Fix
- Production Preflight now shows detailed Slot Diagnostics for every capacity blocker: Court Group, member surfaces, each court's hours and date exception, configured pool window, effective window, court mode, overflow status, base/total slots, and required games.
- Slot generation now uses the same effective court-group/pool time intersection used by validation, preventing a stale/inherited pool window from validating while yielding zero slots.
- Retains v86.21 Entire League click/scope correction and production-only preflight.
- Retains v86.20 atomic hard-minimum commit gate: every active team must have at least 3 games per playing date before generated scope can be saved.


## v11.11.86.25 — Opponent Matrix Repair
- Even-sized pools now build matchup demand from deterministic circle-method round-robin rounds. This guarantees each team sees every available opponent before a repeat, until the pool exhausts its unique opponents.
- This directly targets 10-team Varsity Boys, 14-team Varsity Girls, 14-team 5/6 Boys, 16-team HS JV, and other even pools.
- Odd pools retain the exact nightly-degree constructor, including the required 4-3-3 pattern for a 3-team pool.
- Re-Optimize general opponent repair budget increased and remains browser-yielding/bounded.
- Final targeted repair now gives All Opponents Before Repeats higher scoring priority than immediate-rematch cleanup while preserving all structural hard rules and the original opponent-balance ceiling.
- Retains v86.22 slot diagnostics/effective-window correction and v86.20 atomic 3-games-per-night commit gate.


## v11.11.86.25 — Rotation Priority Repair
- Corrects the visible browser title/header to v11.11.86.25.
- Treats All Opponents Before Repeats as higher priority than the soft Opponent Balance warning during final repair. A hard rotation improvement may temporarily use up to four additional balance warnings; structural rules and nightly/season minimums remain protected.
- Expands bounded targeted repair from 1,800 to 6,000 candidates and from 6 to 12 passes (45-second cap).
- Exempts 3-team pools from All Opponents Before Repeats and Opponent Balance audit noise because a 3-game nightly minimum mathematically requires repeats.
- Retains atomic 3-games-per-team-per-date commit protection, preflight, court/time rules, and all prior safety checks.


## v11.11.86.25 — Odd-Pool Coverage-First
- Week-one delivery build: preserves all v86.24 hard schedule protections and court/time behavior.
- Fresh-generation odd/general pool pairing now treats a repeat as the highest matchup penalty while either team still has an unplayed active opponent available in the nightly degree sequence.
- Designed specifically to improve 9-team pools such as 7/8 Boys without changing the hard 3-games-per-team-per-date requirement.
- Even-pool round-robin matrix logic from v86.24 is retained.
- Three-team unavoidable-repeat audit exemption is retained.
