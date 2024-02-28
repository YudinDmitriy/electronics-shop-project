from src.item import Item


class MixinLang:
    lang = ('EN', 'RU')
    _language = 'EN'

    def change_lang(self):
        if self.language == 'EN':
            self._language = self.lang[-1]
        else:
            self._language = self.lang[0]

    @property
    def language(self):
        return self._language


class Keyboard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self._language = 'EN'
