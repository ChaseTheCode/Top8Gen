from PIL import Image, ImageFont, ImageDraw
from os.path import exists

# bg size 1920 x 1080
bg = Image.open('resources/events/NB/background.png')
fg = Image.open('resources/events/NB/numbers.png')
cboxes = Image.open('resources/events/NB/playerboxes.png')
nameplates = Image.open('resources/events/NB/nameplates.png')
sponsor_big = Image.open('resources/events/NB/sponsor_big.png')
sponsor_med = Image.open('resources/events/NB/sponsor_med.png')
sponsor_sml = Image.open('resources/events/NB/sponsor_sml.png')
secondary_box_big = Image.open('resources/events/NB/secondary_large.png')
secondary_box_med = Image.open('resources/events/NB/secondary_med.png')
secondary_box_sml = Image.open('resources/events/NB/secondary_small.png')




# cat 1 box 600 x 75
# cat 2 box 322 x 40
# cat 3 box 238 x 29

nboxW, nboxH = 600, 100

bboxW, bboxH = 1300, 250

spnsW, spnsH = 100, 50

sponsorsize = (80, 25)

fnt = ImageFont.truetype('resources/events/NB/font.ttf', 1)

def create_namebox(namebox, fawnt, name, vOffset=0, color=(255, 255, 255, 255) ):
    draw = ImageDraw.Draw(namebox)
    nameW, nameH = draw.textsize(name, fawnt)
    position = ((nboxW-nameW)/2,vOffset)
    draw.text(position, name, color, font=fawnt)

    return namebox

def create_blurb_box(blurb_box, fawnt, name, vOffset=0, color=(255, 255, 255, 255) ):
    draw = ImageDraw.Draw(blurb_box)
    blurbW, blurbH = draw.textsize(name, fawnt)
    position = (0,vOffset)
    draw.text(position, name, color, font=fawnt, anchor="lt")

    return blurb_box

def create_sponsorbox(sponsorbox, fawnt, name, vOffset=0, color=(255, 255, 255, 255) ):
    draw = ImageDraw.Draw(sponsorbox)
    spnsW, spnsH = draw.textsize(name, fawnt)
    position = ((spnsW-spnsW)/2,vOffset)
    draw.text(position, name, color, font=fawnt)

    return sponsorbox

# 1st  w 600 x h 647

# port size w 654 x h 706
# icon size 64 x 64

first_portrait = Image.open('resources/characters/GGST/portraits/purple.png')

first_portrait = first_portrait.resize((600, 647), Image.Resampling.LANCZOS)

# open if
first_secondary_box = Image.open('resources/events/NB/secondary_large.png')
first_secondary_1 = Image.open('resources/characters/GGST/icons/purple.png')
first_secondary_1 = first_secondary_1.resize((64,64), Image.Resampling.LANCZOS)
first_portrait.paste(first_secondary_1, (528, 8), first_secondary_1)
# close if

# open if
first_secondary_2 = Image.open('resources/characters/GGST/icons/purple.png')
first_secondary_2 = first_secondary_2.resize((64,64), Image.Resampling.LANCZOS)
first_portrait.paste(first_secondary_2, (456, 8), first_secondary_1)
# close if


# open if sponsor
fnt = ImageFont.truetype('resources/events/NB/font.ttf', 20)
first_portrait.paste(sponsor_med, (197, 276))

# open sponsor text
sponsor1_text = Image.new('RGBA', (spnsW, spnsH))
sponsor1_text = create_sponsorbox(sponsor1_text, fnt, "HHHHH")
first_portrait.paste(sponsor1_text, (250, 277), sponsor1_text)
# close sponsor text

# open sponsor image
sponsor1_image = Image.open('resources/sponsors/TLOC.png')
sponsor1_image.getbbox()
sponsor1_image = sponsor1_image.crop(sponsor1_image.getbbox())
sponsor1_image.thumbnail((80, 22), Image.Resampling.LANCZOS)
first_portrait.paste(sponsor1_image, (205, 279), sponsor1_image)
# close sponsor image

fnt = ImageFont.truetype('resources/events/NB/font.ttf', 55)                                           

