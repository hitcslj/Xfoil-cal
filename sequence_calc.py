import argparse
import os
import subprocess
import time
import yaml
from _utils import *

def load_config(file_path):
    with open(file_path, "r") as ymlfile:
        return yaml.safe_load(ymlfile)

def write_xfoil_input(airfoil_name, config, args):
    output_dir = os.path.join('result', airfoil_name)
    os.makedirs(output_dir, exist_ok=True)
    output_file_name = getOutputFileName(OutputFiles.POLAR, config['setup']['polarfiles_dir'])(airfoil_name)
    if args.delete_old and os.path.exists(output_file_name):
        os.remove(output_file_name)

    input_file_path = os.path.join(output_dir, 'input_file.in')
    with open(input_file_path, 'w') as input_file:
        input_file.write(f'LOAD cst_gen/{airfoil_name}.dat\n')
        input_file.write(f'{airfoil_name}\n')
        input_file.write('PLOP\n')
        input_file.write('G F\n\n')
        input_file.write("PPAR\n")
        input_file.write(f"n {config['setup']['n_panelnodes']}\n\n\n")
        input_file.write("PANE\n")
        input_file.write("OPER\n")

        if args.reynolds_num >= 0:
            input_file.write(f"Visc {args.reynolds_num}\n")
        
        if args.mach_num > 0:
            input_file.write(f"Mach {args.mach_num}\n")
            
        input_file.write("PACC\n")
        input_file.write(f"{output_dir}/{args.mach_num}\n\n")

        if not args.delete_old:
            input_file.write("y\n\n")

        input_file.write(f"ITER {config['setup']['n_iter']}\n")
        input_file.write(f"CSeq {config['sequence_variables']['cl_i']} {config['sequence_variables']['cl_f']} {config['sequence_variables']['cl_step']}\n")

        input_file.write("\n\n")
        input_file.write("quit\n")

    return input_file_path

def run_xfoil(input_file_path):
    try:
        subprocess.run(["./xfoil_linux_arm"], stdin=open(input_file_path), timeout=300, shell=True)  # 设置超时时间为300秒
    except subprocess.TimeoutExpired:
        print("XFoil process timed out.")

def main(args):
    config = load_config('config.yaml')

    for airfoil_name in args.aerofoil_names:
        input_file_path = write_xfoil_input(airfoil_name, config, args)
        run_xfoil(input_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--reynolds_num", type=int, default=-1,
                        help="Value of Reynolds Number as integer (-1 for inviscid flow)")
    
    parser.add_argument("-m", "--mach_num", type=float, default=0,
                        help="Value of Mach Number as integer")
    
    parser.add_argument('-o', '--delete_old', action='store_false', default=True,
                        help='If NOT FLAGGED (true), deletes any previously stored data for inputted aerofoils, else if FLAGGED (false), appends new data to this previously stored data')
    
    parser.add_argument('-n', '--aerofoil_names', nargs='+', default=['NACA0012', 'NACA0013', 'NACA0014'],
                        help='NACA 4-digit aerofoils to test (in "NACAxxxx" form)')

    args = parser.parse_args()
    main(args)
