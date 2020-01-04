import os
import sys
import re
import chardet
from WordSegmentation import *
from app import app

path = "data/DATA-UNICODE"


def preprocess():
    writeFileList()
    stno2Txt()
    segmentation()


def GetFileList(srcDir, fileList):
    # Get all files path into fileList
    newDir = srcDir
    if os.path.isfile(srcDir):
        fileList.append(srcDir)
    elif os.path.isdir(srcDir):
        for s in os.listdir(srcDir):
            newDir = os.path.join(srcDir, s)
            GetFileList(newDir, fileList)
    return fileList


def writeFileList():
    output = sys.stdout
    outputFile = open('paths.txt', 'w')
    sys.stdout = outputFile
    fileList = GetFileList(path, [])

    for route in fileList:
        print(route)

    outputFile.close()
    sys.stdout = output


def stno2Txt():
    # convert stno to txt
    for line in open('paths.txt'):
        # get file name
        line0 = line[0:4]
        line1 = line[5:17]
        line2 = line[18:21]
        line3 = line[22:-1]  # with postfix
        line4 = line[22:-6]  # without postfix
        line = line0 + "/" + line1 + "/" + line2 + "/" + line3

        path = line

        fb = open(path, 'rb')
        data = fb.read()
        encoding = chardet.detect(data)['encoding']
        page = open(line, 'r', encoding=encoding, errors='ignore').read()
        dr = re.compile(r'<[^>]>', re.S)
        dd = dr.sub('', page)

        fname = 'data/directory' + '/' + line4 + '.txt'  # file path
        f = open(fname, 'w+', encoding=encoding)
        f.write(dd)


with app.app_context():
    print('in with')
    db.app = app
    db.drop_all()
    db.create_all()
    preprocess()
