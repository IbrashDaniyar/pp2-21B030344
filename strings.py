s1 = "Hello"
print(type(s1))
multi_string1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

multi_string2 = '''
This is the multiline string
that can contain multiple lines of text
in a single string variable 
'''

my_str = "Seoul National university"
ch1 = my_str[0]
ch2 = my_str[-1]

print(ch1, ch2)

print(len("Hello World"));

if "Seoul" in my_str:
    print("Yes")
else:
    print("No")

if "Private" not in my_str:
    print("national")
    
else:
    print("private")

print(my_str[:5])
print(my_str[6:14])
print(my_str[15:])
print(my_str[-5:-2:-1])

a = "Kendrik Lamar"
print(a.upper()) 
print(a.lower()) 
print(a.strip()) 
print(a.replace('K', 'G')) 
print(a.split(' ')) 

name = "Daniyar"
surname = "Ibrash"
fullname = surname + " " + name
print(fullname)