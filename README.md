# MSS 3v3 League Scheduler v10.3

A self-contained browser-based league scheduling and management prototype for My Sport Space.

## New in v10.3

- Added **Undo** to the latest applicable schedule-history entry.
- Older entries offer **Restore This Version** when later changes exist.
- Undo and restore actions create a new audit-history record; history is never deleted.
- Past, completed, or scored games open in **Historical Correction** mode rather than ordinary rescheduling mode.
- Historical games cannot be moved to today or a future date.
- Historical corrections require a reason.
- Teams cannot be changed while a score is attached to a game.
- Existing score corrections require a reason and are recorded in Schedule Change History.
- A game with both scores entered is automatically marked Completed.
- Published reversals become unpublished changes and must be published again.

## Included files

- `index.html` — application
- `START_HERE.html` — local launcher
- `sample-teams.csv` — sample registration data
- `sample-scores.csv` — sample score data
- `sample-league-setup.json` — sample configured league
- `logo.png` — MSS logo

## Local use

Unzip the package and open `START_HERE.html` or `index.html` in a modern browser. For GitHub Pages, publish `index.html` as the repository landing page.
