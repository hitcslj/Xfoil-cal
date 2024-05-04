import os
import argparse
from concurrent.futures import ThreadPoolExecutor

def process_file(name, mas):
    for m in mas:
        command = f'python Sequence_calc.py -r 1000000 -m {m} -n {name.split(".")[0]}'
        os.system(command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--s", type=int, default=0,
                        help="start index")
    parser.add_argument("--e", type=int, default=10,
                    help="end index")
    
    args = parser.parse_args()

    data_path = './cst_gen'
    names = os.listdir(data_path)
    names.sort()
    n = len(names)
    mas = [0.2,0.3,0.4,0.5,0.6,0.7]
    s,e = min(args.s,n-1),min(args.e,n-1)
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for name in names[s:e+1]:
            futures.append(executor.submit(process_file, name, mas))
        
        # 等待所有任务完成
        for future in futures:
            future.result()
    
    print("Done!")

    
'''
python calc.py  --s 0 --e 9999
python calc.py  --s 10000 --e 19999
python calc.py  --s 20000 --e 29999
python calc.py  --s 30000 --e 39999
python calc.py  --s 40000 --e 49999
python calc.py  --s 50000 --e 59999
python calc.py  --s 60000 --e 69999
python calc.py  --s 70000 --e 79999
python calc.py  --s 80000 --e 89999
python calc.py  --s 90000 --e 99999
python calc.py  --s 100000 --e 109999
python calc.py  --s 110000 --e 119999
python calc.py  --s 120000 --e 129999
python calc.py  --s 130000 --e 139999
python calc.py  --s 140000 --e 149999
'''
    
    

