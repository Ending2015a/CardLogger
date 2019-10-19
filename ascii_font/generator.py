import re
import os
import sys
import time
import logging

from collections import deque

import subprocess


TEXT_FLF = 'Rectangles.flf'

HEADER = 'flf2a'

LINE_END = ['#', '@', chr(127)]
FONT_END = ['##', '@@', chr(127)*2]

CHARSET_PATTERN = r'.*charset=(.*)$'
matcher = re.compile(CHARSET_PATTERN)

def generate(input_filename, output_filename, object_name):

    out = subprocess.check_output('file -i "{}"'.format(input_filename), shell=True).decode('utf-8')


    match = matcher.match(out)

    if match is not None:
        charset = match.group(1).strip()
    else:
        charset = 'utf-8'

    if charset == 'binary':
        print('Detect binary encoding')
        charset = 'iso-8859-1'

    print('    Using charactor set: {}'.format(charset))
    with open(input_filename, 'r', encoding=charset) as inpf, open(output_filename, 'w') as outf:
        header = inpf.readline()
        magic_number = header.split(' ')

        assert magic_number[0].startswith(HEADER), 'Got an unexpected header: {}'.format(magic_number[0])

        hardblank = magic_number[0].replace(HEADER, '')
        ch_height = int(magic_number[1])

        # create read buffer
        read_buf = deque(maxlen=ch_height)
        
        # create output file header
        outf.write(\
"""

if not '.' in __name__:
    package_name = '__main__'
else:
    package_name = __name__.rsplit(".", 1)[0]

if package_name == "__main__":
    module_name = 'base'
else:
    module_name = package_name + '.' + 'base'

module = __import__(module_name, fromlist=['.'])
AsciiFont = getattr(module, 'AsciiFont')


"""     )
        
        outf.write('{} = AsciiFont("{}")\n'.format(object_name, hardblank))
        
        outf.write('# {}\n\n'.format(header))

        # start from 32 (space)
        current_ascii = 32
        stop_ascii = 127

        for line in inpf:
            # remove newlines
            line = line.replace('\n', '').rstrip()

            #print('line: {}/line end: {}'.format(line, line[-1]))

            if not line:
                continue

            # write comments
            if not (line[-1] in LINE_END):
                outf.write('# {}\n'.format(line))
            else:

                # replace hardblank to normal space
                #line = line.replace(hardblank, ' ')
                
                # if not font end
                if not (line[-2:] in FONT_END):

                    # replace line end to new line
                    for line_end in LINE_END:
                        line = line.replace(line_end, '\n')

                    # append to read_buf
                    read_buf.append(line)

                # font end
                else:

                    # remove font end
                    for font_end in FONT_END:
                        line = line.replace(font_end, '')

                    # append to buf
                    read_buf.append(line)

                    char = chr(current_ascii)

                    if char == '"':
                        char = '\\"'
                    elif char == '\\':
                        char = '\\\\'


                    outf.write('{}["{}"] = (\n'.format(object_name, char))
                    for buf in read_buf:
                        # convert all escape to literal
                        buf = buf.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
                        outf.write('"{}"\n'.format(buf))

                    outf.write(')\n\n')

                    current_ascii += 1
                    
            if current_ascii == stop_ascii:
                break

    return True


if __name__ == '__main__':

    assert len(sys.argv) >= 2, 'python generator.py [flf files]'

    for argv in sys.argv[1:]:

        input_filename = str(argv)

        basename = os.path.basename(input_filename)

        object_name, ext = basename.split('.')

        # convert to valid name
        for rep in [' ', '/', '\\', '-']:
            object_name = object_name.replace(rep, '_')
        
        output_filename = object_name + '.py'

        print('Generating file "{}" from "{}"'.format(output_filename, input_filename))

        try:
            generate(input_filename, output_filename, object_name)
        except Exception as e:
            print('    Failed to generate file: {}'.format(str(e)))
            continue

        print('    test loadability:')

        try:
            if not os.path.isfile(object_name):
                time.sleep(0.1)

            module = __import__(object_name, fromlist=['.'])
            obj = getattr(module, object_name)
            print('        Clear')
        except:
            print('        Failed')
            raise
