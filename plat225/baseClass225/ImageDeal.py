from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image
from func.getPath import getPath


def imgScaled(image, width=100, height=100):

    img = QImage(image)
    result = img.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    return result


def imgTrans(image, width=200, height=200):

    img = Image.open(image)
    img.thumbnail((width, height))
    return img


def imgSave(image, outName, width=200, height=200, style='png'):
    path = getPath('【款号图片】')
    outFileName = path + str(outName).strip() + '.' + style
    img = Image.open(image)
    img.thumbnail((width, height))
    # img.show()
    img.save(outFileName)


def pixmapSave(image, out_name, width=200, height=200, pict_format='png'):
    path = getPath('【款号图片】')
    out_file_name = path + str(out_name).strip() + '.' + pict_format
    img = QPixmap(imgScaled(image, width, height))
    img.save(out_file_name)

    # image = QPixmap(imgScaled(imageList[4], 200, 200))
    # image.save(get_path('【款号图片】') + str('实例15').strip() + '.png')


if __name__ == '__main__':
    imageList = ['C:\\Users\\10145\\Desktop\\1.png',
                 'C:\\Users\\10145\\Desktop\\2.png',
                 'C:\\Users\\10145\\Desktop\\3.jpg',
                 'C:\\Users\\10145\\Desktop\\4.png',
                 'C:\\Users\\10145\\Desktop\\5.jpg',
                 'C:\\Users\\10145\\Desktop\\6.png',
                 'C:\\Users\\10145\\Desktop\\7.png',
                 'C:\\Users\\10145\\Desktop\\8.png',
                 'C:\\Users\\10145\\Desktop\\9.png',
                 'C:\\Users\\10145\\Desktop\\10.png']

    for i in imageList:
        imgSave(i, '示范{}'.format(imageList.index(i) + 1))
