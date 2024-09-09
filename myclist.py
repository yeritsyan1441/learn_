
"""1․ Գրել MyList class, որը կունենա գրեթե բոլոր այն մեթոդները
և ֆունկցիոնալությունը, որը ունի list class-ը առանց ժառանգելու։"""


class MyList:
    
    __num = None
    
    def __init__(self):
        self.number = []

    def append(self, number):
        if isinstance(number, int):
            self.number += [number]
        elif isinstance(number, list):
            self.number += number
        else:
            raise TypeError("Can not concatenate such types")

    def pop(self, index=None):
        item = -1
        if index is None and self.number:
            self.number = self.number[:item]
            item += -1
            self.__num = self.number[item]
        else:
            if isinstance(index, int) and self.number:
                new = []
                for k in range(len(self.number)):
                    if k != index:
                        new += [self.number[k]]
                self.number = new.copy()
   
    def sort(self, reverse=False):
        if reverse is False:
            for j in range(len(self.number)):
                for k in range(len(self.number)-j-1):
                    if self.number[k] > self.number[k+1]:
                        self.number[k], self.number[k + 1] = self.number[k+1], self.number[k]
        else:
            for j in range(len(self.number)):
                for k in range(len(self.number)-j-1):
                    if self.number[k] < self.number[k+1]:
                        self.number[k], self.number[k+1] = self.number[k+1], self.number[k]

    def extend(self, iterable):
        for k in iterable:
            self.number += [k]

    def index(self, element):
        for j in range(len(self.number)):
            if self.number[j] == element:
                return j

    def count(self, element):
        counter = 0
        for j in self.number:
            if j == element:
                counter += 1
        return counter

    def remove(self, element):
        new = []
        for j in self.number:
            if j != element:
                new.append(j)
        self.number = new.copy()

    def insert(self, position, value):
        ...

    def __copy__(self):
        pass

    def __str__(self):
        return f"{self.number}"