namebox1 = Image.new('RGBA', (nboxW, nboxH))
namebox1 = create_namebox(namebox1, fnt, "H")

# 2nd-4th 322 x 348

# second


second_portrait = Image.open('resources/characters/GGST/portraits/steve_07.png')

second_portrait = second_portrait.resize((322, 348), Image.Resampling.LANCZOS)

# open if secondary 1
second_secondary_1 = Image.open('resources/characters/GGST/icons/mario_01.png')
second_secondary_1 = second_secondary_1.resize((48,48), Image.Resampling.LANCZOS)
second_portrait.paste(second_secondary_1, (267, 8), second_secondary_1)
# close if secondary 1

# open if secondary 2
second_secondary_2 = Image.open('resources/characters/GGST/icons/mario_01.png')
second_secondary_2 = second_secondary_2.resize((48,48), Image.Resampling.LANCZOS)
second_portrait.paste(second_secondary_2, (211, 8), second_secondary_2)
# close if secondary 2

# open if sponsor
fnt = ImageFont.truetype('resources/events/NB/font.ttf', 20)
second_portrait.paste(sponsor_med, (197, 276))

# open sponsor text
sponsor2_text = Image.new('RGBA', (spnsW, spnsH))
sponsor2_text = create_sponsorbox(sponsor2_text, fnt, "HHHHH")
second_portrait.paste(sponsor2_text, (250, 277), sponsor2_text)
# close sponsor text

# open sponsor image
sponsor2_image = Image.open('resources/sponsors/TLOC.png')
sponsor2_image.getbbox()
sponsor2_image = sponsor2_image.crop(sponsor2_image.getbbox())
sponsor2_image.thumbnail((80, 22), Image.Resampling.LANCZOS)
second_portrait.paste(sponsor2_image, (205, 279), sponsor2_image)
# close sponsor image

# close if sponsor


fnt = ImageFont.truetype('resources/events/NB/font.ttf', 30)
namebox2 = Image.new('RGBA', (nboxW, nboxH))
namebox2 = create_namebox(namebox2, fnt, "hhhhhhhhhhhhhhhh".upper())

# third

third_portrait = Image.open('resources/characters/GGST/portraits/steve_07.png')

third_portrait = third_portrait.resize((322, 348), Image.Resampling.LANCZOS)

third_secondary_1 = Image.open('resources/characters/GGST/icons/mario_01.png')
third_secondary_1 = third_secondary_1.resize((48,48), Image.Resampling.LANCZOS)
third_portrait.paste(third_secondary_1, (267, 8), third_secondary_1)

third_secondary_2 = Image.open('resources/characters/GGST/icons/mario_01.png')
third_secondary_2 = third_secondary_2.resize((48,48), Image.Resampling.LANCZOS)
third_portrait.paste(third_secondary_2, (211, 8), third_secondary_2)

# open if sponsor
fnt = ImageFont.truetype('resources/events/NB/font.ttf', 20)
third_portrait.paste(sponsor_med, (197, 276))

# open sponsor text
sponsor3_text = Image.new('RGBA', (spnsW, spnsH))
sponsor3_text = create_sponsorbox(sponsor3_text, fnt, "RIVAL")
third_portrait.paste(sponsor3_text, (260, 277), sponsor3_text)
# close sponsor text

# open sponsor image
sponsor3_image = Image.open('resources/sponsors/frks.png')
sponsor3_image.getbbox()
sponsor3_image = sponsor3_image.crop(sponsor3_image.getbbox())
sponsor3_image.thumbnail((80, 22), Image.Resampling.LANCZOS)
third_portrait.paste(sponsor3_image, (215, 280), sponsor3_image)
# close sponsor image

# close if sponsor

fnt = ImageFont.truetype('resources/events/NB/font.ttf', 30)
namebox3 = Image.new('RGBA', (nboxW, nboxH))
namebox3 = create_namebox(namebox3, fnt, "hhhhhhhhhhhhhhhh".upper())

# fourth

fourth_portrait = Image.open('resources/characters/GGST/portraits/steve_07.png')

fourth_portrait = fourth_portrait.resize((322, 348), Image.Resampling.LANCZOS)

