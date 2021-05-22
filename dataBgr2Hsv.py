import cv2
import os

path_dir = 'data/jpg'
file_list = os.listdir(path_dir)

for file_name in file_list:
    print(file_name)
    rf='data/jpg'
    rf+=file_name
    src= cv2.imread(rf,cv2.COLOR_BGR2HSV)
    wf='data/hsvjpg'
    wf+=file_name
    cv2.imwrite(wf,src)
