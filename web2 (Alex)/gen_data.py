from hashlib import sha256
from random import randint, choice
from string import ascii_uppercase
from os import chdir, listdir

FLAG='FLAG{1s_1t_r3ally_s0_d1ff1cult}'

FLAG_LEN = len(FLAG)

def get_rand_file_name():
    return 'flag_' + sha256(str(randint(1, 2**20))).hexdigest()

def get_rand_file_data(data_len):
    return ''.join([choice(ascii_uppercase) for _ in range(data_len)])

def mkfile(name, data):
    with open(name, 'w') as f:
        f.write(data)

def mkflag_file():
    file_name = get_rand_file_name()
    mkfile(file_name, FLAG)

def get_rand_files():
    for i in range(FLAG_LEN):
        file_name = get_rand_file_name()
        #file_data = get_rand_file_data()
        mkfile(file_name, '')

def fill_files():
    file_names = listdir(".")
    file_names.sort()
    for index, file_name in enumerate(file_names):
        letter = FLAG[index]
        data = get_rand_file_data(ord(letter))
        mkfile(file_name, data)

if __name__ == '__main__':
    chdir('./nginx_root/flag_is_here')
    get_rand_files()
    fill_files()
