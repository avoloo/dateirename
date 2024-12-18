import os
import logging

def setup_logger():
    """Set up the logger to record changes."""
    logging.basicConfig(
        filename="file_rename.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("Log initialized.")

def rename_files_in_directory(directory, search_text, replace_text):
    """Recursively rename files in a directory by replacing a specific text in their names."""
    if not os.path.exists(directory):
        print("The provided directory does not exist.")
        return

    logging.info(f"Starting renaming in directory: {directory}")
    for root, _, files in os.walk(directory):
        for file_name in files:
            if search_text in file_name:
                old_path = os.path.join(root, file_name)
                new_name = file_name.replace(search_text, replace_text)
                new_path = os.path.join(root, new_name)

                try:
                    os.rename(old_path, new_path)
                    logging.info(f"Renamed: {old_path} -> {new_path}")
                    print(f"Renamed: {old_path} -> {new_path}")
                except Exception as e:
                    logging.error(f"Failed to rename {old_path}: {e}")
                    print(f"Failed to rename {old_path}: {e}")
    logging.info("Renaming completed.")

def main():
    setup_logger()
    print("Welcome to the File Renamer Tool!")

    directory = input("Enter the directory path where files are located: ").strip()
    search_text = input("Enter the text to search for in file names: ").strip()
    replace_text = input("Enter the text to replace it with: ").strip()

    if not directory or not search_text or not replace_text:
        print("Invalid input. Please provide all required information.")
        return

    rename_files_in_directory(directory, search_text, replace_text)

if __name__ == "__main__":
    main()
