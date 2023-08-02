# Veeam Task Test
 
A brief overview of how the code works:

The script uses the argparse module to handle command-line arguments. Users can provide the source folder path, replica folder path, log file path, and synchronization interval as arguments when running the script.

The sync_folders function is the core of the synchronization process. It takes the source folder path, replica folder path, and log file path as arguments. It first checks if the source and replica folders exist and are valid directories. If not, it prints an error message and returns.

Inside the sync_folders function, the script iterates through each entry (files and subdirectories) in the source folder. For each entry, it constructs the full paths for both the source and replica.

If the entry is a file, it copies it from the source to the replica using shutil.copy2. The function then logs this action to the log file and also prints it to the console.

If the entry is a subdirectory, it recursively calls the sync_folders function to synchronize the subdirectory.

After synchronizing files and subdirectories, the function checks for files in the replica folder that are not present in the source folder. It removes such files from the replica folder to ensure it exactly matches the content of the source folder. This deletion action is also logged to the log file and printed to the console.

The log_to_file function handles logging file operations. It appends the log message to the log file, along with a newline character.

The main function handles the periodic synchronization. It runs an infinite loop where it calls the sync_folders function and then sleeps for the specified interval (in seconds) before repeating the synchronization.

When the script is executed, the main function is called. It parses the command-line arguments using argparse, and then the synchronization process begins. The script will continue to run in an infinite loop, periodically synchronizing the folders at the specified interval until you manually stop it.


You can execute the command to run the script in a terminal or command prompt.

Navigate to the directory where your Python script is located. 

Run the Python script using the python command followed by the script name and the command-line arguments. 

As example: 
python sync_script.py "C:\Users\nick_\Documents\Veeam-Task-Test\source" "C:\Users\nick_\Documents\Veeam-Task-Test\replica" "C:\Users\nick_\Documents\Veeam-Task-Test\sync_log.txt" 60

This will execute the script, and it will start synchronizing the source folder with the replica folder at the specified interval. The file operations will be logged to both the console output and the specified log file. The script will keep running and periodically synchronize the folders based on the provided interval until you manually stop it (Ctrl+C in the command prompt).