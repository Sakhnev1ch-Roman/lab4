from typing import Any


class Animal:
    """
    Базовый класс для представления животного.

    Attributes:
        name (str): Имя животного.
        age (int): Возраст животного.
        _energy (int): Уровень энергии животного. Сделан непубличным,
                       так как не должен изменяться напрямую извне.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Конструктор базового класса Animal.

        Args:
            name (str): Имя животного.
            age (int): Возраст животного.
        """
        self.name: str = name
        self.age: int = age
        self._energy: int = 100  # инкапсуляция — внутреннее состояние энергии

    def eat(self, food: str) -> None:
        """
        Метод питания животного.

        Args:
            food (str): Тип пищи.
        """
        pass

    def make_sound(self) -> str:
        """
        Метод, который возвращает звук животного.

        Returns:
            str: Звук животного.
        """
        pass

    def __str__(self) -> str:
        """
        Человекочитаемое представление объекта.

        Returns:
            str: Строковое описание животного.
        """
        return f"Animal(name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        """
        Представление объекта для разработчика.

        Returns:
            str: Строковое представление объекта.
        """
        return f"Animal(name='{self.name}', age={self.age})"


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.

    Наследуется от класса Animal и расширяет его функциональность.

    Attributes:
        breed (str): Порода собаки.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор класса Dog.

        Расширяет конструктор базового класса Animal,
        добавляя параметр породы.

        Args:
            name (str): Имя собаки.
            age (int): Возраст собаки.
            breed (str): Порода собаки.
        """
        super().__init__(name, age)
        self.breed: str = breed

    def make_sound(self) -> str:
        """
        Переопределённый метод из базового класса.

        Причина перегрузки:
        В базовом классе звук животного не определён,
        поэтому в классе Dog необходимо реализовать
        специфическое поведение — лай.

        Returns:
            str: Звук собаки.
        """
        return "Woof!"

    def fetch(self, item: str) -> str:
        """
        Метод, специфичный для собак.

        Args:
            item (str): Предмет, который нужно принести.

        Returns:
            str: Сообщение о действии.
        """
        pass

    def __str__(self) -> str:
        """
        Переопределённый метод строкового представления.

        Returns:
            str: Человекочитаемое описание собаки.
        """
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def __repr__(self) -> str:
        """
        Представление объекта для разработчика.

        Returns:
            str: Точное представление объекта Dog.
        """
        return f"Dog(name='{self.name}', age={self.age}, breed='{self.breed}')"
