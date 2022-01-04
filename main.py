from PIL import Image

'''
names = ["szyfr_1", "szyfr_2", "szyfr_3"]

for img_name in names:
    colors = []
    im = Image.open(f"Szyfr\\{img_name}.png")
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


    rgb_img.save(f'decoded-{img_name}.png', "PNG")
    print(f"Finished {img_name}")

print('finished')
'''


with open('./Szyfr/w_pustyni_i_w_puszczy.txt', encoding='utf-8') as f:
    mask = [5, 6, 6, 6, 6, 1, 10]
    #mask = [5, 10, 6, 1, 11, 6, 6, 8, 3, 8, 5]
    #mask = [8, 9, 8, 2, 3, 6]

    words = f.read().replace('\n', '').split(' ')
    lengths = list(map(lambda x : len(x), words))

    idx = [x for x in range(len(lengths)) if lengths[x:x+len(mask)] == mask]

    print(idx)
    if len(idx) > 0:
        print(words[idx[0]:idx[0] + len(mask)])


print('finished')



