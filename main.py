import os
from PIL import Image, ImageEnhance
import typer
from typing_extensions import Annotated


def main(process: Annotated[str, typer.Option(help="Processes for aglonema images (saturation/contrast/brigthness/shrapness)",
                                              prompt=True)] = "saturation",
         factor: Annotated[float, typer.Option(help="Processes for aglonema images (saturation/contrast/brigthness/shrapness)",
                                               prompt=True)] = 1.0):

    if process not in ["saturation", "contrast", "brigthness", "sharpness"]:
        print("No process matches.")
        exit()

    rootPath = "aglonema/"
    pathList = [rootPath + path + "/" for path in os.listdir(rootPath)]
    totalFiles = sum([len(files) for _, _, files in os.walk(rootPath)])

    print(
        f"Processing images with {process} adjustment by a factor of {factor}.")
    with typer.progressbar(range(totalFiles), label=f"Processing ...") as progress:
        for path in pathList:
            for image in os.listdir(path):
                imageFileName = os.fsdecode(image)
                imagePath = path + imageFileName

                image = Image.open(imagePath)
                if process == "saturation":
                    process = "color"
                enhancer = eval(f"ImageEnhance.{process.capitalize()}(image)")
                output = enhancer.enhance(factor)

                if process == "color":
                    process = "saturation"
                if not os.path.exists(f"output/{process}/{factor}/{path}"):
                    os.makedirs(f"output/{process}/{factor}/{path}")
                output.save(f"output/{process}/{factor}/{imagePath}")
                progress.update(1)
    print(f"Dang! Processed {totalFiles} images.")
    print(
        f"Saved in {os.path.abspath(os.getcwd())}/output/{process}/{factor}/")


if __name__ == "__main__":
    print(r"""
          
 ________  ________  ___       ________  ________  ___       ___     
|\   __  \|\   ____\|\  \     |\   __  \|\   ____\|\  \     |\  \    
\ \  \|\  \ \  \___|\ \  \    \ \  \|\  \ \  \___|\ \  \    \ \  \   
 \ \   __  \ \  \  __\ \  \    \ \  \\\  \ \  \    \ \  \    \ \  \  
  \ \  \ \  \ \  \|\  \ \  \____\ \  \\\  \ \  \____\ \  \____\ \  \ 
   \ \__\ \__\ \_______\ \_______\ \_______\ \_______\ \_______\ \__\
    \|__|\|__|\|_______|\|_______|\|_______|\|_______|\|_______|\|__|
    
    """)
    typer.run(main)
