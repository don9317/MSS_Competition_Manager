# MSS 3v3 League Scheduler v9.3

## Matchup corrections
- A team can never be scheduled against itself.
- Duplicate team IDs in saved pool data are automatically removed.
- Every team is prioritized to play all other teams in its pool before opponents repeat.
- Immediate rematches are strongly avoided.
- Opponent history is carried across all Sundays in the season.
- Regenerating a selected pool replaces that pool's old schedule while preserving other pools.

## Testing note
After installing v9.3, select the affected pool and click Generate Schedule again. The previously generated self-games and unfair matchup sequence will be replaced.
