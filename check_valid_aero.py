import os
from multiprocessing import Pool
import numpy as np
import matplotlib.pyplot as plt


def find_cl_cd(line):
    ans = []
    for s in line.split(' '):
        if len(s)==0:continue
        ans.append(float(s))
        if len(ans)==3:break
    return ans

def process_file(airfoil_result_path):
    # 遍历airfoil_result_path里面的文件
    cnt = set()
    for root, dirs, files in os.walk(airfoil_result_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file[0]=='0':
              num = int(file[2]) # 查看马赫数
              # 读取文件内容
              with open(file_path, 'r') as f:
                  lines = f.readlines()
                  if len(lines)<12:continue
                  for i in range(12,len(lines)):
                      line = lines[i]
                      alpha,cl,cd = find_cl_cd(line)
                      if (cl,cd) in cnt:
                          # 重复了，需要将后面的字符串删除
                          lines = lines[:i]
                          break
                      cnt.add((cl,cd))
              # 将lines的内容重新写入file_path 
              with open(file_path, 'w') as f:
                f.writelines(lines)    
    return len(cnt)

if __name__ == '__main__':
  root_path = 'result'
  files_paths = []
  # 检查一下result目录下面的一级文件夹
  for file in os.listdir(root_path):
      file_path = os.path.join(root_path, file)
      files_paths.append(file_path)

  # 使用多进程处理文件
  with Pool(processes=8) as pool:
      results = pool.map(process_file, files_paths)

  # Calculate the distribution
  unique_counts, count_frequencies = np.unique(results, return_counts=True)

  # Plotting the distribution
  plt.bar(unique_counts, count_frequencies)
  plt.xlabel('Count')
  plt.ylabel('Frequency')
  plt.title('Distribution of Count Values')
  plt.show()
  plt.savefig('Distribution of Count Values.png')
