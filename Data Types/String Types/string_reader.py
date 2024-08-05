# global variables

def string_reader(file_name, numlines=15):
    # open file
    text = open(file_name)
    chunk = str(text.readlines())
    str_len = len(chunk)
    text = chunk[2: str_len - 2]
    read_out = text[: numlines]

    if str_len > numlines:
        return read_out #str_len
    else:
        return ("Error! for reader")

print("String Reader v1 ____________________\nStatus: File Read Sucessfuly!\n1. Print All\n2. Lines to print")
# print(string_reader("test.txt", ))
read_choice = input("Choose Option: ")
# print(type(read_choice))


all_ = string_reader("test.txt", 10)
print(all_)

if read_choice == "1":
    all_ = string_reader("test.txt", 283)
    print(all_)
elif read_choice == 2:
    amt = int(input("Enter amount: "))
    line_break = string_reader("test.txt", amt)
    print(line_break)
else:
    print("Error!!")


# print(read_choice)
# if read_choice ==

