from PIL import Image, ImageDraw

for f in ['tracked.png', 'skipped.png', 'untracked.png']:
    img = Image.new('RGBA', (32, 32))
    drw = ImageDraw.Draw(img, 'RGBA')
    drw.polygon([(0, 0), (0, 31), (31, 31), (31, 0)], (0, 0, 0, 0))
    drw.chord((7, 7, 23, 23), 0, 360, (255, 255, 255, 255), (255, 255, 255, 200))
    del drw

    img.save(f, 'PNG')