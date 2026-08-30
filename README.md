# MSS League Scheduler v11.7

Version 11.7 adds flexible season-game guarantees and an automatic Schedule & Rules Audit.

## New in v11.7
- Season Games Guaranteed per team (default 12)
- Preferred Games per Team per Playing Date (default 3)
- Maximum Games per Team per Playing Date (default 4)
- Per-division overrides for all three values
- Scheduler can vary a team's games by date when availability or scheduling requests require it, while prioritizing the season guarantee
- Catch-up logic increases a team's daily target (up to the configured maximum) when games are owed
- Automatic audit runs after schedule generation
- Audit Selected Scope and Audit Entire League buttons
- Audit checks: season guarantee, max games/date, self-games, team/court double-booking, division time windows, approved court groups, schedule requests, shared-coach conflicts, immediate rematches, all opponents before repeats, and rest/back-to-back rules
- Preferred games/date is treated as a warning rather than a hard failure when uneven distribution is necessary
- Publishing is blocked when the full-league audit has failed hard rules
- IndexedDB autosave and Save Progress remain in place

## Recommended workflow
1. League Setup
2. Registrations
3. Division Setup
4. Divisions & Pools
5. Resources
6. Division Scheduling
7. League Rules
8. Generate Schedule
9. Review Schedule & Rules Audit
10. Resolve hard-rule failures
11. Publish

Open `START_HERE.html` for the launcher or `index.html` directly.
