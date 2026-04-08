import json
from pathlib import Path
from traceback import walk_tb


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

def linear_search(seq,wanted):
    search = {}
    positions = []
    count = 0
    for idx,n in enumerate(seq):
        if n == wanted:
            positions.append(idx)
            count += 1
    search = {"positions":positions,"count":count}
    return search


def binary_search(numbers,wanted_number):



def main():
    sequence = read_data("sequential.json","dna_sequence")
    wanted_NK = linear_search(sequence,"A")

    numbers = read_data("sequential.json","ordered_numbers")

    print(sequential_data)
    print(wanted_NK)


if __name__ == '__main__':
    main()