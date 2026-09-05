# MSS League Scheduler v11.11.11

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


## v11.11.11
Court Group setup now requires an explicit Division selection when divisions exist. Creating the group automatically assigns it to that division in Division Scheduling, and saved Court Groups show their current division assignments.

## v11.11.11
- Synchronizes a division's recurring time window to the common availability of its assigned Court Group.
- Shows Court availability, Division window, and Effective scheduling window together in Division Scheduling.
- Manual start/end edits remain allowed and are treated as an intentional custom window.
- Strengthens Play Every Pool Opponent Before Repeats: a repeat matchup is blocked until both teams have faced every other pool opponent.
- Preserves IndexedDB save/recovery and all v11.11.10 functionality.
