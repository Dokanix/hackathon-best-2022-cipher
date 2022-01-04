from PIL import Image

def get_letter_size(path):
    im = Image.open(path)
    rgb_img = im.convert('RGB')

    y_values = [0] * im.size[1]

    pixels = rgb_img.load()

    for width in range(im.size[0]):
        for height in range(im.size[1]):
            rgb = rgb_img.getpixel((width, height))

            if rgb == (255, 255, 255):
                y_values[height] += 1

    heights = [0]
    counter = 0

    for val in y_values:
        if val > 0:
            heights[counter] += 1
        elif heights[counter] != 0:
            heights.append(0)
            counter += 1

    height = max(heights)
    width = round(height / 1.6)

    return (width, height)
