# v11.11.87.8.1 — Visual Move dropdown hotfix

Fixes an undefined `hhmm` function call in the Visual Game Move & Swap option builder. The exception prevented the Start Time and Court selectors from being populated. The new code uses a local formatter. Also preserves selected game across option refresh.

No schedule-generation or persistent-data schema changes. Continue testing in Scheduling Sandbox. Browser automation was blocked by environment network restrictions; JavaScript syntax and ZIP integrity verified.
