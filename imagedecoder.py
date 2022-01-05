from PIL import Image


def decode_image(path, name):
    colors = []

    im = Image.open(path)
    rgb_img = im.convert('RGB')
    pixels = rgb_img.load()
    for width in range(im.size[0]):
        for height in range(im.size[1]):
            rgb = rgb_img.getpixel((width, height))
            append = True

            if (rgb not in colors):
                for color in colors:
                    if abs(rgb[0] - color[0]) + abs(rgb[1] - color[1]) + abs(rgb[2] - color[2]) < 5:
                        pixels[width, height] = (255, 255, 255)
                        append = False

                if append:
                    colors.append(rgb)

            else:
                pixels[width, height] = (0, 0, 0)
    rgb_img.save(f'decoded-{name}.png', "PNG")

    print(f"Finished {name}")
