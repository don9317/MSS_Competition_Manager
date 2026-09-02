# MSS League Scheduler v11.11.3

Hotfix release focused only on startup/storage reliability.

## What changed
- The application renders a usable clean league **before** attempting to restore IndexedDB data.
- Saved-league restoration now has a timeout so a stalled IndexedDB request cannot leave the screen blank.
- v11.11.3 uses a fresh IndexedDB database name to avoid a potentially stuck prior test database.
- If saved data cannot be restored, the scheduler stays open in recovery mode instead of hanging.
- Added **Reset Saved League** in the top navigation to clear this version's saved IndexedDB data and reload cleanly.
- Existing scheduling, division approval, capacity, fairness, audit, and league-rule features were not intentionally changed.

## Recommended test
1. Open `START_HERE.html`, then launch the scheduler.
2. Confirm the Director Dashboard appears immediately.
3. Confirm the status at upper right changes from `Loading saved league…` to either `Ready — new league`, `League loaded`, or a visible recovery warning.
4. Re-import the 97-team MSS registration CSV if this fresh storage version starts clean.
5. Continue the JV Boys / division-approval tests.
