import xml.etree.ElementTree as ET
from os import listdir, getcwd
import glob
import os
import os.path
# classes information
classes = ['background', 'Two', 'Congratulation', 'Heart_single', 'OK', 'Heart_1', 'Nine', 'One', 'Four', 'Insult', 'Heart_3', 'ILY', 'Eight', 'Seven', 'Honour', 'Heart_2', 'Five', 'Thumb_up', 'Fist', 'Thumb_down', 'Three', 'Six', 'Rock', 'Prayer', 'Palm_up']

def convert(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

if __name__ == '__main__':
    path = "G:/BaiduNetdiskDownload/train/train/images"
    all_files = os.listdir("G:/BaiduNetdiskDownload/train/train/images")
    for image_path in all_files:  # image file path
        image_path = path + '/' + image_path
        image_name = image_path.split('/')[-1]
        fname = 'C:/Users/86178/Desktop/gesture/labels'
        if not os.path.exists(fname):
            os.makedirs(fname)
        out_file = open(fname + '/' + image_name[:-3] + 'txt', 'w')  # txt file path
        f = open('G:/BaiduNetdiskDownload/train/train_voc/Annotations/gesture/train/image/' + image_name[:-3] + 'xml', encoding="utf8")  # xml file path
        xml_text = f.read()
        f.close()

        '''find the element'''
        root = ET.fromstring(xml_text)
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)
        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes:
                print(cls)
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
                 float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')