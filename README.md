# MSS League Scheduler v11.11.7

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
