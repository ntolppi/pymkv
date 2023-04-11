import subprocess, os
from multiprocessing import Pool

from makemkv import MakeMKV, ProgressParser


def create_mkv(drive_path):
    drive, path = drive_path
    disc = os.path.join('/mnt', drive)
    makemkv = MakeMKV(disc, minlength=120)
    makemkv.mkv('all', path)


def create_dir(drive, base_path='/mnt/c/Users/ntolp/Videos/'):
    p = subprocess.Popen(['powershell.exe', '-c', f'(Get-Volume {drive}).FileSystemLabel'], stdout=subprocess.PIPE)
    label = p.stdout.read().strip().decode()

    path = os.path.join(base_path, label)

    # Get list of directories in base path
    os_walk = os.walk(base_path)
    dir_list = next(os_walk)[1]

    # Check if label in base path
    if label not in dir_list:
        # Create directory
        os.mkdir(path)

    return drive, path


drives = ['d', 'e']
with Pool() as pool:
    paths = pool.map(create_dir, drives)

with Pool() as pool:
    info = pool.map(create_mkv, paths)