fourth_secondary_1 = Image.open('resources/characters/GGST/icons/mario_01.png')
fourth_secondary_1 = fourth_secondary_1.resize((48,48), Image.Resampling.LANCZOS)
fourth_portrait.paste(fourth_secondary_1, (267, 8), fourth_secondary_1)

fourth_secondary_2 = Image.open('resources/characters/GGST/icons/mario_01.png')
fourth_secondary_2 = fourth_secondary_2.resize((48,48), Image.Resampling.LANCZOS)
fourth_portrait.paste(fourth_secondary_2, (211, 8), fourth_secondary_2)

# open if sponsor
fnt = ImageFont.truetype('resources/events/NB/font.ttf', 20)
fourth_portrait.paste(sponsor_med, (197, 276))

# open sponsor text
sponsor4_text = Image.new('RGBA', (spnsW, spnsH))
sponsor4_text = create_sponsorbox(sponsor4_text, fnt, "RIVAL")
fourth_portrait.paste(sponsor4_text, (260, 277), sponsor4_text)
# close sponsor text

# open sponsor image
sponsor4_image = Image.open('resources/sponsors/frks.png')
sponsor4_image.getbbox()
sponsor4_image = sponsor4_image.crop(sponsor4_image.getbbox())
sponsor4_image.thumbnail((80, 22), Image.Resampling.LANCZOS)
fourth_portrait.paste(sponsor4_image, (215, 280), sponsor4_image)
# close sponsor image

# close if sponsor

fnt = ImageFont.truetype('resources/events/NB/font.ttf', 30)
namebox4 = Image.new('RGBA', (nboxW, nboxH))
namebox4 = create_namebox(namebox4, fnt, "hhhhhhhhhhhhhhhh".upper())

# fifth

# 238 x 257

fifth_portrait = Image.open('resources/characters/GGST/portraits/lucina_03.png')

fifth_portrait = fifth_portrait.resize((238, 257), Image.Resampling.LANCZOS)

fifth_secondary_1 = Image.open('resources/characters/GGST/icons/mario_02.png')
fifth_secondary_1 = fifth_secondary_1.resize((32,32), Image.Resampling.LANCZOS)
fifth_portrait.paste(fifth_secondary_1, (202, 4), fifth_secondary_1)

fifth_secondary_2 = Image.open('resources/characters/GGST/icons/mario_02.png')
fifth_secondary_2 = fifth_secondary_2.resize((32,32), Image.Resampling.LANCZOS)
fifth_portrait.paste(fifth_secondary_2, (166, 4), fifth_secondary_2)

# open if sponsor
fnt = ImageFont.truetype('resources/events/NB/font.ttf', 13)
fifth_portrait.paste(sponsor_sml, (144, 204))

# open sponsor text
sponsor5_text = Image.new('RGBA', (spnsW, spnsH))
sponsor5_text = create_sponsorbox(sponsor5_text, fnt, "HHHHH")
fifth_portrait.paste(sponsor5_text, (188, 207), sponsor5_text)
# close sponsor text

# open sponsor image
sponsor5_image = Image.open('resources/sponsors/frks.png')
sponsor5_image.getbbox()
sponsor5_image = sponsor5_image.crop(sponsor5_image.getbbox())
sponsor5_image.thumbnail((80, 15), Image.Resampling.LANCZOS)
fifth_portrait.paste(sponsor5_image, (155, 206), sponsor5_image)
# close sponsor image

# close if sponsor

fnt = ImageFont.truetype('resources/events/NB/font.ttf', 21)
namebox5 = Image.new('RGBA', (nboxW, nboxH))
namebox5 = create_namebox(namebox5, fnt, "hhhhhhhhhhhhhhhh".upper())



# sixth

sixth_portrait = Image.open('resources/characters/GGST/portraits/lucina_03.png')

sixth_portrait = sixth_portrait.resize((238, 257), Image.Resampling.LANCZOS)

sixth_secondary_1 = Image.open('resources/characters/GGST/icons/mario_02.png')
sixth_secondary_1 = sixth_secondary_1.resize((32,32), Image.Resampling.LANCZOS)
sixth_portrait.paste(sixth_secondary_1, (202, 4), sixth_secondary_1)

