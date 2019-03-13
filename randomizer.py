import os
import random
import argparse


def get_command_args():
    pars = argparse.ArgumentParser()
    pars.add_argument("root_name", type=str)
    pars.add_argument("depth", type=int)
    return pars


def random_dir_gen(root_name, deep, dir_list):
    string = "abcdefghijklmnop"
    if deep == 0:
        return
    if deep < 0 or deep > 3000:
        print("Wrong deep")
    os.mkdir(root_name)
    dir_list.append(root_name)
    for i in range(0, random.randint(1, 5)):
        next_dir = ""
        for j in range(random.randint(3, 6)):
            next_dir += random.choice(string)
        random_dir_gen("{0}/{1}".format(root_name, next_dir), deep - 1, dir_list)


def random_files_gen(dir_list):
    tree = {"file": "abop", "a": "cd", "b": "ef", "c": "D", "d": "gh", "e": "ki", "f": "D", "g": "lm", "m": "D",
              "h": "D", "k": "D", "l": "D", "i": "j", "j": "n", "n": "D", "o": "D", "p": "D"}
    choose_minos = list()
    for key, value in tree.items():
        if (value == "D"):
            choose_minos.append(key)
    tree[random.choice(choose_minos)] = "Minotaur"
    for key, value in tree.items():
        with open(os.path.join(random.choice(dir_list), "{}.txt".format(key)), "w") as curr_file:
            if value == "Minotaur":
                curr_file.write(value)
            elif value == "D":
                curr_file.write("Deadlock")
            else:
                for i in range(0, len(value)):
                    curr_file.write("@include {}.txt\n".format(value[i]))


if __name__ == '__main__':
    try:
        directories = list()
        args = get_command_args().parse_args()
        random_dir_gen(args.root_name, args.depth, directories)
        random_files_gen(directories)
    except FileExistsError:
        print('The directory "{}" already exists!'.format(args.root_name))
