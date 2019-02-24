import os
import random
import argparse
STRING = "abcdefghijklmnop"
DICTIONARY = {"file": "abop", "a": "cd", "b": "ef", "c": "D", "d": "gh", "e": "ki", "f": "D", "g": "lm", "m": "1",
              "h": "D", "k": "D", "l": "D", "i": "j", "j": "n", "n": "D", "o": "D", "p": "D"}


def get_command_args():
    pars = argparse.ArgumentParser()
    pars.add_argument("root_name", type=str)
    pars.add_argument("depth", type=int)
    return pars


def random_tree_gen(root_name, deep, dir_list):
    if deep == 0:
        return
    if deep < 0 or deep > 3000:
        print("Wrong deep")
    try:
        os.mkdir(root_name)
        dir_list.append(root_name)
        for i in range(random.randint(1, 2)):
            next_dir = ""
            for j in range(random.randint(3, 6)):
                next_dir += random.choice(STRING)
            random_tree_gen("{0}/{1}".format(root_name, next_dir), deep - 1, dir_list)
    except FileExistsError:
        raise


def random_files_gen(dir_list):
    tree = DICTIONARY
    tree[random.choice(STRING)] = "Minotaur"
    for key, value in tree.items():
        with open(os.path.join(random.choice(dir_list), "{}.txt".format(key)), "w") as curr_file:
            if value == "Minotaur":
                curr_file.write(value)
            elif value == "D":
                curr_file.write("Deadlock")
            else:
                for i in range(len(value)):
                    curr_file.write("@include {}.txt\n".format(value[i]))


if __name__ == '__main__':
    try:
        directories = list()
        args = get_command_args().parse_args()
        random_tree_gen(args.root_name, args.depth, directories)
        random_files_gen(directories)
    except FileExistsError:
        print("The directory \"{}\" already exists!".format(args.root_name))
