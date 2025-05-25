name = input('Enter a string: \t')
print('The string is: ', name)
reverse = ''
# for char in range(len(name)):
#     reverse = name[char] + reverse

#using slicing
# reverse = name[::-1]
# print('The reverse of the string is: ', reverse)

for char in name:
    reverse = char + reverse
print('The reversed string is: ', reverse)