sixth_secondary_2 = Image.open('resources/characters/GGST/icons/mario_02.png')
sixth_secondary_2 = sixth_secondary_2.resize((32,32), Image.Resampling.LANCZOS)
sixth_portrait.paste(sixth_secondary_2, (166, 4), sixth_secondary_2)

# open if sponsor
fnt = ImageFont.truetype('resources/events/NB/font.ttf', 15)
sixth_portrait.paste(sponsor_sml, (144, 204))

# open sponsor text
sponsor6_text = Image.new('RGBA', (spnsW, spnsH))
sponsor6_text = create_sponsorbox(sponsor6_text, fnt, "RIVAL")
sixth_portrait.paste(sponsor6_text, (190, 205), sponsor6_text)
# close sponsor text

# open sponsor image
sponsor6_image = Image.open('resources/sponsors/frks.png')
sponsor6_image.getbbox()
sponsor6_image = sponsor6_image.crop(sponsor6_image.getbbox())
sponsor6_image.thumbnail((80, 15), Image.Resampling.LANCZOS)
sixth_portrait.paste(sponsor6_image, (155, 206), sponsor6_image)
# close sponsor image

# close if sponsor

fnt = ImageFont.truetype('resources/events/NB/font.ttf', 21)
namebox6 = Image.new('RGBA', (nboxW, nboxH))
namebox6 = create_namebox(namebox6, fnt, "hhhhhhhhhhhhhhhh".upper())

# seventh

seventh_portrait = Image.open('resources/characters/GGST/portraits/lucina_03.png')

seventh_portrait = seventh_portrait.resize((238, 257), Image.Resampling.LANCZOS)

seventh_secondary_1 = Image.open('resources/characters/GGST/icons/mario_02.png')
seventh_secondary_1 = seventh_secondary_1.resize((32,32), Image.Resampling.LANCZOS)
seventh_portrait.paste(seventh_secondary_1, (202, 4), seventh_secondary_1)

seventh_secondary_2 = Image.open('resources/characters/GGST/icons/mario_02.png')
seventh_secondary_2 = seventh_secondary_2.resize((32,32), Image.Resampling.LANCZOS)
seventh_portrait.paste(seventh_secondary_2, (166, 4), seventh_secondary_2)

# open if sponsor
fnt = ImageFont.truetype('resources/events/NB/font.ttf', 15)
seventh_portrait.paste(sponsor_sml, (144, 204))

# open sponsor text
sponsor7_text = Image.new('RGBA', (spnsW, spnsH))
sponsor7_text = create_sponsorbox(sponsor7_text, fnt, "RIVAL")
seventh_portrait.paste(sponsor7_text, (190, 205), sponsor7_text)
# close sponsor text

# open sponsor image
sponsor7_image = Image.open('resources/sponsors/frks.png')
sponsor7_image.getbbox()
sponsor7_image = sponsor7_image.crop(sponsor7_image.getbbox())
sponsor7_image.thumbnail((80, 15), Image.Resampling.LANCZOS)
seventh_portrait.paste(sponsor7_image, (155, 206), sponsor7_image)
# close sponsor image

# close if sponsor

fnt = ImageFont.truetype('resources/events/NB/font.ttf', 21)
namebox7 = Image.new('RGBA', (nboxW, nboxH))
namebox7 = create_namebox(namebox7, fnt, "hhhhhhhhhhhhhhhh".upper())

# eighth

eighth_portrait = Image.open('resources/characters/GGST/portraits/lucina_03.png')

eighth_portrait = eighth_portrait.resize((238, 257), Image.Resampling.LANCZOS)

eighth_secondary_1 = Image.open('resources/characters/GGST/icons/purple.png')
eighth_secondary_1 = eighth_secondary_1.resize((32,32), Image.Resampling.LANCZOS)
eighth_portrait.paste(eighth_secondary_1, (202, 4), eighth_secondary_1)

eighth_secondary_2 = Image.open('resources/characters/GGST/icons/mario_02.png')
eighth_secondary_2 = eighth_secondary_2.resize((32,32), Image.Resampling.LANCZOS)
eighth_portrait.paste(eighth_secondary_2, (166, 4), eighth_secondary_2)

