# Manual regression checklist (Sandbox only)

1. Open Schedule Management and verify Recent Scheduling Changes displays.
2. Move game A into an eligible empty slot, preview/apply, and confirm history records old/new slots.
3. Undo and confirm A returns to original slot. Redo and confirm A returns to new slot.
4. Move A again and move B. Undo twice, redo twice. Check both game slots and audit.
5. Swap two games, undo, redo; both games must change together.
6. After undo, apply a different move. Redo should no longer be available.
7. Change an involved game through another control. Undo must refuse to overwrite the later edit.
8. Park and restore a game; confirm both actions appear in history but cannot be undone using visual undo.
9. Return to live league. Verify no sandbox changes or undo controls carry over.
10. Run Schedule & Rules Audit and read-only safety checks. Confirm parked-game publication block remains.
