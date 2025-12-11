#This script creates an xmas tree-looking pattern on the terminal screen when you run it, with the height being the number that the user inputs.
#ask user for number, convert it to int & save the variables
print('Enter a number:')
size = int(input())
row_num = 0

#declare space/branch variables with calcs for them, and print the trunk
for row_num in range(1, size +1):
        space = ' ' * (size - row_num)
        point = '^' * (row_num * 2 - 1)
        print(space + point)
ast_space = size - 1
print((' ' * ast_space) + '#')
print((' ' * ast_space) + '#')
