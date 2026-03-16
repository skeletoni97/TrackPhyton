if __name__ == "__main__":
    class AlcoholicBeverage:
        """
        Базовый класс для алкогольных напитков.

        Attributes:
            name (str): Название напитка.
            abv (float): Крепость напитка в процентах.
            volume_ml (float): Объем напитка в миллилитрах.
        """

        def __init__(self, name: str, abv: float, volume_ml: float) -> None:
            """
            Инициализация алкогольного напитка.

            Args:
                name: Название напитка.
                abv: Крепость напитка в процентах.
                volume_ml: Объем напитка в миллилитрах.

            Raises:
                ValueError: Если крепость или объем имеют некорректное значение.
            """
            if abv < 0 or abv > 100:
                raise ValueError("Крепость должна быть в диапазоне от 0 до 100 процентов.")
            if volume_ml < 0:
                raise ValueError("Объем не может быть отрицательным.")

            self.name = name
            self.abv = abv
            self.volume_ml = volume_ml

        def drink(self, ml: float) -> None:
            """
            Выпить указанное количество напитка.

            Args:
                ml: Количество напитка в миллилитрах.

            Raises:
                ValueError: Если количество миллилитров некорректно
                    или превышает оставшийся объем.
            """
            if ml <= 0:
                raise ValueError("Количество должно быть больше нуля.")
            if ml > self.volume_ml:
                raise ValueError(
                    f"Нельзя выпить {ml} мл, осталось только {self.volume_ml} мл."
                )

            self.volume_ml -= ml
            print(f"Выпито {ml} мл напитка {self.name}. Осталось: {self.volume_ml} мл.")

        def get_pure_alcohol_ml(self) -> float:
            """
            Рассчитать количество чистого алкоголя в напитке.

            Этот метод наследуется дочерними классами без изменений,
            так как формула расчета одинакова для всех алкогольных напитков.

            Returns:
                Количество чистого алкоголя в миллилитрах.
            """
            return (self.abv / 100) * self.volume_ml

        def __str__(self) -> str:
            return f"{self.name} ({self.abv}%), {self.volume_ml} мл"

        def __repr__(self) -> str:
            return f"AlcoholicBeverage('{self.name}', {self.abv}, {self.volume_ml})"


    class Beer(AlcoholicBeverage):
        """
        Класс для пива, дочерний по отношению к AlcoholicBeverage.

        Attributes:
            beer_type (str): Тип пива.
            bitterness (int): Горечь пива в IBU.
        """

        def __init__(
                self,
                name: str,
                abv: float,
                volume_ml: float,
                beer_type: str = "лагер",
                bitterness: int = 20
        ) -> None:
            """
            Инициализация объекта пива.

            Конструктор базового класса расширен добавлением
            характеристик, специфичных для пива.

            Args:
                name: Название пива.
                abv: Крепость пива в процентах.
                volume_ml: Объем пива в миллилитрах.
                beer_type: Тип пива.
                bitterness: Горечь пива в IBU.

            Raises:
                ValueError: Если горечь имеет некорректное значение.
            """
            super().__init__(name, abv, volume_ml)

            if bitterness < 0:
                raise ValueError("Горечь не может быть отрицательной.")

            self.beer_type = beer_type
            self.bitterness = bitterness

        def add_vodka_shot(self) -> None:
            """
            Добавить в пиво порцию водки.

            Метод специфичен только для класса Beer, так как
            описывает частный сценарий смешивания напитков.

            После добавления пересчитываются крепость и объем.
            """
            vodka_volume: float = 40.0
            vodka_abv: float = 40.0

            beer_alcohol: float = self.get_pure_alcohol_ml()
            vodka_alcohol: float = (vodka_abv / 100) * vodka_volume

            new_volume: float = self.volume_ml + vodka_volume
            new_abv: float = ((beer_alcohol + vodka_alcohol) / new_volume) * 100

            self.volume_ml = new_volume
            self.abv = round(new_abv, 1)

            print(f"🍺 + 🥃 = Ёрш! Теперь крепость: {self.abv}%, объем: {self.volume_ml} мл.")

        def drink(self, ml: float) -> None:
            """
            Выпить указанное количество пива.

            Метод перегружен по сравнению с базовым классом,
            потому что для пива добавлена дополнительная логика:
            предупреждение при слишком быстром употреблении.

            Args:
                ml: Количество пива в миллилитрах.
            """
            if ml > 499:
                print(f"⚠️ Осторожно! Вы слишком быстро пьете {self.name}.")
            super().drink(ml)

        def __str__(self) -> str:
            return f"Пиво {self.beer_type}: {self.name} ({self.abv}%), {self.volume_ml} мл, IBU: {self.bitterness}"

        def __repr__(self) -> str:
            return (
                f"Beer('{self.name}', {self.abv}, {self.volume_ml}, "
                f"'{self.beer_type}', {self.bitterness})"
            )


    class Vodka(AlcoholicBeverage):
        """
        Класс для водки, дочерний по отношению к AlcoholicBeverage.

        Attributes:
            filtration (int): Степень фильтрации от 1 до 5.
        """

        def __init__(
                self,
                name: str,
                abv: float,
                volume_ml: float,
                filtration: int = 3
        ) -> None:
            """
            Инициализация объекта водки.

            Конструктор базового класса расширен добавлением
            характеристики, специфичной для водки.

            Args:
                name: Название водки.
                abv: Крепость водки в процентах.
                volume_ml: Объем водки в миллилитрах.
                filtration: Степень фильтрации от 1 до 5.

            Raises:
                ValueError: Если степень фильтрации вне диапазона от 1 до 5.
            """
            super().__init__(name, abv, volume_ml)

            if filtration < 1 or filtration > 5:
                raise ValueError("Степень фильтрации должна быть в диапазоне от 1 до 5.")

            self.filtration = filtration

        def drink(self, ml: float) -> None:
            """
            Выпить указанное количество водки.

             Метод перегружен по сравнению с базовым классом,
             потому что для водки важно контролировать размер порции:
             слишком большой объем за один раз нежелателен и опасен.
            Args:
                ml: Количество водки в миллилитрах.
            """
            if ml > 50:
                print("⚠️ Водку обычно пьют небольшими порциями — до 50 мл за раз.")
            super().drink(ml)

        def __str__(self) -> str:
            return f"Водка: {self.name} ({self.abv}%), {self.volume_ml} мл, фильтрация: {self.filtration}/5"

        def __repr__(self) -> str:
            return f"Vodka('{self.name}', {self.abv}, {self.volume_ml}, {self.filtration})"


    beer = Beer("Жигулевское", 4.5, 500, "лагер", 18)
    vodka = Vodka("Столичка", 40.0, 700, 4)

    print(beer)
    print(vodka)

    beer.drink(500)
    vodka.drink(50)

    print(f"Чистого алкоголя в пиве: {beer.get_pure_alcohol_ml():} мл")
    print(f"Чистого алкоголя в водке: {vodka.get_pure_alcohol_ml():} мл")

    beer.add_vodka_shot()

