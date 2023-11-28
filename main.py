import os
from PIL import Image, ImageEnhance


#  ImageEnhance.Color(image)
#  ImageEnhance.Contrast(image)
#  ImageEnhance.Brigthness(image)
#  ImageEnhance.Sharpness(image)


def main():
    rootPath = "aglonema/"
    pathList = [rootPath + path + "/" for path in os.listdir(rootPath)]

    for path in pathList:
        for image in os.listdir(path):
            imageFileName = os.fsdecode(image)
            imagePath = path + imageFileName

            # Saturation
            image = Image.open(imagePath)
            enhancer = ImageEnhance.Color(image)
            factor = 5
            output = enhancer.enhance(factor)

            if not os.path.exists(f"output/saturation/{factor}/{path}"):
                os.makedirs(f"output/saturation/{factor}/{path}")
            output.save(f"output/saturation/{factor}/{imagePath}")


if __name__ == "__main__":
    main()
