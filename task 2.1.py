# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class Rectangle:
    def __init__(self, width: Union[int, float], height: Union[int, float]):
        """
               Создание и подготовка к работе объекта "прямоугольник"

               :param width: ширина
               :param height: высота

               Примеры:
                 >>> glass = Rectangle(500, 2) # инициализация экземпляра класса
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть типа int или float")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами")

        self.width = width
        self.height = height

    def scale(self, n: Union[int, float]) -> None:
        """
            Функция которая Масштабирует прямоугольник в n раз
            :param n: Коэффициент масштабирования

            :raises TypeError: Если коэффициент не является int или float
            :raises ValueError: Если коэффициент не положительный
              Примеры:
              >>> rectangle = Rectangle(500, 200)
              >>> rectangle.scale(0.5)
        """
        if not isinstance(n, (int, float)):
            raise TypeError("Коэффициент масштабирования должен быть типа int или float")
        if n <= 0:
            raise ValueError("Коэффициент масштабирования должен быть положительным")

        self.width *= n
        self.height *= n

    def area(self) -> Union[int, float]:
        """
            Функция которая вычисляет площадь прямоугольника.

            :return: Площадь прямоугольника

            Примеры:
                >>> rectangle = Rectangle(500, 200)
                >>> rectangle.area()
                100000
        """
        return self.width * self.height

    def perimeter(self) -> Union[int, float]:
        """
                    Функция которая вычисляет периметр прямоугольника.
                    :return: Периметр прямоугольника

                    Примеры:
                        >>> rectangle = Rectangle(500, 200)
                        >>> rectangle.perimeter()
                        1400
                """
        return 2 * (self.width + self.height)

class Human:
   def __init__(self, name: str, age: int, height: Union[int, float]):
        """
            Создание и подготовка к работе объекта "Человек"

            :param name: Имя
            :param age: Возраст
            :param height: высота в см


            Примеры:
                >>> human = Human('Artem', 28, 177) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not name.strip():
            raise ValueError("Имя не может быть пустой строкой")

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")

        if not isinstance(height, (int, float)):
            raise TypeError("Рост должен быть типа int или float")
        if height <= 0:
            raise ValueError("Рост должен быть положительным числом")

        self.name = name
        self.age = age
        self.height = height

   def rename(self, new_name: str):
       """
            Функция которая изменяет имя человека на новое.
            :param new_name:

            Примеры:
                >>> human = Human('Artem', 28, 177)
                >>> human.rename("anton")
       """

       if not isinstance(new_name, str):
           raise TypeError("Имя должно быть строкой")
       if new_name == '':
           raise ValueError("Имя не может быть пустой строкой")

       self.name = new_name

   def birthday(self):
       """
              Функция которая добавляет 1 год.

               Примеры:
                       >>> human = Human('Artem', 28, 177)
                       >>> human.birthday()
                       >>> human.age
                       29
       """
       self.age += 1




class Beer:
    def __init__(self, name: str, abv: Union[int, float], volume_ml: Union[int, float]):
        """
                Создание и подготовка к работе объекта "Пиво"

                :param name: Название пива
                :param abv: Крепость в процентах
                :param volume_ml: Объем в мл

                Примеры:
                >>> beer = Beer("Spaten", 5.2, 500)  # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if name == "":
            raise ValueError("Название не может быть пустой строкой")

        if not isinstance(abv, (int, float)):
            raise TypeError("Крепость должна быть типа int или float")
        if not 0 <= abv <= 100:
            raise ValueError("Крепость должна быть от 0 до 100%")

        if not isinstance(volume_ml, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if volume_ml <= 0:
            raise ValueError("Объем должен быть положительным числом")

        self.name = name
        self.abv = abv
        self.volume_ml = volume_ml

    def add_vodka_shot(self) -> None:
        """
            Функция которая делает "Ёрш" и пересчитывает крепость и количество напитка вл.

            Примеры:
               >>> beer = Beer("Spaten", 5.2, 500)
               >>> beer.add_vodka_shot()
               >>> beer.abv
               7.8
               >>> beer.volume_ml
               540
        """
        beer_alcohol = (self.abv / 100) * self.volume_ml  # алкоголь в пиве (в мл)
        vodka_alcohol = 40 * 0.4  # 40мл * 40% = 16мл алкоголя

        new_volume = self.volume_ml + 40
        new_abv = ((beer_alcohol + vodka_alcohol) / new_volume) * 100 # Новая крепость

        self.abv = round(new_abv, 1)
        self.volume_ml = new_volume

    def drink(self, ml: int = 100):
        """
                    Функция Пить пива.

                    :param ml: миллилитров выпитого (по умолчанию 100)
                    :raises TypeError: Если количество не является целым числом
                    :raises ValueError: Если количество отрицательное или превышает текущий объем

                    Примеры:
                        >>> beer = Beer("Spaten", 5.2, 500)
                        >>> beer.drink(100)
                        >>> beer.volume_ml
                        400
                        >>> beer.drink(400)
                        >>> beer.volume_ml
                        0
        """
        if not isinstance(ml, int):
            raise TypeError("Количество должно быть целым числом")
        if ml <= 0:
            raise ValueError("Количество должно быть положительным числом")
        if ml > self.volume_ml:
            raise ValueError(f"Нельзя выпить больше, чем есть в наличии ({self.volume_ml}ml)")

        self.volume_ml -= ml

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    rect = Rectangle(400, 500)
    print(rect)
    rect.scale(2)

    beer = Beer("Baltica 7", 4.7, 500)
    beer.add_vodka_shot()
    beer.drink()

    human = Human("Иван", 25, 180)
    print(human)
    human.rename("Петр")
    human.birthday()

    doctest.testmod()
    pass
