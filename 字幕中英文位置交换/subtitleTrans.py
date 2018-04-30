#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# 转化人人影视字幕，将英文放在上面中文放在下面，完成后在原来字幕所在位置将产生一个新文件，文件名包含"英文&简体"
# 该脚本仅支持python3

import sys

if len(sys.argv) != 2:
    print("Usage:\npython3 subtitleTrans.py path/to/your/subtitle/file")
    sys.exit()

filepath = sys.argv[1]
outfile = filepath.replace("简体&英文", "英文&简体")
f1=None
f2=None
try:
    f1 = open(filepath, 'r', encoding='utf-16le')
    f2 = open(outfile, 'w')
    for line in f1.readlines():
        if line[0:9] == 'Dialogue:':
            pieces = line.split(',,')
            subPieces = pieces[1].split('\\N')
            if len(subPieces) >= 2:
                index = subPieces[1].find('}')
                if index != -1:
                    subPieces[1] = subPieces[1][index+1:]
                subPieces[1] = subPieces[1].strip('.\n')
                result = pieces[0] + ',,' + subPieces[1] + '\\N' + subPieces[0] + '.\n'
            else:
                result = pieces[0] + ',,' + subPieces[0]
            f2.write(result)
        else:
            f2.write(line)
finally:
    if f1:
        f1.close()
    if f2:
        f2.close()

