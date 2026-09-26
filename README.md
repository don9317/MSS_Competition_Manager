# MSS League Scheduler v11.11.86.29 — Block-Local Session Compression

Court optimizer correction:
- Optimize This Date remains on Court Calendar and uses the visible date.
- Each division/pool is evaluated against its own current time/court layout, so useful moves are not rejected merely because another division still occupies an old start time.
- Each division/pool is anchored to its earliest legal configured session time (for this league, 4:30 PM or 7:00 PM) when legally possible.
- Legal courts are filled horizontally at a time before advancing.
- Matchups are unchanged; manual locks are preserved.
- Protected schedule audit and final whole-date rollback gate remain in place.

Do not Generate Schedule to test this fix. On Court Calendar choose 2026-09-27 and click Optimize This Date.
