import sys
from PIL import Image, ImageDraw

def remove_transparency(im, bg_colour=(255, 255, 255)):

    # Only process if image has transparency (http://stackoverflow.com/a/1963146)
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):

        # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
        alpha = im.convert('RGBA').split()[-1]

        # Create a new background image of our matt color.
        # Must be RGBA because paste requires both images have the same format
        # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im


def gen_tupper_k(img):
    img = remove_transparency(img)
    pix=img.load()
    binary = ""
    # bit order uses cartesian coords, so count backward
    for x in reversed(range(0, 106)):
        for y in range(0, 17):
            binary+= "1" if (pix[x, y][0]<245 or pix[x, y][1]<245 or pix[x, y][2]<245) else "0"

    return (int(binary, 2)*17) # multiply final result by 17

def text_to_k(text):
    img = Image.new('RGB', (106, 17), color = 'white')
    d = ImageDraw.Draw(img)
    d.text((0,0), text, fill=(0,0,0))
    return gen_tupper_k(img)

def k_to_wolf(k):
    return "plot 0.5 < floor((2^((-17 floor(x) - floor(y)) mod 17) floor(y/17)) mod 2), x=0..17, y=" + str(k) +".." + str(k+17) 

print(gen_tupper_k(Image.open("keren.png")))
print("    ")
print(k_to_wolf(text_to_k("Poop")))