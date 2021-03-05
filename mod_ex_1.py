import copy
class animal:
    def __init__(self,type1, number_legs, colour):
        self.type1=type1
        self.number_legs=number_legs
        self.colour=colour

rappi=animal('gipogrif', 6, 'pink')
print (rappi.type1)
rappi_many=copy.copy(rappi)
print(rappi_many.type1)

kery=animal("chimera",4, 'green dot')
bill=animal('big',0, 'with pattern')
my_animal=[rappi,kery,bill]
more_animal=copy.copy(my_animal)

print(more_animal[0].type1)

print(more_animal[1].type1)