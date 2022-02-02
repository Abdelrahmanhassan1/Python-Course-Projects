import colorgram


def extract_color(image):
    colors_from_image = colorgram.extract(image, 10)
    # print(colors_from_image)
    rgb_colors = []
    for color in colors_from_image:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        # note we need the color to be in a tuple format
        rgb_colors.append((red, green, blue))
    return rgb_colors


# print(extract_color('hist_spot_painting.jpg'))
