#images

from PIL import Image


def add_santa_hat(filepath):
    avatar = Image.open(filepath, 'r')
    hat = Image.open('./assets/santa_hat.png', 'r')
    avatar.paste(hat, (0, 0), hat)
    avatar.show()
    return avatar


def add_moustache(filepath):
    avatar = Image.open(filepath, 'r')
    moustache = Image.open('./assets/moustache.png', 'r')
    avatar.paste(moustache, (0, 0), moustache)
    avatar.show()
    return avatar

