# MSS League Scheduler 11.11.87.0 — Stabilization Baseline

This is a conservative UI organization release based on 86.13. The scheduling, optimization, audit, persistence, and backup JavaScript functions are preserved. No schedule data is embedded or modified by this ZIP.

## Changes
- Updated main title/header to 87.0.
- Removed the development BUILD CHECK banner and obsolete version-specific explanation from the main schedule view.
- Made Check Readiness, Generate, Audit, and Back Up the primary scheduling actions.
- Moved exports, restore, supplemental audits, and repair utilities into expandable **More scheduling tools**.
- Moved the 86.9/86.11/86.13 one-off November 1 actions and Simulation Test Lab access into expandable **Developer diagnostics**. Their underlying code is intentionally retained.
- Preserved Schedule Optimization Center, wait threshold selector, manual locks, and all existing tab panels.

## Scope / limitations
This is a stabilization *baseline*, not a certified commercial release. No underlying scheduling algorithms were rewritten or consolidated. It is still a local browser application; commercial multi-user data storage, permissions, backups, security review, and browser regression testing remain outstanding.

## Upgrade precautions
1. Export schedule backup from 86.13 and keep that ZIP unchanged.
2. Extract 87.0 to a **new** folder and open index.html.
3. Verify that your existing league data loads. If not, restore from your saved backup after confirming the restore scope.
4. Run the audit on a known test league, and confirm no schedule changes before publishing.
5. Avoid the historical league-specific actions under Developer diagnostics.

## Release checklist
- [x] HTML markup structural check (unique element IDs; referenced buttons retained)
- [x] JavaScript syntax check (Node.js --check)
- [x] ZIP integrity test
- [ ] Browser interaction test on Chrome/Edge
- [ ] 86.13 approved schedule import and full audit regression
- [ ] Generate / optimize / preview / apply / restore end-to-end regression
- [ ] Multi-user storage, security and production deployment validation
