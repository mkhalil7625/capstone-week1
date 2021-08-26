list_of_classes = []

#ask for the number, and use a range loop
class_name = input("Enter the name of a class you are taking, or enter to quit ")
while class_name: #empty strings are falsy in python
    list_of_classes.append(class_name)
    class_name = input("Enter the name of a class you are taking, or enter to quit ")

print('The classes you are taking are: ')
for index,class_name in enumerate(list_of_classes):
    print(f'{index+1}: {class_name}')
    