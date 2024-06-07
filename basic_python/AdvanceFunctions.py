def presentation(name= "rayen", age = 20):
    print("my name is {0}, i'm {1} years old".format(name, age))

presentation(name="ali",age= 35)



presentation("ahmed")
presentation(age=23)
def somme(*parm):
    return sum(parm)

print(somme(5,6,3,78,2,22))
numbers= (5,45, 42)


print(somme(*numbers))


# Dictionner Packing
def presentationDictioner(**kword):
    print("my name", kword['name'] , "i am", kword['age'] , 'years old')

presentationDictioner(name='rayen', age=25)

# Dictionner unPacking
def presentationDictioner(**kword):
    print("my name", kword['name'] , "i am", kword['age'] , 'years old')

d = {
    'name':'sami',
    'age': 45
}
presentationDictioner(**d)

