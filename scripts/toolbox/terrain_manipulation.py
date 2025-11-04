import argparse
import numpy as np
from PIL import Image

def parse_arguments():
    parser = argparse.ArgumentParser(description="Open the terrain image")
    parser.add_argument("-o", "--output", default="out.bmp", help="Path to the output image file (default: out.bmp)")
    parser.add_argument("-tm", "--terrainmap", default="terrain.bmp", help="Path to the terrain bitmap")
    parser.add_argument("-hm", "--heightmap", default="heightmap.bmp", help="Path to the height bitmap")
    parser.add_argument("-oc", "--oceancolor", default="8,31,130", help="Path to the height bitmap")
    parser.add_argument("-dc", "--desertcolor", default="206,169,99", help="Path to the height bitmap")
    parser.add_argument("-od", "--oceandepth", type=int, default=95, help="Path to the height bitmap")
    return parser.parse_args()


def read_image(filename):
    # Open an image file
    image = Image.open(filename)

    # Convert image to RGB (if not already in RGB mode)
    image = image.convert('RGB')

    # Access the pixel data
    return image.load(), image.size

if __name__ == "__main__":
    args = parse_arguments()

    terrainmap, size_terrain = read_image(args.terrainmap)
    heightmap, size_heightmap = read_image(args.heightmap)
    if size_terrain != size_heightmap:
        print("ok")
    size = list(size_terrain)

    tokens = args.oceancolor.split(",")
    ocean_color = [int(elmt) for elmt in tokens]

    tokens = args.desertcolor.split(",")
    desert_color = [int(elmt) for elmt in tokens]
    print(desert_color)

    out_image_pixel = np.zeros((size[1], size[0], 3), dtype=np.uint8)
    out_image_final = np.zeros((size[1], size[0], 3), dtype=np.uint8)

    for x in range(size[0]):
        for y in range(size[1]):
            if heightmap[x, y][0] < args.oceandepth:
                out_image_pixel[y, x] = ocean_color
            else:
                out_image_pixel[y, x] = terrainmap[x, y]

    print(size)
    for x in range(1, size[0]-1):
        if x % 100 == 0:
            print(x, size[0])
        for y in range(1, size[1]-1):
            if all(out_image_pixel[y, x][i] == ocean_color[i] for i in range(3)):
                out_image_final[y, x] = ocean_color
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if any(out_image_pixel[y+j, x+i][k] != ocean_color[k] for k in range(3)):
                            out_image_final[y, x] = desert_color
                            break
                    else:
                        continue
                    break
            else:
                out_image_final[y, x] = out_image_pixel[y, x]

    out_image = Image.fromarray(out_image_final)
    out_image.save("drawing_image.bmp")
    out_image = Image.fromarray(out_image_pixel)
    out_image.save("test.bmp")