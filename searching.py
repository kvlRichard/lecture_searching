import json
from pathlib import Path
from generators import dna_sequence, ordered_sequence
import time



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

def get_time():
    sizes = [100, 500, 1000, 5000, 10000]
    linear_times = []
    binary_times = []
    for size in sizes:
        seq = dna_sequence(max_len = size)
        numbers = ordered_sequence(max_len=size)
        start_linear = time.perf_counter()
        linear_search(seq,"A")
        end_linear = time.perf_counter()
        linear_duration = end_linear - start_linear
    linear_times.append(linear_duration)
    print(linear_duration)

test = get_time()
print(test)

def main():
    sequence = read_data("sequential.json","dna_sequence")
    wanted_NK = linear_search(sequence,"A")
    numbers = read_data("sequential.json","ordered_numbers")
    wanted_number = binary_search(numbers,23)
    print(sequence)
    print(wanted_NK)


if __name__ == '__main__':
    main()