# open if sponsor
fnt = ImageFont.truetype('resources/events/NB/font.ttf', 15)
eighth_portrait.paste(sponsor_sml, (144, 204))

# open sponsor text
sponsor8_text = Image.new('RGBA', (spnsW, spnsH))
sponsor8_text = create_sponsorbox(sponsor8_text, fnt, "RIVAL")
eighth_portrait.paste(sponsor8_text, (190, 205), sponsor8_text)
# close sponsor text

# open sponsor image
sponsor8_image = Image.open('resources/sponsors/frks.png')
sponsor8_image.getbbox()
sponsor8_image = sponsor8_image.crop(sponsor8_image.getbbox())
sponsor8_image.thumbnail((80, 15), Image.Resampling.LANCZOS)
eighth_portrait.paste(sponsor8_image, (155, 206), sponsor8_image)
# close sponsor image

# close if sponsor

fnt = ImageFont.truetype('resources/events/NB/font.ttf', 21)
namebox8 = Image.new('RGBA', (nboxW, nboxH))
namebox8 = create_namebox(namebox8, fnt, "hhhhhhhhhhhhhhhh".upper())

# top bar information

fnt = ImageFont.truetype('resources/events/NB/font.ttf', 33)

namebox_date = Image.new('RGBA', (nboxW, nboxH))
namebox_date = create_namebox(namebox_date, fnt, "march 31, 2022".upper())

namebox_slug = Image.new('RGBA', (nboxW, nboxH))
namebox_slug = create_namebox(namebox_slug, fnt, "start.gg/NB129".upper())

fnt = ImageFont.truetype('resources/events/NB/font.ttf', 43)

namebox_entrants = Image.new('RGBA', (nboxW, nboxH))
namebox_entrants = create_namebox(namebox_entrants, fnt, "256 entrants".upper())

# blurb time

fnt = ImageFont.truetype('resources/events/NB/font.ttf', 35)

blurb_box_1 = Image.new('RGBA', (bboxW, bboxH))
blurb_box_1 = create_blurb_box(blurb_box_1, fnt, "don't forget to register for DFW's Bizzare Adventure,".upper())

blurb_box_2 = Image.new('RGBA', (bboxW, bboxH))
blurb_box_2 = create_blurb_box(blurb_box_2, fnt, "powered by the Liberty Rec Center in Plano, TX! Sign up today!".upper())

blurb_box_3 = Image.new('RGBA', (bboxW, bboxH))
blurb_box_3 = create_blurb_box(blurb_box_3, fnt, "DFWba will feature Singles, 3v3 Squad Strike, and Doubles!".upper())

# pasties!

bg.paste(cboxes, (0,0), cboxes)

bg.paste(first_portrait, (156, 205), first_portrait)
bg.paste(second_portrait, (771, 205), second_portrait)
bg.paste(third_portrait, (1106, 205), third_portrait)
bg.paste(fourth_portrait, (1441, 205), fourth_portrait)
bg.paste(fifth_portrait, (770, 596), fifth_portrait)
bg.paste(sixth_portrait, (1022, 596), sixth_portrait)
bg.paste(seventh_portrait, (1274, 596), seventh_portrait)
bg.paste(eighth_portrait, (1526, 596), eighth_portrait)

bg.paste(nameplates, (0,0), nameplates)

bg.paste(namebox1, (156, 783), namebox1)

bg.paste(namebox2, (631, 516), namebox2)
bg.paste(namebox3, (967, 516), namebox3)
bg.paste(namebox4, (1302, 516), namebox4)
bg.paste(namebox5, (588, 825), namebox5)
bg.paste(namebox6, (840, 825), namebox6)
bg.paste(namebox7, (1092, 825), namebox7)
bg.paste(namebox8, (1344, 825), namebox8)

bg.paste(namebox_date, (252, 61), namebox_date)
bg.paste(namebox_slug, (1080, 61), namebox_slug)
bg.paste(namebox_entrants, (660, 50), namebox_entrants)

bg.paste(blurb_box_1, (40, 949), blurb_box_1)
bg.paste(blurb_box_2, (40, 983), blurb_box_2)
bg.paste(blurb_box_3, (40, 1017), blurb_box_3)

bg.paste(fg, (0,0), fg)
bg.save('test_image.png')