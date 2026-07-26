# MSS 3v3 League Scheduler v9

## Primary 3v3 workflow
1. Import registrations.
2. Divisions are created automatically from grade, gender and level.
3. Oversized divisions split into balanced pools.
4. The Director reviews and approves the Division & Pool Big Board.
5. Add independently schedulable playing surfaces such as Court 1 West and Court 1 East.
6. Create reusable Court Groups from those surfaces.
7. Assign each division to a repeating Sunday time window and Court Group.
8. Set Games per Team per Week, such as three games every Sunday.
9. Generate and review the weekly schedule.

## New in v9
- Half-court playing surfaces
- Reusable Court Groups
- Division-specific Sunday time windows
- Division-to-Court-Group assignments
- Same division returns to the same surfaces each week
- Games per team per week setting
- Calculated total season games
- Weekly schedule generation
- Week number in schedule, score entry and CSV export
- Validation when a division lacks a court group or time window
- Capacity comparison based on assigned division windows

## Testing
Use the included `sample-teams.csv`. Add surfaces such as:
- Court 1 West
- Court 1 East
- Court 2 West
- Court 2 East

Then create groups and assign each division a Sunday window.
