MSS Competition Manager v11.11.86.27 — SESSION-START ANCHORED COURT COMPRESSION

Court optimizer-only correction based on v11.11.86.26.

Changes:
- Each division/pool is optimized from its earliest legal configured session time.
- A 4:30 PM session starts at 4:30 PM when legal; a 7:00 PM session starts at 7:00 PM when legal.
- Within each time, available/legal courts are filled horizontally before advancing to later start times.
- Removed the late-start optimization candidate so the optimizer cannot intentionally slide a division later.
- Matchups are unchanged by Court + Time optimization.
- Manually locked games remain locked.
- Protected Audit rollback remains in place.
- Hard nightly minimum / atomic commit logic is unchanged.

Recommended current workflow:
1. Open this version using START_HERE.html or index.html.
2. Do NOT Generate Schedule or Re-Optimize Schedule.
3. Select 2026-09-27 and click Optimize Selected Date.
4. Review Court Calendar for 9/27.
5. Run Audit Entire League before publishing.
