import json
import subprocess,
import os
from multiprocessing import Pool
from pprint import pp

from makemkv import MakeMKV, ProgressParser


def get_disc_info(disc):
    with ProgressParser() as progress:
        makemkv = MakeMKV(disc, progress_handler=progress.parse_progress)
        makemkv.mkv('all', )


def get_labels(drive):
    p = subprocess.Popen(['powershell.exe', '-c', f'(Get-Volume {drive}).FileSystemLabel'], stdout=subprocess.PIPE)
    return p.stdout.read().strip()


def create_dir(label, base_path='/mnt/c/Users/ntolp/Videos/'):
    pass


drives = ['d', 'e']

with Pool() as pool:
    drive_paths = [f'/mnt/{drive}' for drive in drives]
    info = pool.map(get_disc_info, drive_paths)

with open('disc_info.json', 'w') as disc_info:
    json.dump(info, disc_info)
print("Done getting disc info!")
