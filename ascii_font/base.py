
class AsciiFont(dict):
    def __init__(self, hardblank='$'):
        self.hardblank = hardblank

    def __getitem__(self, key):
        item = super(AsciiFont, self).__getitem__(key)

        return item.replace(self.hardblank, ' ')

    def retrieve(self, font, remove_hardblank=True):
        item = super(AsciiFont, self).__getitem__(font)

        if remove_hardblank:
            return item.replace(self.hardblank, ' ')
        else:
            return item
