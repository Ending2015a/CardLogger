import os
import sys
import time
import logging

class Color(object):

    # === Set ===
    _SET_ = set([1, 2, 4, 5, 7, 8])
    _RESET_ = set([0, 21, 22, 24, 25, 27, 28, 39, 49])

    # === Color ===
    _FDCOLOR_ = set([30, 31, 32, 33, 34, 35, 36, 37])
    _FLCOLOR_ = set([90, 91, 92, 93, 94, 95, 96, 97])
    _BDCOLOR_ = set([40, 41, 42, 43, 44, 45, 46, 47])
    _BLCOLOR_ = set([100, 101, 102, 103, 104, 105, 106, 107])

    def __init__(self, *args):
        self.args = [int(i) for i in args]

    def __int__(self):
        if len(self.args) > 1:
            print(self.args)
            raise Exception('too many color codes, only one color code is accepted')
        elif len(self.args) == 0:
            raise Exception('no color codes')
        return int(self.args[0])

    def __add__(self, other):
        if isinstance(other, Color):
            other = [int(i) for i in other.args]
        elif isinstance(other, list):
            other = [int(i) for i in other]
        elif isinstance(other, tuple):
            other = [int(i) for i in other]
        else:
            other = [int(other)]

        new_color = set(self.args + other)
                        
        return type(self)(*list(new_color))

    def __radd__(self, other):
        return self.__add__(other)

    #def __iadd__(self, other):
    #    return self.__add__(other)

    def __str__(self):
        return ';'.join( [str(i) for i in self.args] )

    def __repr__(self):
        return "<{}.{} object ({}) at {}>".format(
                    type(self).__module__,
                    type(self).__qualname__,
                    self.__str__(),
                    hex(id(self)))

    #def __iter__(self):
    #    for x in list.__iter__(self.args):
    #        yield x

    def __contains__(self, key):
        return int(key) in self.args

    
    def __getitem__(self, item):
        return self.args[item]


    def type(self):
        return type(self).type(self)

    @classmethod
    def type(cls, code):
        code = int(code)

        if code in cls._SET_:
            return 'SET'
        elif code in cls._RESET_:
            return 'RESET'
        elif code in cls._FDCOLOR_:
            return 'FDCOLOR'
        elif code in cls._FLCOLOR_:
            return 'FLCOLOR'
        elif code in cls._BDCOLOR_:
            return 'BDCOLOR'
        elif code in cls._BLCOLOR_:
            return 'BLCOLOR'
        elif code == 39:
            return 'FDEFAULT'
        elif code == 49:
            return 'BDEFAULT'

        raise Exception('Unknown color code')


    @classmethod
    def _sumList(cls, clist):
        if len(clist) == 0:
            return cls(0)

        c = None
        for t in clist:
            c = cls(t) if c is None else c+cls(t)
        return c

    @classmethod
    def reset(cls, *args):
        codes = []
        if len(args) == 0:
            return Color(0)
        else:

            for color in args:
                codes += list(color)

            for idx, code in enumerate(codes):
                t = cls.type(code)
                if t in ['SET']:
                    color = cls(code+20)
                elif t in ['FDCOLOR', 'FLCOLOR']:
                    color = cls(39)
                elif t in ['BDCOLOR', 'BLCOLOR']:
                    color = cls(49)
                else:
                    color = cls(code)

                codes[idx] = color
    
        return cls._sumList(codes)


    @classmethod
    def background(cls, *args):
        codes = []
        if len(args) == 0:
            raise Exception('no color was specified to be transformed into background color code')
        else:
            for color in args:
                codes += list(color)
            
            for idx, code in enumerate(codes):
                t = cls.type(code)
                if t in ['FDCOLOR', 'FLCOLOR', 'FDEFAULT']:
                    color = cls(code + 10)
                else:
                    color = cls(code)
                
                codes[idx] = color

        return cls._sumList(codes)
    
    @classmethod
    def foreground(cls, *args):
        codes = []
        if len(args) == 0:
            raise Exception('no color was specified to be transformed into forground color code')
        else:
            for color in args:
                codes += list(color)

            for idx, code in enumerate(codes):
                t = cls.type(code)
                if t in ['BDCOLOR', 'BLCOLOR', 'BDEFAULT']:
                    color = cls(code - 10)
                else:
                    color = cls(code)

                codes[idx] = color

        return cls._sumList(codes)


    @classmethod
    def dark(cls, *args):
        codes = []
        if len(args) == 0:
            raise Exception('no color was specified to be transformed into dark color code')
        else:
            for color in args:
                codes += list(color)
            
            for idx, code in enumerate(codes):
                t = cls.type(code)
                if t in ['BLCOLOR', 'FLCOLOR']:
                    color = cls(code - 60)
                else:
                    color = cls(code)

                codes[idx] = color

        return cls._sumList(codes)


    @classmethod
    def light(cls, *args):
        codes = []
        if len(args) == 0:
            raise Exception('no color was specified to be transformed into light color code')
        else:
            for color in args:
                codes += list(color)

            for idx, code in enumerate(codes):
                t = cls.type(code)
                if t in ['BDCOLOR', 'FDCOLOR']:
                    color = cls(code + 60)
                else:
                    color = cls(code)

                codes[idx] = color

        return cls._sumList(codes)


    @classmethod
    def bg(cls, *args):
        return cls.background(*args)

    @classmethod
    def fg(cls, *args):
        return cls.foreground(*args)





Color.BOLD = Color(1)
Color.DIM = Color(2)
Color.UNDERLINE = Color(4)
Color.BLINK = Color(5)
Color.REVERSE = Color(7)
Color.HIDDEN = Color(8)

Color.DEFAULT = Color(39)
Color.BLACK = Color(30)
Color.RED = Color(91)
Color.GREEN = Color(92)
Color.YELLOW = Color(93)
Color.BLUE = Color(94)
Color.MAGENTA = Color(95)
Color.CYAN = Color(96)
Color.GRAY = Color(37)
Color.WHITE = Color(97)




if __name__ == '__main__':

    print('Black:', Color.BLACK)
    print('White:', Color.WHITE)
    print('Bold:', Color.BOLD)
    print('Black + Bold:', Color.BOLD + Color.BLACK)
    print('reset all:', Color.reset())
    print('reset Black:', Color.reset(Color.BLACK))
    print('reset (Black + Bold):', Color.reset(Color.BLACK + Color.BOLD))
    print('reset (Black and Bold):', Color.reset(Color.BLACK, Color.BOLD))
    print('White background:', Color.bg(Color.WHITE))
    print('White background + Black foreground:', Color.bg(Color.WHITE) + Color.BLACK)
    print('reset background:', Color.reset(Color.bg(Color.WHITE)))
    print('reset background + reset foreground + bold:', Color.reset(Color.BLACK + Color.bg(Color.BLACK)) + Color.BOLD)
