# How to apply these standards

1. Name the family before you model anything. Renaming later is cheap in the
   file system and expensive in the model.
2. Author parameters before geometry, so the geometry has something to attach
   to.
3. Run `scripts/check_names.py` against an exported schedule before every
   issue. It is faster than reading the schedule.
4. Anything that cannot comply gets an entry in the exceptions list, not a
   quiet workaround.
