from cv2 import VideoCapture
from cv2 import imwrite
import os, random, shutil
import xml.etree.ElementTree as ET
import os

'''
img:要保存的图片名字
addr:图片地址以及相片名字前部分
num:第几张图片
'''
def save_img(img, addr, num):
    address = addr + str(num) +'.jpg'
    imwrite(address, img)


'''
file_dir: 此文件下存放原始图片
tar_dir: 目标路径
'''

def move_file(file_dir, tar_dir, label_dir = None, label_tar = None, rate = 0.2):
    all_path = os.listdir(file_dir)     #.jpg
    file_num = len(all_path)    #num
    pick_num = int(file_num * rate) #
    sample = random.sample(all_path, pick_num)
    txt_name = []
    for name in sample:
        txt_name.append(name[:-3]+'txt')

    for name in txt_name:
        name1 = label_dir + name
        name2 = label_tar + name
        # with open(name1, 'r', encoding='utf-8') as f1:
        #     if not os.path.exists(name2):
        #         os.makedirs(name2)
        #     with open(name2, 'w', encoding='utf-8') as f2:
        #         f2.write(f1.read())
        # print(name1,name2)
        shutil.move(name1, name2)

    for name in sample:
        shutil.move(file_dir + name, tar_dir + name)
if __name__ == '__main__':

    # video_path = r'E:\QQ\MobileFile\IMG_0090.mp4'
    # img_train_path = r'C:\Users\86178\Desktop\my_data\images/train/'
    # img_test_path = r'C:\Users\86178\Desktop\my_data\images/test/'
    # video = VideoCapture(video_path)
    # success, frame = video.read()
    # print()
    # #start_frame = 0
    # #end_frame = 1
    # j = 0
    # for i in range(len(frame)):
    #     save_img(frame, img_train_path, j)
    #     j+=1
    #     success, frame = video.read()

    img_orign_path = 'G:/BaiduNetdiskDownload/train/train/images/'
    img_tar_test_path = 'E:/yolov5-master/my_gestures/images/test/'
    img_tar_train_path = 'E:/yolov5-master/my_gestures/images/train/'

    labels_orign = r'C:/Users/86178/Desktop/gesture/labels/'
    labels_test = r'E:/yolov5-master/my_gestures/labels/test/'
    labels_train = r'E:/yolov5-master/my_gestures/labels/train/'

    move_file(img_orign_path, img_tar_test_path, rate=0.05, label_dir= labels_orign, label_tar= labels_test)
    move_file(img_orign_path, img_tar_train_path,rate = 1, label_dir= labels_orign, label_tar= labels_train)
