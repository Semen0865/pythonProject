import random


class HiddenMathOperation:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

    def __hidden_operation(self):
        # Випадково обираємо одну з математичних операцій: додавання, віднімання, множення або ділення
        operation = random.choice(['+', '-', '*', '/'])

        # Генеруємо випадкове число для операції
        operand = random.randint(1, 10)

        # Виконуємо операцію
        if operation == '+':
            self.number += operand
        elif operation == '-':
            self.number -= operand
        elif operation == '*':
            self.number *= operand
        elif operation == '/':
            if operand != 0:  # перевірка на ділення на нуль
                self.number /= operand

    def display_result(self):
        self.__hidden_operation()
        print("Результат обчислень:", self.number)


# Приклад використання
number = HiddenMathOperation(10)
number.display_result(