# MSS League Scheduler v11.11.21

Regression / reliability release.

Key fixes:
- Restored resource action functions accidentally omitted in v11.11.5 (playing surfaces, court groups, off dates, division scheduling assignments).
- Added visible success/failure confirmations for resource actions and Save Progress.
- Hardened critical control bindings so one failed button cannot disable unrelated buttons.
- Tightened "Ready to Schedule" so a division must be approved and have a valid saved court group, surfaces, and time window.
- Preserves IndexedDB storage, division-by-division approval, multi-pool scheduling, rules audit, and board navigation.

QA performed:
- JavaScript syntax check.
- Static regression check for critical resource functions and control IDs.
- ZIP contents verification.


## v11.11.20
Court Group setup now requires an explicit Division selection when divisions exist. Creating the group automatically assigns it to that division in Division Scheduling, and saved Court Groups show their current division assignments.

## v11.11.20
- Synchronizes a division's recurring time window to the common availability of its assigned Court Group.
- Shows Court availability, Division window, and Effective scheduling window together in Division Scheduling.
- Manual start/end edits remain allowed and are treated as an intentional custom window.
- Strengthens Play Every Pool Opponent Before Repeats: a repeat matchup is blocked until both teams have faced every other pool opponent.
- Preserves IndexedDB save/recovery and all v11.11.10 functionality.


## v11.11.20 opponent-rotation fix
- Opponent rotation is now checked chronologically at the actual candidate game date/time.
- Nightly-minimum and season-repair passes can no longer use future games to justify an earlier repeat.
- The Play Every Pool Opponent Before Repeats audit should now agree with schedule generation.


## v11.11.20 changes
- Odd-team nightly balancing: when a pool has an odd number of teams, the nightly-minimum repair can give one team the legal 4th game so every team still reaches the minimum (for example 4-3-3-3-3 in a five-team pool).
- Extra games rotate toward teams that have received fewer prior overflow nights.
- New Court Calendar tab: view a selected playing date as a time-by-court grid, filter by division/pool, click a game to edit it, and visually flag court/time or team double-booking conflicts.


## v11.11.20
- Added an iterative post-generation repair engine. After the normal generator satisfies nightly and season game counts, it performs same-pool/same-date matchup swaps that preserve each team's games-per-night totals while reducing shared-coach conflicts, immediate rematches, and repeats before all pool opponents have been faced.
- The repair loop accepts only changes that improve the combined hard-rule score and re-runs the Rules Audit afterward.
- Odd-pool overflow games that are mathematically required (for example 5 teams with a 3-game nightly minimum) are now treated as expected balancing rather than a generic warning when they remain within the configured maximum.


## v11.11.20 changes
- Structural round-robin-first protection: post-generation repair cannot create new early repeats or immediate rematches.
- Court Group ↔ Division Scheduling assignment is synchronized both directions for more reliable persistence.
- Division Scheduling adds Court Use modes: Preferred, Exclusive, and Open.
- Preferred divisions use protected courts first; when capacity is short, Generate Schedule searches compatible open facility slots and asks the Director before using overflow courts.
- Schedule Audit distinguishes Director-approved overflow court usage from actual court-assignment violations.


## v11.11.20
- Added custom pool names from the Division & Pool Big Board.
- Use Rename on any pool to set names such as Gold, Silver, American, or National.
- Pool names are display labels only; internal Pool A/B identifiers remain stable so schedules and saved data are not broken.
- Custom names flow through schedule scope, Court Calendar, Schedule Management, standings, and team schedule displays.


## v11.11.20
- Pool naming is now always visible inside each expanded pool card.
- Enter a custom Pool Name and click Save Name.
- Pool naming is disabled while a division is approved/locked; unlock the division to rename its pools.
- Internal Pool A/Pool B identifiers remain unchanged so schedules and saved data remain stable.


## v11.11.20 additions
- Pool-level Court Group overrides for multi-pool divisions (for example HS Boys Gold and Blue can use different protected court groups while remaining one division).
- Pool overrides can also carry their own recurring start/end time and court-use mode.
- Entire Division scheduling respects each pool's assigned Court Group.
- New Export Division Season and Export Division Week CSV controls on the Schedule page.


## v11.11.20
- Multi-pool divisions can now select **Use Pool Assignments** as the parent/default Court Group.
- If every pool has an explicit Court Group and valid time window, the division is considered Ready without a parent Court Group.
- Existing v11.11.18 pool assignments are auto-detected and migrated to pool-assignment mode.
- Dashboard readiness and validation now recognize valid pool-level resource assignments.
- Court Group usage displays include pool-specific assignments.


### v11.11.20
- Pool-level Court Group assignments automatically synchronize stale/inherited pool time windows to the Court Group availability.
- Invalid pool windows show a Use Court Hours recovery action.
- Added Schedule All Ready Divisions so blocked pools do not prevent other approved/ready divisions from being scheduled.
- Entire League preflight now identifies blocked divisions instead of leaving the Director to hunt for the mismatch.

## v11.11.21 — Physical courts + multiple availability windows
- Playing Surfaces now represent a physical court once, with one or more availability windows. Adding the same court name again adds another time window instead of creating a duplicate court.
- Existing duplicate court entries are merged automatically on load and Court Group references are preserved.
- Playing Surfaces are sorted naturally (Court 1, Court 2, … Court 10) and each court shows its time blocks together.
- Court Groups now display their common availability windows.
- Division/pool time synchronization uses the assigned Court Group. When multiple time blocks exist, HS divisions default to the later block and elementary/middle divisions to the earlier block; intentional custom restrictions are preserved.
- Scheduling and capacity calculations now generate slots from all availability windows on each physical court.

QA performed for v11.11.21:
- JavaScript syntax check with Node.
- Static check that the multi-window court functions, synchronization functions, and resource controls are present.
- ZIP integrity verification.
