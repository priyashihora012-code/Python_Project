# import os

# def create_file(filename):
#     f = open(filename, 'w')
#     f.close()
#     print("File created successfully!")

# def write_file(filename, data):
#     with open(filename, 'w') as f:
#         f.write(data)
#     print("Data written successfully!")

# def read_file(filename):
#     if os.path.exists(filename):
#         with open(filename, 'r') as f:
#             print("File Content:")
#             print(f.read())
#     else:
#         print("File does not exist!")

# def append_file(filename, data):
#     with open(filename, 'a') as f:
#         f.write("\n" + data)
#     print("Data appended successfully!")

# # Direct run test code
# if __name__ == "__main__":
#     print("Testing file operations module directly.")

def create_file(fname):
    f = open(fname, "w")
    f.close()
    return "File created successfully!"

def write_file(fname, data):
    f = open(fname, "w")
    f.write(data)
    f.close()
    return "Data written successfully!"

def read_file(fname):
    try:
        f = open(fname, "r")
        data = f.read()
        f.close()
        return data
    except:
        return "File does not exist."

def append_file(fname, data):
    f = open(fname, "a")
    f.write(data)
    f.close()
    return "Data appended successfully!"