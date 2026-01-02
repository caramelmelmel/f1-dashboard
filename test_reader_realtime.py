import time

def follow(the_file):
    """
    Generator that yields new lines appended to the end of a file.
    It mimics the 'tail -f' behavior.
    """
    try:
        # 1. Open the file for reading
        the_file.seek(0, 2) # Seek to the end of the file (0 offset from position 2/end)
        
        while True:
            # 2. Read any new line that has been written since the last check
            line = the_file.readline()
            
            # 3. Check if new data was read
            if not line:
                # If readline returns an empty string, no new data has been written yet.
                # Pause execution for a short time to avoid consuming 100% CPU.
                time.sleep(0.1) 
                continue # Go back to the top of the loop
            
            # 4. Yield the new line
            yield line.strip() # .strip() removes the newline character

    except FileNotFoundError:
        print(f"Error: File not found.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

# --- Example Usage ---
FILE_PATH = '07_dec_2025_finale_saved_data.txt'

print(f"--- Starting to tail file: {FILE_PATH} ---")

try:
    # Use 'with open' to ensure the file is closed properly
    with open(FILE_PATH, 'r') as logfile:
        
        # Iterate over the generator to process new lines as they arrive
        for newline in follow(logfile):
            print(f"{newline}")
            # Add your real-time processing logic here (e.g., parsing, logging)
            
except KeyboardInterrupt:
    print("\n--- Tailing stopped by user. ---")