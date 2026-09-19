# Decision log

## Two-letter prefixes, not Uniclass codes
Readability at a glance beat schedule mapping. Classification stays a
parameter.

## Type catalogues above eight types
File size and load time, not principle. Below eight, embedded types are fine.

## No model files in this repository
Git stores whole copies of binaries. A 240 MB central model would make the
repository unusable within a month, and the model already has a versioning
system of its own.

## Schedule checks run before issue, not after
A check that runs after issue is a report. A check that runs before issue is a
gate. The script is the same; the timing is the whole value.