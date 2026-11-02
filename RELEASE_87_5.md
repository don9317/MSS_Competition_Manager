# MSS League Scheduler 87.5 — Scheduling Sandbox pilot

- Dedicated browser IndexedDB record `sandbox-87-5` (live record remains `current`).
- Create sandbox from saved live league via read-only copy; return to live using URL query parameter.
- Sandbox treats the first scheduled date as a virtual past boundary for date-based parking eligibility, without modifying real dates.
- Explicit Prepare Old Games button clears scores/completion/locks ONLY in sandbox copy to permit Parking Lot testing.
- Reset Sandbox copies live league again; no changes written to live record.
- Sandbox publishing and destructive database erase disabled.
- This is a local/browser prototype, not a secure server-isolated environment. Do not use sandbox for live operations.
- Test with backup and confirm live league unchanged after returning.
