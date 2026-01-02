def file_reader():
    with open('test_finale.file', 'rb') as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            print(last_line)
            return last_line
        else:
            print("File is empty")
            return None

# Call the function
file_reader()

while True:
    file_reader()