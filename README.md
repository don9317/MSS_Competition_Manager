# MSS League Scheduler v11.0 — Production Candidate

Version 11.0 is the first full workflow/operations candidate for the League Management module.

## Major v11.0 improvements
- Director Dashboard with League Setup Wizard, Validation Center, Division Status, League Progress, Publishing Status, Scheduling Rules summary, and Recent Activity.
- A dedicated **League Scheduling Rules** section under Resources with on/off controls for:
  - Allow Back-to-Back Games
  - Play Every Pool Opponent Before Repeats
  - Avoid Immediate Rematches
  - Protect Shared Coaches
  - Honor Team Schedule Requests
  - Keep Teams in Assigned Pool (core rule)
- Game length, additional minimum-rest slots, and maximum teams per pool remain configurable.
- Always-enforced protections prevent self-games, double-booked teams, and double-booked courts.
- Division Assignments are generated automatically from registered divisions and show Court Group, recurring start/end time, and Games per Team per Week.
- If only one Court Group exists, unassigned divisions automatically use it.
- Per-division games/week settings are used by schedule generation and progress calculations.
- Schedule Management keeps division/pool, week, status, and court filters, publishing controls, change history, undo/restore, and historical corrections.
- Team Detail modal Close button uses delegated event handling; Escape and background-click closing are also supported.
- Complete Demo League remains included with schedules, sample scores, standings, and published portal data.

## Included files
- `index.html` — application
- `START_HERE.html` — local launcher
- `logo.png`
- `sample-teams.csv`
- `sample-scores.csv`
- `sample-league-setup.json`
- `README.md`

For GitHub Pages, publish `index.html` as the site entry point. `START_HERE.html` is only a convenience launcher for downloaded/local packages.
