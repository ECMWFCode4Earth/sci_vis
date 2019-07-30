# ---------------------------------------------------------------------------------
# | generate_icons.py |
# Scan (not recursively) the directories in the current folder for any
# .cpt file and create a .png equivalent with the same name. Requires the pillow
# library (https://pillow.readthedocs.io/en/stable/)
# ---------------------------------------------------------------------------------

from PIL import Image
import os
import colorsys


# ---------------------------------------------------------------------------------
# CTP READER
# ---------------------------------------------------------------------------------


def read_cpt(file_path=None):
    # Adapted from James Boyle's script
    # https://scipy-cookbook.readthedocs.io/items/Matplotlib_Loading_a_colormap_dynamically.html
    try:
        f = open(file_path)
    except:
        print("File not found: '{}'".format(file_path))
        return None

    lines = f.readlines()
    f.close()

    rgb = []
    color_model = "RGB"
    last_color = None

    for l in lines:
        ls = l.split()
        if not ls:
            continue
        if l[0] == "#":
            if ls[-1] == "HSV":
                color_model = "HSV"
                continue
            else:
                continue
        if ls[0] == "B" or ls[0] == "F" or ls[0] == "N":
            pass
        else:

            color1 = (float(ls[1]),
                      float(ls[2]),
                      float(ls[3]))

            if color1 != last_color:
                rgb.append(color1)
                last_color = color1

            color2 = (float(ls[5]),
                      float(ls[6]),
                      float(ls[7]))

            if color2 != last_color:
                rgb.append(color2)
                last_color = color2

    if color_model == "HSV":
        for i in range(len(rgb)):
            color = rgb[i]
            rr, gg, bb = colorsys.hsv_to_rgb(color[0]/360, color[1], color[2])
            rgb[i] = (rr, gg, bb)

    elif color_model == "RGB":
        for i in range(len(rgb)):
            rgb[i] = rgb[i][0] / 255, rgb[i][1] / 255, rgb[i][2] / 255

    return rgb


# ---------------------------------------------------------------------------------
# ICONS GENERATION
# ---------------------------------------------------------------------------------


def create_image(path):
    colors = read_cpt(path)
    if not colors:
        print("error")
        return
    height = 32
    width = len(colors)
    img = Image.new('RGB', (width, height))

    pixels = []
    for i in range(height):
        for j in range(len(colors)):
            pixels.append((
                int(colors[j][0]*255),
                int(colors[j][1]*255),
                int(colors[j][2]*255)
            ))

    img.putdata(pixels)
    img = img.resize((32, 32))
    img.save(path.replace(".cpt", ".png"))


for dir_name in os.listdir("."):
    if os.path.isdir(os.path.join(".", dir_name)):
        for file_name in os.listdir("./"+dir_name):
            if file_name.endswith(".cpt"):
                create_image(dir_name+"/"+file_name)
