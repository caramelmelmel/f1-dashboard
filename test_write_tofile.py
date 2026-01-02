import time
def file_writer():
    writing = f'Hello, World! {time.time()}\n'
    while True:
        with open('test_finale.file', 'ab') as file:
            file.write(f'Hello, World! {writing}\n'.encode())

file_writer()