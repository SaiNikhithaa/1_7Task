#Create a dictionary from two lists:
#a.	keys = ['id', 'name', 'age']
#b.	values = [101, 'John', 25]
keys = ['id', 'name', 'age']
values = [101, 'John', 25]
my_dict = dict(zip(keys, values))
print(my_dict)
#Create a dictionary to store student name and age.
student=["nikhitha","suvarna","alekhya","arundathi","ayesha","keerthana"]
age=[21,22,23,15,19,20]
final=dict(zip(student,age))
print(final)
#Create an empty dictionary and add key-value pairs one by one
my_dict = {}
my_dict['id'] = 101
my_dict['name'] = 'Nikhitha'
my_dict['age'] = 25
print(my_dict)
#Get the value of key "salary" from this dictionary:
#                    EX: employee = {'name': 'John', 'age': 30, 'salary': 50000}
employee={
    "name" : "john",
    "age" : 21,
    "salary" : 50000
}
print(employee.get("salary"))
#Remove the last inserted key-value pair from the dictionary using an appropriate method
details= {
    "name" : "Nikhitha",
    "branch" : "ECE",
    "college" : "MRECW"
}
print(details.popitem())
#Define packing and unpacking in Python. Also, provide one example for both packing and unpacking.
#packing:
"""Packing is the process of putting multiple values into a single variable (like a tuple or list)."""
person = ("Nikhitha", 22, "ECE")
print(person)
#unpacking:
"""Unpacking is the process of extracting individual values from a packed collection"""
name, age, branch = person
print(name)
print(age)
print(branch)
