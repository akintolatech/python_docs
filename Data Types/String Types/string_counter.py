"""
Programming Python
Desc: String Counter and Replacer
All right reserved Motiv8 Technologies Dec 2021
"""
text = open('test.txt')
string = text.read()

string_list = string.split()




print(string_list)
# print(string_list.count('to'))

# print(string_list.replace('to', 'saratu'))
shell = list()

for i in string_list:
    if i == 'to':
        string_list.remove(i)
        string_list.append('saratu')

print(string_list)