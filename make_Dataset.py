'''
Author: Wuyao 1955416359@qq.com
Date: 2023-05-27 19:47:51
LastEditors: Wuyao 1955416359@qq.com
LastEditTime: 2023-05-27 19:48:11
FilePath: \Make_Dataset1\make_Dataset.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import random
import shutil
from tqdm import tqdm

def split_files(input_dir1, input_dir2, output_dir1,output_dir2):
    txt_files = os.listdir(input_dir1)
    jpg_files = os.listdir(input_dir2)

    # 随机打乱文件列表
    random.shuffle(txt_files)


    total_files = len(txt_files)
    train_ratio = int(total_files * 0.7)
    val_ratio = int(total_files * 0.2)
    test_ratio = total_files - train_ratio - val_ratio

    # 创建新的目录
    train_dir = os.path.join(output_dir2, 'train')
    val_dir = os.path.join(output_dir2, 'val')
    test_dir = os.path.join(output_dir2, 'test')

    train_dir_labels = os.path.join(output_dir1, 'train')
    val_dir_labels = os.path.join(output_dir1, 'val')
    test_dir_labels = os.path.join(output_dir1, 'test')

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    os.makedirs(train_dir_labels, exist_ok=True)
    os.makedirs(val_dir_labels, exist_ok=True)
    os.makedirs(test_dir_labels, exist_ok=True)



    # 复制文件到新的目录，并显示进度条
    print("正在分配文件...")
    for i, txt_file in enumerate( tqdm(txt_files[:train_ratio], desc='Train files', unit='file')):
        jpg_file = os.path.splitext(txt_file)[0] + ".jpg"
        src_txt = os.path.join(input_dir1, txt_file)
        src_jpg = os.path.join(input_dir2, jpg_file)
        shutil.copy(src_txt, os.path.join(train_dir_labels,txt_file))
        shutil.copy(src_jpg, os.path.join(train_dir, jpg_file))

    for i, txt_file in enumerate( tqdm(txt_files[train_ratio:train_ratio + val_ratio], desc='Validation files', unit='file')):
        jpg_file = os.path.splitext(txt_file)[0] + ".jpg"
        src_txt = os.path.join(input_dir1, txt_file)
        src_jpg = os.path.join(input_dir2, jpg_file)
        shutil.copy(src_txt, os.path.join(val_dir_labels,txt_file))
        shutil.copy(src_jpg, os.path.join(val_dir, jpg_file))

    for i, txt_file in enumerate( tqdm(txt_files[train_ratio + val_ratio:], desc='Test files', unit='file')):
        jpg_file = os.path.splitext(txt_file)[0] + ".jpg"
        src_txt = os.path.join(input_dir1, txt_file)
        src_jpg = os.path.join(input_dir2, jpg_file)
        shutil.copy(src_txt, os.path.join(test_dir_labels,txt_file))
        shutil.copy(src_jpg, os.path.join(test_dir, jpg_file))

    print("文件分配完成！")

# 设置输入文件夹和输出文件夹的路径
# input_dir1 = '/path/to/txt_folder'
# input_dir2 = '/path/to/jpg_folder'
# output_dir1 = '/path/to/output_folder/labels'
# output_dir2 = '/path/to/output_folder/images'

input_dir1 = r'D:\epai\yolov5-6.0\my_data\labels\train'
input_dir2 = r'D:\epai\yolov5-6.0\my_data\images\train'
output_dir1 = r'D:\epai\yolov5-6.0\newdataset\labels'
output_dir2 =  r'D:\epai\yolov5-6.0\newdataset\images'
# 调用函数进行文件分配
split_files(input_dir1, input_dir2, output_dir1, output_dir2)
