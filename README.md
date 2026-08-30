# MSS League Scheduler v11.1 — Production Candidate

Version 11.1 restores and clarifies the fundamental season and division-scheduling setup required before schedule generation.

## Major v11.1 improvements
- **League Start Date** and **League End Date** are now explicit fields.
- **League Playing Days** supports any combination of Monday through Sunday using a compact checkbox dropdown.
- **Exception / Off Dates** can be added individually with an optional reason such as a holiday, facility event, or closure.
- The scheduler calculates the actual playable dates between the start/end dates after applying selected playing days and off dates.
- The Director Dashboard and Validation Center verify season dates, selected playing days, exception dates, playable dates, and division scheduling readiness.
- **Division Assignments** is renamed **Division Scheduling** and clearly captures, for every division:
  - Court Group
  - Recurring Start Time
  - Recurring End Time
  - Games per Team per Playing Date
- Division scheduling settings are enforced by schedule generation and capacity calculations.
- Schedule screens now refer to **Playing Date #** rather than Week so leagues can operate on any day or multiple days per week.
- League Scheduling Rules from v11.0 remain intact, including back-to-back games, opponent repeats, immediate rematches, shared-coach protection, team schedule requests, game length, and minimum rest.
- v11.1 uses a new local-storage key while migrating prior v11/v10 test data when possible.

## Included files
- `index.html` — application
- `START_HERE.html` — local launcher
- `logo.png`
- `sample-teams.csv`
- `sample-scores.csv`
- `sample-league-setup.json`
- `README.md`

For GitHub Pages, publish `index.html` as the site entry point. `START_HERE.html` is only a convenience launcher for downloaded/local packages.
