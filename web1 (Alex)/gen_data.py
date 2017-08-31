from hashlib import sha256
from random import randint, choice
from string import printable
from os import chdir

FLAG='FLAG{mak3_y0ur_0wn_skr1pts_k33dy}'

def get_rand_file_name():
    return 'flag_' + sha256(str(randint(1, 2**20))).hexdigest()

def get_rand_file_data(mmin=20, mmax=50):
    return ''.join([choice(printable) for _ in range(randint(mmin, mmax))])

def mkfile(name, data):
    with open(name, 'w') as f:
        f.write(data)

def mkflag_file():
    file_name = get_rand_file_name()
    mkfile(file_name, FLAG)

def get_rand_files(count=1000):
    for i in range(count):
        file_name = get_rand_file_name()
        file_data = get_rand_file_data()
        mkfile(file_name, file_data)

if __name__ == '__main__':
    chdir('./nginx_root/flag_is_here')
    get_rand_files()
    mkflag_file()
