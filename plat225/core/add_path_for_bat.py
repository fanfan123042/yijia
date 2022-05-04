import sys
import os

path_upper = '\\'.join(os.getcwd().split('\\')[:-1])
# print('当前上一层路径为:', path_upper)
path_exist = sys.path
# print('当前路径为:', path_exist)

if path_upper in path_exist and (path_upper + '\\core') in path_exist:
    pass
    # print('执行bat文件设置路径: 当前路径 {} 已在系统路径中... ...\n'.format(path_upper))
else:
    sys.path.insert(1, path_upper)
    sys.path.insert(1, path_upper + '\\core')
    sys.path.insert(1, path_upper + '\\baseClass219')
    sys.path.insert(1, path_upper + '\\ui')
    sys.path.insert(1, path_upper + '\\main')
    sys.path.insert(1, path_upper + '\\bin')

    # print('执行bat文件设置路径: 之前没有该路径 {}, 现已添加到系统路径中... ...\n'.format(path_upper))

