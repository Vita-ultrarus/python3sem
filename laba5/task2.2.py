class Mother:
    def __str__(self):
        return("Доча!")


class Daughter(Mother):
    def __str__(self):
        return("Что, мама??")


print(Mother())
print(Daughter())


