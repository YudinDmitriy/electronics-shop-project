import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        with open(csv_file, newline='', encoding='windows-1251') as csvfile:
            items = csv.DictReader(csvfile, delimiter=',')
            cls.all = []
            for item in items:
                cls(str(item['name']), float(item['price']), int(item['quantity']))

    @staticmethod
    def string_to_number(number):
        if number.isdigit():
            return int(number)
        elif '.' in number:
            return int(float(number))

