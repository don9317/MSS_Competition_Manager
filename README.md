# MSS League Scheduler v11.11.86.32 — Within-Group Court Priority

Court optimization now gives the previous court assignment zero preference. Within each legal division/pool court group it uses physical order (1A, 1B, 2A, 2B, 3A, 3B...) after earliest session start and horizontal compression. A 3-team pool assigned to 2B + 3A should remain on 2B unless 2B is legally unavailable. Hard rules and protected audit rollback remain authoritative.
