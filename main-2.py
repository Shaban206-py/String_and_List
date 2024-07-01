# String...
nam : str = "Hello world"
print(nam)




#string are immuatable
# nam[4] = "e"
#it shows an error because strings cannot be change

#string can be concatinate
string1 : str = 'Hello' 
string2 : str = 'World'
string3 = string1+string2
print(string3)

# if we want add string with space

string1 : str = 'Hello' 
string2 : str = 'World'
string3 = string1+' '+ string2
print(string3)
    

    # String cannot be added with other values
# language : str = 'Python'
# age :int = 20
# value1 = language+age
# print(value1)

#If we want to add string and other data type we can add by assinging it as a string 

language : str = 'Python'
age :int = 20
value1 = language+str(age)
print(value1)