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
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python check_duplicates.py <destination_folder> <source_folder>")
        sys.exit(1)
    
    destination = sys.argv[1]
    source = sys.argv[2]
    
    check_and_copy_files(destination, source)
