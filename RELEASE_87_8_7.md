# MSS Competition Manager v11.11.87.8.7 — Change History & Safer Undo/Redo

- Adds a Recent Scheduling Changes panel to Schedule Management showing up to 12 visual moves, swaps, parking, and restoration entries with before/after slots.
- Replaces single visual undo with an in-session multi-step undo stack and redo stack for previewed visual moves/swaps.
- Undo/redo checks that all involved games still match the expected snapshots and blocks changes if they do not.
- Switching between live and sandbox clears in-session undo/redo stacks. Undo/redo remains sandbox-only.
- Parking and restoration are visible in history but not eligible for automatic undo/redo.
- No changes to scheduling generation or existing saved games.

Testing: JS syntax, archive integrity, and source-level regression assertions passed. Browser smoke test was blocked by the runtime. Test the full flow in Sandbox before relying on it.
