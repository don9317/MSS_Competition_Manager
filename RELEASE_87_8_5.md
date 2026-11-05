# Version 87.8.5 — Sandbox Audit Date Scope Fix

The Audit Entire League (Future Dates) button previously used the live future-date selector even inside the Sandbox, causing historical sandbox schedules and parked games to be omitted.

Sandbox audits now use dates present in sandbox scheduled AND parked games. Live audits still use the selected future-date scope. The parked-game warning remains scope-aware. No stored game records are changed by this release.

Tests: static JavaScript syntax and ZIP integrity. Verify in the browser with a parked historical game and then after restoration.
