from PIL import Image
import glob
import sys

def merge(logo, image, resample=Image.BICUBIC, resize_big_image=True):
    if logo.height == image.height:
        _logo = logo
        _image = image
    elif (((logo.height > image.height) and resize_big_image) or
          ((logo.height < image.height) and not resize_big_image)):
        _logo = logo.resize((int(logo.width * image.height / logo.height), image.height), resample=resample)
        _image = image
    else:
        _logo = logo
        _image = image.resize((int(image.width * logo.height / image.height), logo.height), resample=resample)
    dst = Image.new('RGB', (_logo.width + _image.width, _logo.height))
    dst.paste(_logo, (0, 0))
    dst.paste(_image, (_logo.width, 0))
    return dst

def main():
    images = glob.glob("*.jpg")
    logo = Image.open("" + str(sys.argv[1]) + "")
    path = "/".join(sys.argv[1].split("/")[:-1])
    brand = sys.argv[1].split("/")[-2]
    count = 0
    for image in images:
        image = Image.open(image)
        count += 1
        merge(logo, image).save(f"{path}/{brand}_{count}.jpg")


if __name__ == '__main__':
    main()