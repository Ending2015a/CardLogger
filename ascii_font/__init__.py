import re
import os
import sys
import time
import logging

from collections import deque

import subprocess

from .base import AsciiFont

DEFAULT_FLF_PATH = './flf'
DEFAULT_FLF_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 
        DEFAULT_FLF_PATH)
# absolute path

FONT_TYPE_LIST = {}


def load_font_type_list(installed_path=DEFAULT_FLF_PATH):
    
    for flf in os.listdir(installed_path):
        
        if not flf.endswith('.flf'):
            continue

        flf_path = os.path.join(installed_path, flf)
        flf_name, _ = os.path.splitext(flf)
        for rep in [' ', '/', '\\', '-']:
            flf_name = flf_name.replace(rep, '_')

        FONT_TYPE_LIST[flf_name] = {'path': flf_path, 'module': None}


        

def install_font_type(name, flf_path):

    flf_name = name
    for rep in [' ', '/', '\\', '-']:
        flf_name = flf_name.replace(rep, '_')

    if flf_name in FONT_TYPE_LIST:
        print('Font type \'{}\' is already installed'.format(flf_name))

    if not os.path.isfile(flf_path):
        raise Exception('Path \'{}\' does not exist'.format(flf_path))

    FONT_TYPE_LIST[flf_name] = {'path':flf_path, 'module': None}


def load(font_type):

    flf_path = FONT_TYPE_LIST[font_type]['path']


    HEADER = 'flf2a'
    
    line_end = ['#', '@', chr(127)]
    font_end = ['##', '@@', chr(127)*2]

    charset_pattern = r'.*charset=(.*)$'
    matcher = re.compile(charset_pattern)

    out = subprocess.check_output('file -i "{}"'.format(flf_path), shell=True).decode('utf-8')

    match = matcher.match(out)

    if match is not None:
        charset = match.group(1).strip()
    else:
        charset = 'utf-8'

    if charset == 'binary':
        print('Detect binary encoding')
        charset = 'iso-8859-1'

    with open(flf_path, 'r', encoding=charset) as inpf:

        header = inpf.readline()
        magic_number = header.split(' ')

        assert magic_number[0].startswith(HEADER), 'Got an unexpected header: {}'.format(magic_number[0])


        hardblank = magic_number[0].replace(HEADER, '')
        ch_height = int(magic_number[1])

        # create read buffer
        read_buf = deque(maxlen=ch_height)

        font = AsciiFont(hardblank)

        current_ascii = 32
        stop_ascii = 127

        for line in inpf:
            line = line.replace('\n', '').rstrip()

            if not line:
                continue

            
            if not (line[-1] in line_end):
                pass
            else:
                # font end
                if not ((line[-2:] in font_end) and (len(read_buf) == read_buf.maxlen-1)):

                    #if (not (line[-2:]) in font_end):

                    end = line[-1]
                    line = line.replace(end, '\n')

                    read_buf.append(line)

                else:

                    end = line[-2:]
                    line = line.replace(end, '')

                    read_buf.append(line)

                    char = chr(current_ascii)

                    # concat to one string ('\n')
                    font[char] = ''.join(read_buf)

                    current_ascii += 1

                    read_buf.clear()

            if current_ascii == stop_ascii:
                break
    
    FONT_TYPE_LIST[font_type]['module'] = font
    
    return font

def retrieves(font_type, chars):
    if font_type in FONT_TYPE_LIST:
        if FONT_TYPE_LIST[font_type]['module'] is not None:
            font_type = FONT_TYPE_LIST[font_type]['module']
        else:
            font_type = load(font_type)
    else:
        raise Exception('Font type \'{}\' is not installed'.format(font_type))

    type_chars = []

    for c in chars:
        type_char = font_type.retrieve(c)

        type_chars.append(type_char)


    return type_chars


load_font_type_list()
