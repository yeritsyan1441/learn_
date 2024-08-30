class Animal:

    @staticmethod
    def eat():
        return "Animal is eating..."

    @staticmethod
    def sleep():
        return "Animal is sleeping..."


class Bird(Animal):

    @staticmethod
    def eat():
        return "Bird is pecking at its food..."

    @staticmethod
    def fly():
        return "Bird is flying..."


class Fish(Animal):

    @staticmethod
    def swim():
        return "Fish is swimming..."









