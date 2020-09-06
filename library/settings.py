import os
DIRPATH = os.path.dirname(os.path.dirname(__file__))

FILEPATH = DIRPATH + r'\data' + r'\users.yaml'


if __name__ == '__main__':
    print(FILEPATH)