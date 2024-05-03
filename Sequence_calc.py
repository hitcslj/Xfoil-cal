from _utils import *
import argparse
import time
import yaml
import os
from subprocess import Popen


def main(args: argparse.Namespace):

    # Open + read YAML config file
    with open('config.yaml', "r") as ymlfile:
        cfg: dict = yaml.safe_load(ymlfile)

    # Set directory to the dir of XFOIL
    # os.chdir(cfg['setup']['xfoil_path'])
    # current_directory = os.getcwd()
    # print("当前工作目录为:", current_directory)
    # Create output folder (if it doesn't already exist)
    if not os.path.isdir(cfg['setup']['polarfiles_dir']):
        os.mkdir(cfg['setup']['polarfiles_dir'])

    # --------------------------------------------------------------------------
    # XFOIL input file writer

    for airfoil_name in args.aerofoil_names:

        output_file_name = getOutputFileName(OutputFiles.POLAR, cfg['setup']['polarfiles_dir'])(airfoil_name)
        os.makedirs(f'result/{airfoil_name}',exist_ok=True)
        if args.delete_old and os.path.exists(output_file_name):
            os.remove(output_file_name)

        with open("input_file.in", 'w') as input_file:
            input_file.write('LOAD cst_gen/' + airfoil_name + '.dat' + '\n')
            input_file.write(airfoil_name + '\n' )
            input_file.write('PLOP\n')
            input_file.write('G F\n\n')
            input_file.write("PPAR\n")
            input_file.write(f"n {cfg['setup']['n_panelnodes']}\n\n\n")


            input_file.write("PANE\n")
            input_file.write("OPER\n")

            if args.reynolds_num >= 0:
                input_file.write(f"Visc {args.reynolds_num}\n")
                
            if args.mach_num > 0:
                input_file.write(f"Mach {args.mach_num}\n")
                
            input_file.write("PACC\n")
            
            input_file.write(f"result/{airfoil_name}/{args.mach_num}\n\n")

            if not args.delete_old:
                input_file.write("y\n\n")

            input_file.write(f"ITER {cfg['setup']['n_iter']}\n")
            input_file.write(f"CSeq {cfg['sequence_variables']['cl_i']} {cfg['sequence_variables']['cl_f']} {cfg['sequence_variables']['cl_step']}\n")

            input_file.write("\n\n")
            input_file.write("quit\n")

        
        # Running calculations in XFOIL 
        # (ARM linux) ./xfoil_linux_arm
        # (x86-64 linux) ./xfoil
        # (windows) ./xfoil.exe
        
        Popen("./xfoil < input_file.in", shell=True)

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