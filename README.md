# MSS 3v3 League Scheduler v9.5

## Registration import correction
- CSV import now defaults to **Replace all existing registrations**.
- Append mode remains available when intentionally adding late teams.
- Added **Clear Registrations & Schedule** on the Registrations tab.
- Clearing registrations preserves league settings, courts and court groups.
- Duplicate displayed team names are identified immediately.
- Schedule generation is blocked while duplicate team names remain.
- Loading sample teams replaces prior registration data instead of appending.

This fixes the situation where a unique-name CSV was imported on top of the old sample list, leaving both old and new team records in the browser.
