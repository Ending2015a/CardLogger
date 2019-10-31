import os
import sys
import time
import string
import logging


MODULE_PATH = __name__.rsplit('.', 1)[0]
c_module = __import__(MODULE_PATH+'.cmd_colors', fromlist=['.'])
C = getattr(c_module, 'Color')


font_module = __import__(MODULE_PATH+'.ascii_font.__init__', fromlist=['.'])
ascii_font = font_module #getattr(font_module, 'ascii_font')

#from sshex.logger.cmd_colors import Color as C


def format_color_message(message, code_map, color_fmt):
    for code in code_map:
        message = message.replace(code, color_fmt.format(code_map[code]))
    return message


class ColoredFormatter(logging.Formatter):
 
    LEVEL_COLORS = {
        'WARNING': C.BOLD + C.dark(C.YELLOW),
        'INFO': C.BOLD + C.GREEN,
        'ERROR': C.BOLD + C.dark(C.RED),
        'DEBUG': C.BOLD + C.dark(C.BLUE),
        'CRITICAL': C.BOLD + C.RED
    }

    LEVEL_LABEL = {
        'WARNING': 'WARN',
        'INFO': 'INFO',
        'ERROR': 'ERRO',
        'DEBUG': 'DEBU',
        'CRITICAL': 'ERRO'
    }

    CODES = {
        '$TIME': C.dark(C.GREEN),
        '$THREAD': C.light(C.BLACK),
        '$MODULE': C.dark(C.CYAN),
        '$BOLD': C.BOLD,
        '$UNBOLD': C.reset(C.BOLD),
        '$BLINK': C.BLINK,
        '$RESET': C.reset(),
    }

    COLOR_FMT = '\033[{}m'

    def __init__(self, fmt=None, datefmt=None, style='%'):

        if fmt is not None:
            fmt = format_color_message(fmt, self.CODES, self.COLOR_FMT)

        super(ColoredFormatter, self).__init__(fmt, datefmt, style)


    def getLevelColor(self, record):
        return self.LEVEL_COLORS[record.levelname]


    def format(self, record):
        # get $LEVEL color
        levelcolor = self.getLevelColor(record)

        

        # set level label
        original_levelname = record.levelname
        record.levelname = self.LEVEL_LABEL[record.levelname]

    
        # === formatting ===
        record.message = record.getMessage()
        # asctime
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        
        # message
        s = self.formatMessage(record)

        # exception
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)

        if record.exc_text:
            if s[-1:] != '\n':
                s = s + '\n'
            s = s + '$EXCEPT' + record.exc_text + '$RESET'
        if record.stack_info:
            if s[-1:] != '\n':
                s = s + '\n'
            s = s + '$EXCEPT' + self.formatStack(record.stack_info) + '$RESET'

        self.CODES['$EXCEPT'] = self.LEVEL_COLORS['ERROR']
        self.CODES['$LEVEL'] = levelcolor

        s = format_color_message(s, self.CODES, self.COLOR_FMT)


        record.levelname = original_levelname

        return s


def _recursive_format(value, args):
    '''
    :returns: formatted single str object
    '''

    if len(args) == 0:
        return format(value, '') # args = []
    elif len(args) == 1:
        return format(value, args[0]) # args ['03d']

    # --- magic font ---
    elif '@f' in args:
        #print(args)
        index = args.index('@f')
        #print(index)
        if len(args) <= index+1:
            raise ValueError('No font type specified.')

        font_type = args[index+1]

        del args[index+1]
        del args[index]
    
        # must be a str object
        # !! recursive call !!
        formatted_obj = _recursive_format(value, args)

        # get ascii font for each character
        objs = [obj.split('\n') for obj in ascii_font.retrieves(font_type, formatted_obj)]
        
        # concat characters into a list of lines
        lines = multilineformat(objs)

        return '\n'.join(lines) #join to a single str

    # error
    return None


def customformat(value, format_spec=''):

    # split by ':'
    # :@f:font:03d
    args = format_spec.split(':')


    formatted_obj = _recursive_format(value, args)


    if formatted_obj is None:
        raise ValueError('Unknown format code \'{}\' for object of type \'{}\''.format(format_spec, type(value)))

    return formatted_obj.split('\n')


