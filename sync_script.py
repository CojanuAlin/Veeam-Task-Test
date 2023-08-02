import os
import shutil
import time
import argparse

def sync_folders(source_folder, replica_folder, log_file):
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
                log_to_file(log_file, f"Copied file: {source_path} to {replica_path}")
                print(f"Copied file: {source_path} to {replica_path}")

            # If the entry is a subdirectory, recursively sync it
            elif os.path.isdir(source_path):
                sync_folders(source_path, replica_path, log_file)

        # Remove files from the replica folder that are not in the source folder
        for entry in os.listdir(replica_folder):
            replica_path = os.path.join(replica_folder, entry)
            if os.path.isfile(replica_path) and not os.path.exists(os.path.join(source_folder, entry)):
                os.remove(replica_path)
                log_to_file(log_file, f"Removed file: {replica_path}")
                print(f"Removed file: {replica_path}")

        print(f"Synchronization completed from '{source_folder}' to '{replica_folder}'.")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        log_to_file(log_file, f"Error occurred: {str(e)}")

def log_to_file(log_file, message):
    with open(log_file, "a") as file:
        file.write(f"{message}\n")

def main():
    parser = argparse.ArgumentParser(description="Synchronize two folders: source and replica.")
    parser.add_argument("source_folder", help="Path to the source folder.")
    parser.add_argument("replica_folder", help="Path to the replica folder.")
    parser.add_argument("log_file", help="Path to the log file.")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds.")

    args = parser.parse_args()

    while True:
        sync_folders(args.source_folder, args.replica_folder, args.log_file)
        time.sleep(args.interval)

if __name__ == "__main__":
    main()
