import os
import shutil

def sync_folders(source_folder, replica_folder):
    try:
        # Check if both source and replica folders exist
        if not os.path.exists(source_folder) or not os.path.isdir(source_folder):
            print(f"Source folder '{source_folder}' does not exist or is not a directory.")
            return
        if not os.path.exists(replica_folder):
            os.makedirs(replica_folder)
        elif not os.path.isdir(replica_folder):
            print(f"Replica folder '{replica_folder}' is not a directory.")
            return

        # Get the list of files and subdirectories in the source folder
        entries = os.listdir(source_folder)

        # Synchronize each file and subdirectory
        for entry in entries:
            source_path = os.path.join(source_folder, entry)
            replica_path = os.path.join(replica_folder, entry)

            # If the entry is a file, copy it from source to replica
            if os.path.isfile(source_path):
                shutil.copy2(source_path, replica_path)

            # If the entry is a subdirectory, recursively sync it
            elif os.path.isdir(source_path):
                sync_folders(source_path, replica_path)

        print(f"Synchronization completed from '{source_folder}' to '{replica_folder}'.")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    source_folder = r"C:\Users\Raijin\Desktop\Veeam\Veeam-Task-Test\Source"
    replica_folder = r"C:\Users\Raijin\Desktop\Veeam\Veeam-Task-Test\Replica"

    sync_folders(source_folder, replica_folder)