def calculatemaxline(value_list):
    max_count = 0
    for v in value_list:
        if isinstance(v, list) or isinstance(v, tuple):
            max_count = max(max_count, len(v))

    return max_count


def multilineformat(result, max_line_count=None):


    if max_line_count is None:
        max_line_count = calculatemaxline(result)


    # multi line formatting
    lines = ['' for _ in range(max_line_count)]

    current_max_length = 0

    for idx, segment in enumerate(result):

        # literal_text
        if isinstance(segment, str):
            # only the first line will add literal_text
            lines[0] += segment
            # others will append spaces
            for line_id in range(1, max_line_count):
                lines[line_id] += ' ' * len(segment)
                    
            current_max_length += len(segment)

        # formatting
        elif isinstance(segment, tuple):
            spec = segment[0]
            pattern = segment[1]

            if spec == 'VERT':
                for line_id in range(max_line_count):
                    lines[line_id] += pattern

                current_max_length += len(pattern)

        # formatted object
        else:
            for line_id in range(len(segment)):
                lines[line_id] += segment[line_id]

                # update max length
                current_max_length = max(current_max_length, len(lines[line_id]))
            

        # padding each line to current_max_length
        for line_id in range(max_line_count):
            lines[line_id] += ' ' * (current_max_length - len(lines[line_id])) # append spaces



    return lines

class MultilineStringFormatter(string.Formatter): 

    def format_field(self, value, format_spec):
        return customformat(value, format_spec)

    def _vformat(self, format_string, args, kwargs, used_args, recursion_depth, auto_arg_index=0):

        if recursion_depth < 0:
            raise ValueError('Max string recursion exceeded')

        result = []

        max_line_count = 0

        for literal_text, field_name, format_spec, conversion in self.parse(format_string):

            if literal_text:
                result.append(literal_text)

            if field_name is not None:

                # auto field
                if field_name == '':
                    if auto_arg_index is False:
                        raise ValueError('cannot switch from manual field specification to automatic field numbering')

                    field_name = str(auto_arg_index)
                    auto_arg_index += 1

                elif field_name.startswith('|'):
                    # add vertical line
                    if field_name[1:] == '':
                        field_name = '|'
                    else:
                        field_name = field_name[1:]

                    result.append(('VERT', field_name))
                    
                    continue

                elif field_name.isdigit():
                    if auto_arg_index:
                        raise ValueError('cannot switch from manual field specification to automatic field numbering')

                    auto_arg_index = False

                # given the field_name, find the object it references
                obj, arg_used = self.get_field(field_name, args, kwargs)
                used_args.add(arg_used)

                obj = self.convert_field(obj, conversion)

                format_spec, auto_arg_index = string.Formatter()._vformat(
                            format_spec, args, kwargs,
                            used_args, recursion_depth-1,
                            auto_arg_index=auto_arg_index)

                # splitted by \n
                formatted_obj = self.format_field(obj, format_spec)


                # format the object and append to the result
                result.append(formatted_obj)

                max_line_count = max(max_line_count, len(formatted_obj))

        lines = multilineformat(result, max_line_count)
        
        '''
        # multi line formatting
        lines = ['' for _ in range(max_line_count)]

        current_max_length = 0

        for idx, segment in enumerate(result):

            # literal_text
            if isinstance(segment, str):
                # only the first line will add literal_text
                lines[0] += segment
                # others will append spaces
                for line_id in range(1, max_line_count):
                    lines[line_id] += ' ' * len(segment)
                    
                current_max_length += len(segment)

            # formatting
            elif isinstance(segment, tuple):
                spec = segment[0]
                pattern = segment[1]

                if spec == 'VERT':
                    for line_id in range(max_line_count):
                        lines[line_id] += pattern

                    current_max_length += len(pattern)

            # formatted object
            else:
                for line_id in range(len(segment)):
                    lines[line_id] += segment[line_id]

                    # update max length
                    current_max_length = max(current_max_length, len(lines[line_id]))
            

            # padding each line to current_max_length
            for line_id in range(max_line_count):
                lines[line_id] += ' ' * (current_max_length - len(lines[line_id])) # append spaces
        '''

        return lines, auto_arg_index

