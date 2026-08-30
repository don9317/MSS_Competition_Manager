# MSS League Scheduler v11.6.2

Version 11.6 replaces the League Scheduler's primary browser storage with IndexedDB and adds visible save-progress protection.

## v11.6.2 storage and progress protection
- League data is now stored in IndexedDB rather than localStorage, removing the small localStorage quota that blocked larger real-world imports.
- Automatic saves occur after league changes.
- A visible save indicator in the header shows Changes Pending, Saving Progress, League Saved, or Save Failed.
- The Resources page now has an explicit **Save Progress** button for a manual checkpoint.
- Export Setup remains available as a portable JSON backup.
- Reset Everything deletes the saved IndexedDB league record for this scheduler.
- No League Scheduler data is written to localStorage in v11.6.2.

## Existing v11 features retained
- Direct MSS registration-export import, including existing registration divisions.
- Director-editable Division Setup with combine, rename, and manual team reassignment.
- League start/end dates, any combination of playing days, and exception/off dates.
- Playing surfaces and court groups.
- Division-specific court group, recurring start/end times, and games per team per playing date.
- League Scheduling Rules with on/off policy toggles.
- Director Dashboard, validation center, schedule generation and management, results, standings, Coach Tools, and League Portal.

Open `START_HERE.html` or `index.html` in a modern browser. For maximum persistence reliability, keep using the same browser and the same extracted folder/location for the scheduler during testing.
