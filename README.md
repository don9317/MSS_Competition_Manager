# MSS League Scheduler v11.11.86.33 — Within-Group Court Priority

Court optimization now gives the previous court assignment zero preference. Within each legal division/pool court group it uses physical order (1A, 1B, 2A, 2B, 3A, 3B...) after earliest session start and horizontal compression. A 3-team pool assigned to 2B + 3A should remain on 2B unless 2B is legally unavailable. Hard rules and protected audit rollback remain authoritative.


## v11.11.86.33
Adds a court-only compaction pass before time rebuilding. It preserves game times and matchups while moving games to the lowest-ranked legal court in the division/pool court group. Pure court-rank improvements are accepted and reported in Optimization Status.


## v11.11.86.34
Resource-change repair: Optimize This Date now detects games whose saved court/time is no longer legal under current court groups, availability, or date exceptions. Invalid placements are mandatory repairs; valid manual locks remain protected, while an invalid locked placement may be moved. Final success requires zero invalid current-resource placements on the selected date.


## v11.11.86.35
Multi-pass late-session compaction. Optimize This Date now repeats division/pool compaction sweeps (up to four), so games stranded late by temporary cross-block court occupancy are reconsidered after earlier blocks move. Stops when a full sweep accepts no further improvement. Opponents remain unchanged and protected audit rules remain enforced.


## v11.11.86.36
Print/export-only change. Court/Game # numbering restarts at Game 1 for each court at 7:00 PM (High School session). Printed court sheets show Elementary and High School section labels but no time column. CSV includes Session and Game # but no game time. Scheduler and optimizer logic are unchanged from v86.35.
\n\n## v11.11.86.37\nFixes Director Dashboard Edit League Rules navigation so it opens and scrolls to the League Setup/Game Length control. Adds alternating latest-game-first optimizer cleanup sweeps to reconsider games stranded late after earlier legal slots open. Matchups/opponents are unchanged by court/time optimization.\n

## v11.11.86.38
Optimizer fix: adds a game-level left-shift cleanup after block optimization. Latest games are reconsidered one at a time and moved to the earliest legal earlier court/time while preserving opponents, court legality, team spacing/conflicts, schedule requests, and protected audit rules. This targets stranded late-session games after large empty gaps. Includes the v86.37 League Rules navigation fix.


## v11.11.86.39
Management/UI safety update. Director Dashboard now reports actual Divisions / Pools separately (for example 7 / 8) and division scheduling counts use true divisions rather than pool rows. Start New League now requires warning + typed NEW LEAGUE + final confirmation; Erase All League Data retains warning + typed ERASE ALL protection. Court Groups are listed alphabetically and include Edit Courts to change group surface membership without regenerating schedules. Scheduler/optimizer behavior remains v86.38.


## v86.41
- Added Schedule Management export: **Export CSV / By Time**.
- Sort order: Date → Time → Court.
- Columns: Date, Time, Court, Division, Pool, Team A, Team B.
- Uses the current Schedule Management filters.
- No scheduler, optimizer, pool, court, audit, or league logic changes.


## v11.11.86.41
- Game Length changes now re-grid existing working schedule start times to the new interval while preserving dates, courts, matchups, scores, and game records.
- Fixes Court Calendar retaining stale 12-minute times after returning Game Length to 10 minutes.
- No scheduler, optimizer, pool, court-assignment, or matchup-generation changes.


## v11.11.86.43
- Clean package of v86.41 game-length regrid fix.
- No additional functional changes.
- Retains Export CSV / By Time from v86.40 and all prior scheduling/management behavior.


v86.43: One-time startup repair converts stale off-grid 12-minute game timestamps to the current Game Length grid while preserving matchups, courts, dates, game records/numbers, and scores.
