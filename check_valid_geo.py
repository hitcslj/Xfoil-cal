import os
from multiprocessing import Pool
from data_gen import CSTLayer
import numpy as np
import matplotlib.pyplot as plt



def read_file(file_path):
    data = []
    with open(file_path) as file:
        for line in file:
            values = line.strip().split()
            data.append([float(values[0]), float(values[1])])
    return np.array(data)


def process_file(file_path):  # cst拟合的翼型和原始翼型的差距 （1433筛选？）

    data = read_file(file_path)
    name = file_path.split('/')[-1].split('.')[0]
    y = data[:,1]
    cst = CSTLayer()
    au,al,te = cst.fit_CST(y)#拟合中的x坐标和数量需要与原始翼型一致
    yu = cst.A0.dot(au) + cst.x_coords*te #cst.x_coords可以替换成你需要的x坐标分布
    yl = cst.A0.dot(al) - cst.x_coords*te
    yu_gt = y[:129][::-1]
    yl_gt = y[128:]
    # 计算上下表面的CST拟合误差
    error_u = np.mean(np.abs(yu - yu_gt))
    error_l = np.mean(np.abs(yl - yl_gt))
    error = error_u + error_l

    # Plotting the ground truth and fitted wing profiles
    plt.figure()
    plt.plot(cst.x_coords, yu_gt, 'r', label='Ground Truth Upper')
    plt.plot(cst.x_coords, yl_gt, 'r', label='Ground Truth Lower')
    plt.plot(cst.x_coords, yu, 'b', label='Fitted Upper')
    plt.plot(cst.x_coords, yl, 'b', label='Fitted Lower')

    # Display the fitting error as a text annotation
    plt.text(0.5, 0.9, f"Error: {error:.6f}", transform=plt.gca().transAxes, ha='center')

    plt.legend()
    # plt.show()
    plt.savefig(f'error_vis/{name}.png')
    return error<4e-4

if __name__ == '__main__':
  root_path = 'data/airfoil/interpolated_uiuc'
  os.makedirs('error_vis',exist_ok=True)
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

  # # Plotting the error distribution
  # plt.hist(errors, bins=20)  # Adjust the number of bins as needed
  # plt.xlabel('Fitting Error')
  # plt.ylabel('Frequency')
  # plt.title('Distribution of Fitting Errors')
  # plt.show()
  # plt.savefig('error.png')