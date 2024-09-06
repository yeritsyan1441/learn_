class Calculator:

    def __init__(self, number):
        if isinstance(number, int | float):
            self.__number = number
        else:
            raise ValueError("Number must be int or float")

    @property
    def number(self):
        return self.__number

    def __add__(self, other):
        if isinstance(other, Calculator):
            return self.__number + other.__number

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return self.__number - other.__number

    def __rsub__(self, other):
        return other - self.__number

    def __eq__(self, other):
        if isinstance(other, Calculator):
            return self.__number == other.__number

    def __mul__(self, other):
        return self.__number * other.__number

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            return self.__number / other.__number

    def __rtruediv__(self, other):
        return other.__number / self

    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            return self.__number // other.__number

    def __rfloordiv__(self, other):
        return other.__number // self.__number


class Clock:

    def __init__(self, seconds, tm):
        self.seconds = seconds % 86400
        self.tm = None

    def __str__(self):
        hours = self.seconds // 3600
        minutes = (self.seconds - hours * 3600) // 60
        seconds = self.seconds % 60
        self.tm = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def change_time(current_time, changing):

    if int(changing[:2]) + int(current_time[:2]) <= 24:
        hour = int(changing[:2]) + int(current_time[:2])
    elif int(changing[:2]) + int(current_time[:2]) > 24:
        hour = int(changing[:2]) + int(current_time[:2]) - 24
    if int(changing[3:5]) + int(current_time[3:5]) <= 60:
        minute = int(changing[3:5]) + int(current_time[3:5])
    elif int(changing[3:5]) + int(current_time[3:5]) > 60:
        minute = int(changing[3:5]) + int(current_time[3:5]) - 60
    if int(changing[6:]) + int(current_time[6:]) <= 60:
        second = int(changing[6:]) + int(current_time[6:])
    elif int(changing[6:]) + int(current_time[6:]) > 60:
        second = int(changing[6:]) + int(current_time[6:]) - 60

    return f"{hour:02d}:{minute:02d}:{second:02d}"



# second = Clock(4500)
# print(second)


