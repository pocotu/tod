import cv2
from svgpathtools import svg2paths2
from svg.path import parse_path
from tqdm import tqdm
class sketch_from_svg:
    def __init__(self, svg_file, img_file, img_size=(500, 500)):
        self.path