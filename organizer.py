import os
import shutil
import argparse # Needed for handling command-line arguments

FILE_TYPES = {
    # Images
    'IMAGES': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff'],
    # Videos
    'VIDEOS': ['.mp4', '.mov', '.avi', '.mkv', '.wmv'],
    # Documents
    'DOCUMENTS': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.txt', '.odt'],
    # Code/Scripts
    'CODE': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.rb'],
    # Archives
    'ARCHIVES': ['.zip', '.rar', '.7z', '.tar'], # Added missing '.' to '.7z'
}

def organize_files(directory):
    """Organizes files in the given directory into subfolders based on extension."""

    # to check if the directory exists 
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        return
    
    print(f"Starting organization in: {directory}")

    for filename in os.listdir(directory):
        source_path = os.path.join(directory, filename)

        # Skip directories and the script itself (using os.path.basename(__file__) is safer)
        if os.path.isdir(source_path) or filename == os.path.basename(__file__): 
            continue
        
        # to get the extension of file
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        target_folder = 'OTHERS' # default folder for unlisted extension type

        # --- CORRECT LOGIC HERE ---
        for folder, extensions in FILE_TYPES.items():
            if extension in extensions:
                target_folder = folder
                break # Found a match, stop searching
        # --------------------------
        
        # create the target folder path
        target_dir_path = os.path.join(directory, target_folder)

        # create the folder if it doesn't exist
        os.makedirs(target_dir_path, exist_ok = True)

        # move the file
        destination_path = os.path.join(target_dir_path, filename)

        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename} -> {target_folder}/")
        except Exception as e:
            print(f"Error moving {filename}: {e}")


# ------------------ Execution Block with argparse ------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A simple Command Line Interface tool to organize files into type-based folders."
    )
    
    # Define the argument: the user MUST provide a directory path
    parser.add_argument(
        'directory', 
        type=str, 
        help='The path to the directory you want to organize (e.g., C:/Users/Parth/Downloads).'
    )

    args = parser.parse_args()
    
    # Run the organizer on the directory provided by the user
    organize_files(args.directory)
    print('\nOrganization complete!')