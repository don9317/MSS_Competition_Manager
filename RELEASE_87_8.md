# v11.11.87.8 — Visual Move & Swap Safety Pilot

- Clarifies the sandbox visual move/swap controls.
- Swaps now explicitly exchange the two games’ original slots rather than treating the chosen empty-slot controls as a swap target.
- Adds Undo Last Visual Change, which reverses both games in a swap together, provided neither has changed since.
- Retains live-league protection, previews, audit history, Parking Lot, and league settings.

## Test
Use Scheduling Sandbox only. Prepare historical games for testing, preview a move, apply, undo; then preview a swap, apply, undo. Run safety checks and scheduling audit.

## Limitations
No drag-and-drop, no persistent undo across page reloads, and no shared multi-user database. Full browser regression testing remains necessary.
