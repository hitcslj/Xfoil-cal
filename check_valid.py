import os
from multiprocessing import Pool


def process_file(airfoil_result_path):
    # 遍历airfoil_result_path里面的文件
    for root, dirs, files in os.walk(airfoil_result_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file[0]=='0':
              # 读取文件内容
              with open(file_path, 'r') as f:
                  lines = f.readlines()
                  if len(lines)>12:
                      return True
    return False

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

  cnt = sum(results)
  print(cnt / len(files_paths))
