path = 'G:/BaiduNetdiskDownload/train/train_voc/labelmap.txt'
import os

with open(path) as f:
    text = []
    for line in f:
        text.append(line)

text.pop(0)

for i in range(len(text)):
    text[i] = text[i][:text[i].find(':')]
print(text)


