# MSS Competition Manager v11.11.87.8.4 — Parking Lot Audit Completeness

- Adds a scoped **Unassigned games — Parking Lot** warning row to the Schedule & Rules Audit.
- Lists parked matchups, division, date and original slot in an expandable detail section.
- The top-level audit status distinguishes a rule-valid schedule from a complete, ready-to-publish schedule.
- Entire League audits include all parked games; selected-scope audits filter by division/pool; future-date audits filter by selected dates.
- Existing publishing protection remains: publishing is blocked if any game is parked.
- This release does not change game placement, scheduling algorithms, or stored league data.
- Test in Sandbox with one parked game, then restore and repeat audit. Confirm live data separately.
