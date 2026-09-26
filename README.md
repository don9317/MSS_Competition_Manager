# MSS League Scheduler v11.11.86.33 — Within-Group Court Priority

Court optimization now gives the previous court assignment zero preference. Within each legal division/pool court group it uses physical order (1A, 1B, 2A, 2B, 3A, 3B...) after earliest session start and horizontal compression. A 3-team pool assigned to 2B + 3A should remain on 2B unless 2B is legally unavailable. Hard rules and protected audit rollback remain authoritative.


## v11.11.86.33
Adds a court-only compaction pass before time rebuilding. It preserves game times and matchups while moving games to the lowest-ranked legal court in the division/pool court group. Pure court-rank improvements are accepted and reported in Optimization Status.


## v11.11.86.34
Resource-change repair: Optimize This Date now detects games whose saved court/time is no longer legal under current court groups, availability, or date exceptions. Invalid placements are mandatory repairs; valid manual locks remain protected, while an invalid locked placement may be moved. Final success requires zero invalid current-resource placements on the selected date.
