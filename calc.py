import os
import argparse
from concurrent.futures import ThreadPoolExecutor

def process_file(name, mas):
    for m in mas:
        command = f'python sequence_calc.py -r 1000000 -m {m} -n {name.split(".")[0]}'
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
    
    with ThreadPoolExecutor(max_workers=200) as executor:
        futures = []
        for name in names[s:e+1]:
            futures.append(executor.submit(process_file, name, mas))
        
        # 等待所有任务完成
        for future in futures:
            future.result()
    
    print("Done!")
    
    

