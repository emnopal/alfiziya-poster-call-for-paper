import time
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


def poster_generator(volume, no, due_date, due_month, due_year) -> BytesIO:
    image = Image.open('server_side.png')
    draw = ImageDraw.Draw(image)

    fonts = 'font/Montserrat-Bold.ttf'
    fonts_italic = 'font/Montserrat-BoldItalic.ttf'

    text_volume = f'Volume {volume} No. {no}'
    if int(text_volume.split()[1]) < 10:
        if text_volume.split()[3] == 'I':
            font = ImageFont.truetype(fonts, 93)
            draw.text((602, 1089), text_volume, (255, 255, 255), font=font)
        else:
            font = ImageFont.truetype(fonts, 88)
            draw.text((604, 1091), text_volume, (255, 255, 255), font=font)
    else:
        if int(text_volume.split()[1]) == 11:
            if text_volume.split()[3] == 'I':
                font = ImageFont.truetype(fonts, 90)
                draw.text((606, 1091), text_volume, (255, 255, 255), font=font)
            else:
                font = ImageFont.truetype(fonts, 88)
                draw.text((602, 1091), text_volume, (255, 255, 255), font=font)
        elif int(text_volume.split()[1]) == 10 or int(text_volume.split()[1]) > 11 and int(text_volume.split()[1]) < 20:
            if text_volume.split()[3] == 'I':
                font = ImageFont.truetype(fonts, 88)
                draw.text((603, 1091), text_volume, (255, 255, 255), font=font)
            else:
                font = ImageFont.truetype(fonts, 85)
                draw.text((600, 1091), text_volume, (255, 255, 255), font=font)
        else:
            if text_volume.split()[3] == 'I':
                font = ImageFont.truetype(fonts, 85)
                draw.text((603, 1091), text_volume, (255, 255, 255), font=font)
            else:
                font = ImageFont.truetype(fonts, 83)
                draw.text((600, 1091), text_volume, (255, 255, 255), font=font)

    text_due_date = f'{due_date} {due_month} {due_year}'
    if len(text_due_date.split()[0]) < 2:
        text_due_date = "0" + text_due_date
    else:
        text_due_date = text_due_date

    if len(text_due_date.split()[1]) == 3:
        font = ImageFont.truetype(fonts_italic, 80)
        draw.text((690, 1728), text_due_date, (255, 255, 255), font=font)
    elif len(text_due_date.split()[1]) == 4:
        font = ImageFont.truetype(fonts_italic, 80)
        draw.text((685, 1728), text_due_date, (255, 255, 255), font=font)
    elif len(text_due_date.split()[1]) == 5:
        font = ImageFont.truetype(fonts_italic, 80)
        draw.text((683, 1728), text_due_date, (255, 255, 255), font=font)
    elif len(text_due_date.split()[1]) == 6:
        font = ImageFont.truetype(fonts_italic, 80)
        draw.text((640, 1728), text_due_date, (255, 255, 255), font=font)
    elif len(text_due_date.split()[1]) == 7:
        font = ImageFont.truetype(fonts_italic, 80)
        draw.text((630, 1728), text_due_date, (255, 255, 255), font=font)
    elif len(text_due_date.split()[1]) == 8:
        font = ImageFont.truetype(fonts_italic, 80)
        draw.text((570, 1728), text_due_date, (255, 255, 255), font=font)
    elif len(text_due_date.split()[1]) == 9:
        font = ImageFont.truetype(fonts_italic, 80)
        draw.text((550, 1728), text_due_date, (255, 255, 255), font=font)

    bytes = BytesIO()

    # image.save(f'output/server_side_{time.time()}.png', optimize=True, quality=100)
    image.save(bytes, 'png', optimize=True, quality=100)
    bytes.seek(0)

    return bytes
