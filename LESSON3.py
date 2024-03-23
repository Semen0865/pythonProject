import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3


    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:+^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
kate = Student(name="Kate")
semen = Student(name="Semen")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
    if kate.alive == False:
        break
    kate.live(day)
    if semen.alive == False:
        break
    semen.live(day)


    class Student:
        def __init__(self, name, money=0):
            self.name = name
            self.money = money
            self.learning_ability = 100
            self.job = None

        def earn_money(self, amount):
            """Заробіток грошей"""
            self.money += amount
            print(f"{self.name} заробив {amount} грошей. Загальний баланс: {self.money}")

        def spend_money(self, amount):
            """Витрачання грошей"""
            if self.money >= amount:
                self.money -= amount
                print(f"{self.name} витратив {amount} грошей. Загальний баланс: {self.money}")
            else:
                print("Недостатньо коштів!")

        def study(self):
            """Студент вивчається"""
            if self.learning_ability >= 90:
                print(f"{self.name} вже дуже добре навчається!")
            else:
                self.learning_ability += 10
                print(f"{self.name} вдосконалюється в навчанні. Здатність до навчання: {self.learning_ability}")

        def go_to_work(self):
            """Студент йде на роботу"""
            if self.job is None:
                print(f"{self.name} немає роботи!")
            else:
                print(f"{self.name} йде на роботу в {self.job}")

        def solve_problem(self):
            """Студент вирішує проблему"""
            if self.money >= 50:
                self.spend_money(50)
                print(f"{self.name} вирішив проблему!")
            else:
                print(f"{self.name} не має грошей, щоб вирішити проблему. Потрібно піти на роботу!")

        def live_one_year(self):
            """Студент живе протягом року"""
            for _ in range(12):
                self.study()
                if self.learning_ability < 50:
                    self.go_to_work()
                elif self.money < 10:
                    self.go_to_work()
                elif self.money >= 100:
                    self.spend_money(100)
                else:
                    self.solve_problem()
