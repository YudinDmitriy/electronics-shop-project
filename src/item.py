import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.massage = args


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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise Exception

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
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        try:
            with open(csv_file, newline='', encoding='windows-1251') as csvfile:
                items = csv.DictReader(csvfile, delimiter=',')
                cls.all = []
                for item in items:
                    cls(str(item['name']), float(item['price']), int(item['quantity']))
        except(FileNotFoundError):
            raise FileNotFoundError('Отсутствует файл item.csv')
        except(KeyError):
            raise InstantiateCSVError('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(number):
        if number.isdigit():
            return int(number)
        elif '.' in number:
            return int(float(number))
