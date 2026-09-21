import os
import shutil
from pathlib import Path

def copy_markdown_files(source_dir: str, dest_dir: str):
    # Convert to Path objects for better path handling
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)
    
    # Walk through all directories and files in source
    for root, dirs, files in os.walk(source_path):
        # Get the relative path from the source directory
        rel_path = Path(root).relative_to(source_path)
        
        # Create corresponding directory in destination
        dest_dir_path = dest_path / rel_path
        dest_dir_path.mkdir(parents=True, exist_ok=True)
        
        # Process each file
        for file in files:
            if file.lower().endswith('.md'):
                source_file = Path(root) / file
                dest_file = dest_dir_path / file
                
                # Skip if destination file already exists
                if not dest_file.exists():
                    shutil.copy2(source_file, dest_file)
                    print(f"Copied: {source_file} -> {dest_file}")
                else:
                    print(f"Skipped existing file: {dest_file}")

if __name__ == "__main__":
    # Example usage
    source_directory = input("Enter source directory path: ")
    destination_directory = input("Enter destination directory path: ")
    
    copy_markdown_files(source_directory, destination_directory)
