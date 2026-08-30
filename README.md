# MSS League Scheduler v11.10

Key scheduling refinement:
- Minimum Games / Team / Playing Date is now the primary hard rule.
- Calculated Season Minimum = minimum games per playing date × league playing dates.
- Maximum Games / Team / Playing Date permits controlled overflow (for example, 4 when the minimum is 3).
- Schedule generation includes a dedicated nightly-minimum repair pass before season-total repair.
- Schedule & Rules Audit FAILS when an available team receives fewer than its nightly minimum.
- Games above the minimum are allowed up to the maximum and appear as an audit warning rather than a failure.
- Existing IndexedDB autosave / Save Progress protection remains in place.

Typical 3v3 setup: 3 minimum games per date × 4 playing dates = 12-game season minimum, maximum 4 games per date.


## v11.10
- Adds Entire Division scheduling scope for multi-pool divisions.
- Pools are scheduled together while matchups remain inside their approved pools.
- Fair slot allocation rotates and balances early/middle/late opportunities across pools.
- Adds Time-Slot Fairness to the Schedule & Rules Audit.
- Improves feasibility explanations when Back-to-Back Games or rest rules prevent the nightly minimum.
