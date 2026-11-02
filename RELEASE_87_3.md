# Version 87.3 — Read-only schedule safety checks

Adds an optional director dashboard check for missing teams, duplicate game IDs, self-matchups, same-slot court/team conflicts, and missing game fields. It verifies no state mutation. The existing rules audit remains authoritative for scheduling constraints. No game movement, multi-user login, database migration, or optimizer changes.

Back up the approved league before deployment. Run the safety check and the existing Rules Audit. This is not a full automated regression suite.
