# sample notes

## log rotation

Use logrotate with a weekly cadence and keep 4 archives.
Compress rotated files with gzip to save disk.

## backups

Nightly rsync to the backup volume, verified with checksums weekly.
