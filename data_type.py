
#numeric  data type
# 1 intiger
number=30
print(number)

# 2 floating

number2=50.43
print(number2)

# complex_number

complex_number=3+10j
print(complex_number)

#string data type

name="Arafat Islam"
print(name)

#sequence  data type

# 1 array
#only int
number=[10,20,30]
print(number)
#only string
country_name=["Dhaka","Khulna",'Komilla']
print(country_name)
# int , float and string
number2=['dhaka',10,123.45,'komilla']
print(number2)
# ripited value allow
number3=["Dhaka","Khulna",'Komilla',"Dhaka","Khulna",'Komilla']
print(number3)

number3=("Dhaka","Khulna",'Komilla',"Dhaka","Khulna",'Komilla')
print(number3[2])
number3=("Dhaka","Khulna",'Komilla',"Dhaka","Khulna",'Komilla')
print(number3[4])
number3=("Dhaka","Khulna",'Komilla',"Dhaka","Khulna",'Komilla')
print(number3[3])

# 2 tuple

#only int
number=(10,20,30)
print(number)

#only string
country_name=("Dhaka","Khulna",'Komilla')
print(country_name)

# int , float and string
number2=('dhaka',10,123.45,'komilla')
print(number2)

# ripited value allow
number3=("Dhaka","Khulna",'Komilla',"Dhaka","Khulna",'Komilla')
print(number3)

# range

number=range(0,10)
print(number)

number=range(0,10)
print(*number)

number=range(0,10,2) # 2 kore berbe
print(*number)

number=range(0,30,3) # 3 kore berbe
print(*number)

number=range(10) # by defolt 0 theke soro hobe and 9 porjonto cholbe
print(*number)

# Boolean data type

isBangladesh=True
print(isBangladesh)

# none data type
name=None
print(name)

#mapping data type
#dictronary data type (dict data type)
person={
    'First_name': 'Arafat' ,
    'Last_name': 'Islam' ,
    'Age': 25 ,
    'isBangladesh': True

 }

print(person)
print(person['Last_name'])
print(person['isBangladesh'])


#set data type

number={1,2,3,4,5}
print(number)
number1={1,2,3,2,4,5,3}
print(number1)

#frozenset (immutable)
number=frozenset([1,2,3,4,5,6])
print(number)

number1=frozenset([1,2,1,5,4,3,4,5,6])
print(number1)