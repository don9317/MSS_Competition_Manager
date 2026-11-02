# MSS Competition Manager v11.11.87.7 — League Setup Navigation

## Changes
- Replaced the top-level Resources tab with **League Setup** and **Courts & Fields**.
- League Setup displays league dates, game duration, minimum/maximum games, configurable maximum waiting time, and scheduling rules.
- Courts & Fields displays physical courts, date-specific availability, court groups, division scheduling assignments, and advanced diagnostics.
- Redesigned the maximum waiting-time controls as a compact row and hides duration/enforcement controls when the league maximum is disabled.
- Existing legacy navigation links to `settings` still resolve to League Setup.
- The underlying scheduling, parking, sandbox, storage, and auditing engines are unchanged.

## Cautions
- This is a navigation/UI release. Team-specific schedule requests remain in Registrations.
- Some older optimizer routines still have separate waiting-time thresholds.
- Static JavaScript and archive checks passed; browser UI automation was blocked by the environment, so validate the navigation in the Scheduling Sandbox before relying on it.
- Back up league data before publishing.
