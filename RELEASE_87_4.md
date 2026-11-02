# v11.11.87.4 — Interactive Parking Lot (pilot)

- Parking Lot remains visible above the Schedule/Court Calendar/Management tabs.
- Schedule Management offers **Park** for future, unscored, unlocked games. Parked games retain their entire game record in IndexedDB, separate from the active game list.
- **Choose slot / Restore** prompts for date, 24-hour time, and exact court name. Checks overlapping court and team assignments, back-to-back restrictions, court availability, and division window. Restored games are marked unpublished and locked.
- Publishing is blocked while games remain parked. Parking and restoration create change-history entries.
- Does not yet support drag-and-drop, multi-game transactions, redo, or cloud user accounts.
- IMPORTANT: This is a pilot. Use a disposable test league or backup copy only; do not park any game from an approved production schedule. The full scheduling audit is still required after restoration.
- Static JavaScript syntax and archive integrity checked; browser interaction testing not completed.
