# backuPi
A tool to automatically zip and backup files on a drive onto another drive.

Install via
```bash
python3 setup.py install
```

## MVP:
1. Trigger every 5 minutes if nothing is running to check
2. Exactly three drives plugged in
    1. Exactly one drive has exactly one "to-backup" folder
    2. Exactly one drive has exactly one "backups" folder
    3. Exactly one drive is the temp drive for creating the compressed file. This should be empty.
    3. Stop process and warn if above conditions don't match
3. Compress "to-backup" folder contents
    1. Create `hash` using last modified date time, size, number of files in total (maybe?)
    2. Named `yyyy/mm/dd/drivename/hash.zip` where `HHMM` is 24hr time for when backup began
    3. Compare against hash/file path
    3. If not existing, compress onto temp drive
4. Create folder and copy from temp drive to main
5. Notify

## Additional features:
1. Trigger when new drive is plugged in
2. Indicate status using LED
3. Copy to network drive connected to another RPi
4. Web app hosted on RPi as a visual interface