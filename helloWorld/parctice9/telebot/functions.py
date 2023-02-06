def get_token(file):
    with open(file, 'r') as data:
        return data.readline()
