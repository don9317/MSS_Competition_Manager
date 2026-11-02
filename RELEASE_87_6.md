# MSS League Scheduler 11.11.87.6 — Configurable Waiting Time

- Added league-wide Maximum Team Waiting Time settings under Resources → League Setup: enable/disable, 15/30/45/60/75/90/120 minutes, strict or preferred. Defaults for prior leagues: 45 minutes, preferred.
- New setting is saved in the league state (including sandbox copy).
- Parking Lot is shared above all Admin tabs, including Court Calendar; its count and games remain synchronized.
- Parking Lot restoration checks newly created idle gaps against the configured threshold; strict blocks, preferred warns.
- Court compression waiting comparisons now use the league threshold instead of a hardcoded 45 minutes.

## Limitations

This release does not implement drag-and-drop or two-game swaps. Full schedule generation and all legacy diagnostics have not been refactored to honor the new maximum wait setting. Existing hard rules and historical special-purpose repair tools remain unchanged. Use the Scheduling Sandbox for testing.

## Test

1. In Sandbox, open Resources and set maximum wait to 15 minutes, Strict.
2. Try restoring a parked game into a slot that creates a longer idle gap; confirm it blocks.
3. Change to Preferred and confirm it warns.
4. Disable the limit and confirm the waiting-time block is removed.
5. Confirm the same Parking Lot is visible from Court Calendar and Schedule Management.
6. Run Read-only Safety Checks and Schedule Audit.
