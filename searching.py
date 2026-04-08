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
    left_bound = 0
    right_bound = len(numbers) -1

    while left_bound <= right_bound:
        center = (left_bound + right_bound) //2
        if numbers[center] == wanted_number:
            return center
        elif numbers[center] < wanted_number:
            left_bound = center +1
        elif numbers[center] > wanted_number:
            right_bound = center -1

test = binary_search([-51, -12, -3, -3, -1, 2, 8, 13, 14, 14, 14, 21, 22, 23, 24, 25, 48, 63, 64, 70, 72, 78, 90, 102, 120],2)
print(test)
def main():
    sequence = read_data("sequential.json","dna_sequence")
    wanted_NK = linear_search(sequence,"A")

    numbers = read_data("sequential.json","ordered_numbers")
    print()

    print(sequence)
    print(wanted_NK)


if __name__ == '__main__':
    main()