def read_file(file):
    with open(file, 'r') as f:
        return f.read()

def write_file(file, s):
    with open(file, 'w+') as f:
        return f.write(s)