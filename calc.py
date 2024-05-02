import subprocess
from multiprocessing import Pool
import os
import numpy as np

# For calculation
names = os.listdir('./foil')
mas = [0.2,0.3,0.4,0.5,0.6,0.7]
start,end = 0,0
def process_file(name):
    for i in range(len(mas)):
        command = f'python Sequence_calc.py -r 1000000 -m {mas[i]} -n {name.split(".")[0]}'
        subprocess.run(command, shell=True)


# with Pool(processes=8) as pool:
#     pool.map(process_file, names)
for name in names:
    process_file(name)


