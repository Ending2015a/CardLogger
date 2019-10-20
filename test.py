import ascii_font

ascii_font.load_font_type_list()

font_types = list(ascii_font.FONT_TYPE_LIST.keys())

print(font_types)

for font_type in font_types:

    print('loading font type: {}'.format(font_type))
    font = ascii_font.load(font_type)

    for c in ['a', 'b', 'c', ' ', '!']:
        
        print(font.retrieve(c))
