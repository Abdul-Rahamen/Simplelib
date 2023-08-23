import math
import sys
from PIL import Image ,ImageFilter



class ImageAnalsis :
    def __init__(self):
        pass

    def convert(Im):
        if (sys.argv) != 2:
            sys.exit("Usage: python filter.py filters.png")
        image=Im.open(sys.argv[1]).convert("RGB")
        return image
    def FilterImage(image):
        filtered = image.filter(ImageFilter.Kernel(
            size=(3,3,),
            kernel=[-1,-1,-1,-1,9,-1,-1,-1,-1],
            scale=1
        ))
        filtered.show()
f = ImageAnalsis()
if __name__ == "__main__":
   m = f.convert(Image)
   f.convert(m)