def camelCase(string):
    string = input("enter your sentence: ")

    output = ''.join(x for x in string.title() if x.isalnum())
    return output[0].lower()+output[1:]

print(camelCase('string'))

