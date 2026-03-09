---
name: check-duplicate-file
description: Check for duplicate files between two folders and copy unique files from one folder to another. Use this skill when users want to compare files across directories, identify duplicates by filename, merge folder contents while avoiding overwrites, or sync files between locations. Trigger when users mention comparing folders, checking for duplicates, copying unique files, merging directories, or avoiding duplicate files.
---

# Check Duplicate File

A skill for comparing files between two folders and copying unique files while avoiding duplicates.

## What This Skill Does

This skill helps you compare files between two directories and intelligently copy only the unique files from a source folder to a destination folder. It compares files by filename (not content) and provides clear feedback about what was copied and what was skipped.

## When to Use This Skill

Use this skill when the user wants to:
- Compare files between two folders
- Copy files from one folder to another while avoiding duplicates
- Merge folder contents without overwriting existing files
- Get a report of which files are unique vs duplicated
- Sync files between directories based on filename

## How It Works

The skill provides a Python script that:

1. Scans the destination folder and creates a list of all existing files
2. Scans the source folder and creates a list of all files to potentially copy
3. Compares filenames between the two folders
4. Copies any file from the source to the destination if it doesn't already exist there (by filename)
5. Provides detailed output showing which files were copied and which were skipped

## Key Features

- Cross-platform path handling using `pathlib.Path`
- Preserves file metadata during copying with `shutil.copy2()`
- Comparison based on filename only (not file content or size)
- Clear console output showing the operation results
- Non-destructive - never overwrites existing files

## Usage Pattern

When a user asks to check for duplicates or copy unique files:

1. Clarify which folder is the destination (where files should end up) and which is the source (where to copy from)
2. Use the provided script or adapt it to the user's specific folder paths
3. Run the script to perform the comparison and copying
4. Show the user the results: which files were copied and which were skipped

## The Script

Here's the core script that implements this functionality:

```python
import os
import shutil
from pathlib import Path

def get_file_list(folder_path):
    """Get list of all files with full paths in a folder."""
    file_list = []
    folder = Path(folder_path)
    
    if folder.exists() and folder.is_dir():
        for file_path in folder.iterdir():
            if file_path.is_file():
                file_list.append(str(file_path))
    
    return file_list

def check_and_copy_files(destination_folder, source_folder):
    """Check for duplicates and copy unique files from source to destination."""
    # Create list of files in destination folder
    dest_files = get_file_list(destination_folder)
    print(f"Files in {destination_folder}:")
    for f in dest_files:
        print(f"  {f}")
    
    # Create list of files in source folder
    source_files = get_file_list(source_folder)
    print(f"\nFiles in {source_folder}:")
    for f in source_files:
        print(f"  {f}")
    
    # Extract just filenames for comparison
    dest_filenames = {Path(f).name for f in dest_files}
    
    # Check each file in source and copy if not in destination
    print(f"\nChecking for duplicates...")
    copied_files = []
    
    for file_path in source_files:
        filename = Path(file_path).name
        
        if filename not in dest_filenames:
            # File doesn't exist in destination, copy it
            destination_path = Path(destination_folder) / filename
            shutil.copy2(file_path, destination_path)
            copied_files.append(filename)
            print(f"  Copied: {filename}")
        else:
            print(f"  Skipped (duplicate): {filename}")
    
    print(f"\nSummary: Copied {len(copied_files)} file(s) to {destination_folder}")

if __name__ == "__main__":
    # Example usage - modify these paths as needed
    destination = "folder1"
    source = "folder2"
    
    check_and_copy_files(destination, source)
```

## Customization

You can adapt this script for different use cases:

- **Recursive folder scanning**: Modify `get_file_list()` to use `folder.rglob('*')` instead of `folder.iterdir()`
- **Content-based comparison**: Add hash comparison using `hashlib` to compare file contents, not just names
- **Selective file types**: Add filtering by file extension
- **Move instead of copy**: Replace `shutil.copy2()` with `shutil.move()`
- **Dry run mode**: Add a flag to preview what would be copied without actually copying

## Important Notes

- The script compares files by filename only - two files with the same name but different content are considered duplicates
- Existing files in the destination are never overwritten
- The script only processes files in the immediate directory, not subdirectories (unless modified for recursion)
- File metadata (timestamps, permissions) is preserved during copying thanks to `shutil.copy2()`

## Path Operator Explanation

The script uses `Path(folder) / filename` which is Python's modern way to construct file paths. It's equivalent to `os.path.join(folder, filename)` but more readable and works consistently across Windows, macOS, and Linux.
