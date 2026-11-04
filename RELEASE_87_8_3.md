# MSS Competition Manager 87.8.3 — Startup & Sandbox Navigation Hotfix

- Separates saved-data read failures from UI rendering failures; no longer reports “Opened clean — saved data unavailable” when the data loaded but a view failed.
- Defensive view/tab initialization: keeps the Admin navigation available and falls back safely if a requested panel is missing.
- Normal Schedule Management, Court Calendar, and Schedule tabs remain the interface in Sandbox mode; the yellow banner confirms the test workspace.
- Preserves sandbox and live storage record separation.
- Does not modify scheduling algorithms or existing game records.

Testing: JavaScript syntax and ZIP integrity checked. Interactive browser testing unavailable in this runtime. Back up league data and confirm both live and sandbox records before further editing.
