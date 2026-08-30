MSS League Scheduler v11.5

Major v11.5 improvement: direct MSS registration-export support.

- Automatically recognizes MSS registration CSVs using playerOrTeamName and name.
- Treats the MSS registration `name` field as the already-selected registration division.
- Creates each unique registration division automatically and places every team directly into it.
- Parses grade/gender/HS JV/HS Varsity metadata when possible for display and later matching.
- Preserves v11.2 Division Setup tools so the Director can rename, combine, split/reassign teams before approval.
- Adds a file preview before import showing format, registration count, and number of source divisions detected.
- Continues to support the standard Team Name / Coach / Gender / Grade / Skill / Request CSV format.
- Retains v11.1 season start/end dates, any-day-of-week scheduling, exception/off dates, court groups, division-specific time windows, games per playing date, rules, validation, schedule management, results, standings, and public portal.

Open START_HERE.html or index.html in a modern browser.


## v11.5 fixes
- Uses a fresh browser-storage key to avoid carrying oversized/stale data from earlier test builds.
- Replace import now clears prior divisions, published schedules, schedule history, and activity before loading the new registration file.
- Clear Registrations & Schedule now also clears the selected CSV filename and import preview.
- MSS import preview clearly says the file is ready to import; clicking Import CSV performs the actual load.


## v11.5 storage/resource fix
- Automatically removes older League Scheduler localStorage records that can consume the browser quota.
- Playing Surface and Exception / Off Date additions now retry after storage cleanup and show a clear message if the browser is still full.
