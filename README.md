# MSS 3v3 League Scheduler v9.2

## Fixes
- A Court Group named **All Courts** now dynamically includes every current playing surface.
- Existing saved groups named All Courts are automatically converted to dynamic groups.
- Adding or removing a playing surface automatically changes what All Courts contains.
- Capacity calculations and schedule generation now use the resolved current surfaces in the group.
- Added a defensive check preventing a team from being scheduled against itself.

## Important
For custom court groups, the scheduler still uses only the surfaces manually selected when that group was created.
