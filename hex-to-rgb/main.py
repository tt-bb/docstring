def convertir_hex_en_rgb(hexadecimal: str) -> tuple:
    """
    La fonction convertit une couleur en hexadécimal
    vers le format rgb
    :param hexadecimal: la couleur au format #FFFFFF
    :return: rgb: la couleur au format (255, 255, 255)
    """
    red = hexadecimal[1:3]
    green = hexadecimal[3:5]
    blue = hexadecimal[5:]
    rgb = (int(red, 16), int(green, 16), int(blue, 16))
    return rgb


# TEST
print(convertir_hex_en_rgb("#FFFFFF"))
