# Check Duplicate File Skill

A skill for comparing files between two folders and copying unique files while avoiding duplicates.

## Installation

Install this skill by copying the `check_duplicate_file` folder to your skills directory, or use the packaged `.skill` file.

## What It Does

This skill helps you:
- Compare files between two directories by filename
- Copy unique files from a source folder to a destination folder
- Avoid overwriting existing files
- Get a clear report of what was copied and what was skipped

## Usage

When you need to merge folders or copy unique files, just ask:
- "Check for duplicate files between folder1 and folder2"
- "Copy unique files from downloads to my archive folder"
- "Merge these two directories without overwriting"

The skill will use the provided Python script to perform the comparison and copying operation.

## Script Usage

You can also run the script directly:

```bash
python scripts/check_duplicates.py <destination_folder> <source_folder>
```

Example:
```bash
python scripts/check_duplicates.py ./archive ./downloads
```

## Features

- Cross-platform compatibility (Windows, macOS, Linux)
- Preserves file metadata during copying
- Non-destructive (never overwrites existing files)
- Clear console output showing results
- Comparison based on filename only

## License

This skill is provided as-is for use with Claude.
