import os
import argparse


def get_root_name():
    parser = argparse.ArgumentParser()
    parser.add_argument("root_name", type=str)
    args = parser.parse_args()
    return args.root_name


def find_next_file(root_name, file_name):
    for root, dirs, files in os.walk(root_name):
        for file in files:
            if file == file_name:
                return os.path.join(root, file)
    return None


def find_minos(root_name, file_name, my_list):
    curr_path = find_next_file(root_name, file_name)
    my_list.append(curr_path)
    if curr_path is None:
        my_list.pop()
        return 0
    with open(curr_path, 'r') as curr_file:
        line = curr_file.readline()
        if not line:
            print("File is empty")
            return 1
        while line:
            if line.strip() == "Deadlock":
                my_list.pop()
                return 1
            elif line.strip() == "Minotaur":
                return 0
            elif line.split()[0] == "@include" and line.split()[1].endswith(".txt"):
                if find_minos(root_name, line.split()[1], my_list) == 0:
                    return 0
                line = curr_file.readline()
            else:
                print("Wrong input in file \"{}\"".format(file_name))
                return 1
    return 1


def process():
    root_name = get_root_name()
    try:
        my_list = list()
        if find_minos(root_name, "file.txt", my_list) == 0:
            for i in my_list:
                print("./{}".format(i))
        else:
            print("Minotaur was not found")
    except FileNotFoundError:
        print("Directory \"{}\" was not found".format(root_name))


if __name__ == "__main__":
    process()

