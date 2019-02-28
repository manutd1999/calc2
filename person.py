from random import choice


class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.make_greeting()

    def make_greeting(self):
        return 'Hello {n}'.format(n=self.name)


def main():
    people = [
        Person('Mya'),
        Person('Jill'),
        Person('Peter'),
        Person('Ali'),
        Person('Sara')
    ]
    person = choice(people)
    print(person)


if __name__ == '__main__':
    main()
