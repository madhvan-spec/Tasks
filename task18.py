class FileReadError(Exception):
    pass

class FileNotFound(FileReadError):
    pass

class FileEmpty(FileReadError):
    pass

def read_file(path):
    try:
        with open(path, "r") as f:
            data = f.read()
            if not data:
                raise FileEmpty("The file is empty")
            return data

    except FileNotFoundError:
        raise FileNotFound(f"File not found: {path}")


try:
    print(read_file("task18.txt"))
except FileReadError as e:
    print("Error:", e)
