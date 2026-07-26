# MSS 3v3 League Scheduler v9.1

## Fixes and additions
- Added a 15-minute game-length option.
- The Schedule / Display Scope dropdown now controls what is generated.
- Selecting one pool validates and schedules only that pool's division.
- Other divisions no longer need court groups before a selected pool can be scheduled.
- Existing schedules for other pools are retained when one pool is regenerated.
- Existing games are considered when checking court, team and shared-coach conflicts.
- Selecting “All divisions and pools” still validates and regenerates the complete league.

## Required setup for a selected pool
The selected pool's division still needs:
- A valid Sunday start/end time
- An assigned Court Group
- At least one playing surface in that Court Group
