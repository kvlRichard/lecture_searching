import json
from pathlib import Path

# get current working directory path


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name
    with open(file_path,'r') as f:
        data = json.load(f)
        for key,value in data.items():
            if key == field:
                return value
        return None



def main():
    sequential_data = read_data("sequential.json","unordered_numbers")
    print(sequential_data)


if __name__ == '__main__':
    main()