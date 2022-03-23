class Temp:
    attempts = 10

    def __init__(self, x):
        self.x = x
        Temp.attempts -= 1

    @staticmethod
    def show_attempts():
        print(Temp.attempts)

t = Temp(4)

t.show_attempts()

r= Temp(5)
r.show_attempts()