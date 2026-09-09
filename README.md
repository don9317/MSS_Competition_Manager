# MSS League Scheduler v11.11.36

## v11.11.36 — retain partial schedules and audit unmet guarantees

This build keeps the bounded, browser-responsive guaranteed-game placer from v11.11.32, but restores the earlier league-director workflow: if one pool/date cannot place every guaranteed game, the best valid partial schedule is retained and generation continues through the remaining dates/divisions. The schedule is saved and displayed, and Audit Entire League identifies every team/date that falls below the 3-games-per-date or calculated season minimum.

Generation warnings now identify the exact division/pool/date, games placed vs. planned, and the bounded-placement reason. A failure in one pool/date no longer discards the entire league schedule.

## v11.11.36 — responsive guaranteed-game placement
- Replaces the recursive guaranteed-game DFS with bounded, one-game-at-a-time greedy placement.
- Yields to the browser every couple of game placements so Chrome stays responsive.
- Uses up to 24 short placement attempts with varied slot ordering instead of combinatorial backtracking.
- Stops a difficult pool/date after a 12-second safe limit and reports how many guaranteed games were placeable.
- Commits a pool/date only when all guaranteed games fit, preserving the 3-games-per-playing-date contract.


## v11.11.36 stability changes
- Generate Schedule now stops after the initial schedule is placed, saved, and rendered.
- Post-generation cleanup is no longer automatic; use the new **Optimize Schedule** button only when desired.
- Optimization is bounded and optional so it cannot prevent a generated schedule from appearing.
- Divisions using **Use Pool Assignments** no longer display or use parent recurring times. The parent time is shown as **Controlled by Pool Assignments**.
- Legacy parent 6:00 PM–8:00 PM values are cleared when pool-assignment mode is active.
- Pool override time fields no longer fall back to a hidden 6:00 PM–8:00 PM default.


## v11.11.36 — Court Group assignment consistency

- Court Group assignment now uses the actual Division Scheduling / Pool Court Override records as the single source of truth.
- Old `primaryDivisionId` metadata can no longer silently overwrite or contradict the current assignment.
- The Court Group assignment control now supports both a Division Default and individual pool assignments (for example HS Varsity Boys — Gold / Blue).
- `Current use` is calculated from the same live assignment records as scheduling, so the dropdown and Current use cannot disagree.
- Moving a division or pool to a different Court Group updates the previous group immediately on re-render.
- Startup migration clears stale legacy assignment metadata without guessing assignments from Court Group names.

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

## v11.11.23 — Physical courts + multiple availability windows
- Playing Surfaces now represent a physical court once, with one or more availability windows. Adding the same court name again adds another time window instead of creating a duplicate court.
- Existing duplicate court entries are merged automatically on load and Court Group references are preserved.
- Playing Surfaces are sorted naturally (Court 1, Court 2, … Court 10) and each court shows its time blocks together.
- Court Groups now display their common availability windows.
- Division/pool time synchronization uses the assigned Court Group. When multiple time blocks exist, HS divisions default to the later block and elementary/middle divisions to the earlier block; intentional custom restrictions are preserved.
- Scheduling and capacity calculations now generate slots from all availability windows on each physical court.

QA performed for v11.11.23:
- JavaScript syntax check with Node.
- Static check that the multi-window court functions, synchronization functions, and resource controls are present.
- ZIP integrity verification.


## v11.11.23
- Removes the hidden 6:00–8:00 division default for new divisions.
- Re-synchronizes saved division windows from their assigned Court Groups when the stored time has no usable court overlap.
- Court Groups may contain surfaces with different availability windows; scheduling uses each physical court only during its own available hours.
- HS divisions prefer the later available block; elementary/middle divisions prefer the earlier block.
- Improves overlap diagnostics so stale time defaults do not masquerade as missing assignments.


## v11.11.27 — Bounded overflow scheduling / performance hotfix
- Reworks approved overflow-court scheduling so the generator does not search every compatible court/time combination in the facility.
- Builds a small, ranked overflow plan per pool/date, using primary courts first and only enough extra slots to cover the expected shortage plus a limited safety buffer.
- Caps nightly repair loops, season-repair loops, and post-generation swap repairs so the browser returns a result instead of running indefinitely.
- Existing overflow approval behavior remains: the Director must approve use of additional courts before they are considered.
- Capacity, audit, Court Calendar, pool-specific court groups, and Division Week/Season exports remain available.

QA performed for v11.11.27:
- JavaScript extracted from the standalone HTML and syntax-checked with Node.
- Static verification of bounded overflow planning and loop caps.
- ZIP integrity verification.


## v11.11.27 stability change
Alternate/overflow-court approval is now a separate saved step. Approving alternate courts does not continue into schedule generation. Click Generate Schedule again after approval. A visible scheduling-stage indicator was also added to help isolate any future long-running stage.


## v11.11.27 scheduling-engine stability
- Builds one league-wide overflow reservation plan before matchup generation.
- Prevents multiple divisions from assuming the same alternate court/time slot is available.
- Generates divisions/pools in browser-friendly chunks and yields between targets so Chrome remains responsive.
- Keeps alternate-court approval separate from generation.
- Displays the active division/pool during generation and performs cleanup only after initial placement.


## v11.11.27 stability change
Game placement now yields to the browser inside each date, matchup, court-search, nightly-repair, and season-repair loop. Each division/pool has a 45-second safe ceiling, cleanup is bounded/cooperative, and the full audit is deferred until the generated schedule has rendered.


## v11.11.36 guarantee-first scheduling
- Rebuilt from the stable v11.11.29 generation flow.
- Matchups are planned before courts/times using round-robin rotation.
- Minimum games per playing date and calculated season minimum are hard guarantees.
- Immediate rematches are structurally avoided by round order, while every opponent is completed before the rotation repeats.
- Court/time placement commits a playing date only if every guaranteed matchup for that date can be placed.
- A failed placement stops safely and does not save a partial schedule.

## v11.11.36
- Replaces the date-level greedy placer with a bounded asynchronous constraint solver.
- Uses most-constrained-game-first search to protect the 3-games-per-playing-date guarantee.
- Yields frequently to the browser to preserve the anti-freeze behavior from v11.11.32/33.
- Tries strict rules first, then controlled fallback tiers only if needed; any relaxation is reported for Audit review.
- Keeps the best partial schedule only if all bounded solver tiers fail.


## v11.11.36
- Plans exactly the nightly minimum game count, adding only the single parity game mathematically required for an odd team-game total.
- Rotates the odd-pool extra game across teams and dates.
- Prefers least-played opponents while building the matchup plan, reducing repeats before all opponents are faced.
- Removes the whole-round overscheduling behavior from v11.11.34.
- Director Dashboard now shows Games Scheduled, Minimum Required, and Extra Games as separate metrics.

## v11.11.36
- Keeps the successful exact 3-games-per-playing-date planner from v11.11.35.
- Makes opponent rotation structural: a team cannot repeat an opponent until it has faced every other pool opponent, except when mathematically unavoidable in very small pools.
- Adds hard chronological immediate-rematch protection during court/time placement.
- Leaves the stable bounded/asynchronous court solver and capacity logic intact.
- No changes to the weekly minimum, season minimum, or overflow approval architecture.
