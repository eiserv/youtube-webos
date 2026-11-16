"""Generate the fork's geometric play icon. No external images or fonts."""
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parents[1] / 'assets'

def icon(size):
    scale = 4
    side = size * scale
    image = Image.new('RGB', (side, side))
    px = image.load()
    for y in range(side):
        for x in range(side):
            t = (x + y) / (2 * side)
            px[x, y] = tuple(round(a * (1 - t) + b * t) for a, b in zip((76, 105, 137), (21, 29, 47)))
    draw = ImageDraw.Draw(image, 'RGBA')
    draw.rounded_rectangle((side*.12, side*.21, side*.88, side*.79), radius=side*.16,
                           fill=(236, 245, 255, 35), outline=(236, 245, 255, 150), width=max(1, side//95))
    draw.polygon([(side*.43, side*.34), (side*.43, side*.66), (side*.69, side*.50)], fill=(247, 250, 255, 255))
    return image.resize((size, size), Image.Resampling.LANCZOS)

for name, size in [('icon',80), ('largeIcon',130), ('mediumLargeIcon',115), ('extraLargeIcon',192), ('playIcon',80)]:
    icon(size).save(OUT / (name + '.png'))
