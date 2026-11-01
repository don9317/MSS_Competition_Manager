# MSS League Scheduler v11.11.87.1 — Diagnostics & Commercial UX Preparation

Based on validated 87.0. **No scheduling engine, optimization, audit, or persistence logic changed.**

- Moved Scheduling Inputs and Odd-Pool Opponent Pattern diagnostics into one collapsible Advanced Diagnostics panel in Resources; kept existing element IDs and refresh functions.
- Removed stale diagnostic version headings and November 1-only instructional text.
- Added a sticky, collapsible Game Parking Lot **visibility preview** at the top of the director workspace. This is not yet a functioning parking/drag-and-drop tool; it does not change games.
- Added a commercial multi-user access requirements note on Director Dashboard. This offline app has no secure authentication or live multi-location database; do not treat the note as implemented access control.
- Preserved all existing scheduling and audit controls, backup/restore, and historical compatibility functions.

## Release validation
- JavaScript parse: checked with node --check
- Duplicate HTML IDs: checked
- ZIP integrity: checked
- Browser interactive regression: **not yet performed**
- Approved 86.13/87.0 schedule remains the reference; never overwrite your backup.

## Next engineering priorities
1. Automated regression tests for new schedule generation, audit, optimize/preview/apply, restore, and manual locks.
2. Transactional game parking lot with drag/drop, undo/redo, audit before commit, and unscheduled-game publish blocker.
3. Backend identity, invitation flows, per-organization/event/location permissions, concurrency-safe score entry, audit logs and database backups.
