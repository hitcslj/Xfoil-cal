import os
import argparse
import subprocess


def process_file(name):
    for i in range(len(mas)):
        command = f'python Sequence_calc.py -r 1000000 -m {mas[i]} -n {name.split(".")[0]}'
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_path", type=str, default='/home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen',
                        help="airfoil data path")
    
    parser.add_argument("--s", type=int, default=0,
                        help="start index")
    parser.add_argument("--e", type=int, default=1,
                    help="end index")
    
    args = parser.parse_args()

    data_path = args.data_path
    names = os.listdir(data_path)
    names.sort()
    n = len(names)
    mas = [0.2,0.3,0.4,0.5,0.6,0.7]
    s,e = min(args.s,n-1),min(args.e,n-1)
    for name in names[s:e+1]:
        process_file(name)
    print("Done!")  
'''
python calc.py --data_path ~/airfoil/cst_gen --s 0 --e 9999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 10000 --e 19999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 20000 --e 29999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 30000 --e 39999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 40000 --e 49999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 50000 --e 59999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 60000 --e 69999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 70000 --e 79999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 80000 --e 89999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 90000 --e 99999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 100000 --e 109999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 110000 --e 119999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 120000 --e 129999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 130000 --e 139999
python calc.py --data_path /home/bingxing2/ailab/scxlab0059/data/airfoil/cst_gen --s 140000 --e 149999
'''
    
    

