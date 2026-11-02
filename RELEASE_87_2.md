# MSS League Scheduler v11.11.87.2 — Build Identification & Safety Checks

Based on 87.1. This is a deliberately conservative release.

## Added
- Header **Build 87.2 · Details** button, with read-only build version, unique build ID, actual loaded URL, and IndexedDB storage origin.
- **Copy Build Info** action for support/debugging. Browser clipboard permissions may require a manual copy fallback.
- `verify_release.py`: reproducible static smoke tests for JavaScript syntax, HTML ID uniqueness, core functions, storage constants, sticky Parking Lot, and release labels.

## Unchanged
- Scheduler, optimizer, audit, game data, league storage schema, backup/restore, and 87.1 Parking Lot preview.
- Parking Lot is still a **nonfunctional preview**, not drag/drop or transactional scheduling.
- No cloud accounts, server-enforced permissions, or multi-location score synchronization are included.

## Important
- The GitHub Pages website does not update automatically when this ZIP is downloaded. Publish the included files to the correct repository and wait for deployment.
- Back up the approved league before testing. Avoid running two scheduler tabs against the same browser origin.
- Automated **static** checks are not a substitute for full browser-based regression tests or live league acceptance testing.

## Validation
Run `python verify_release.py` from the extracted folder (requires Node.js for syntax checking).
