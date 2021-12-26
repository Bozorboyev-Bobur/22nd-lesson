# rf = open('./data.txt', 'r')
# rf.close()

# with open('./data.txt', 'r') as rf:
#     lines = rf.readlines()
#     users = []
#     for line in lines:
#         list = line.strip().split(';')
#         user = {
#             'fullName': list[0],
#             'birthDate': list[1],
#             'age': int(list[2]),
#             'sex': list[3]
#         }
#         users.append(user)
#     print(users)


# print(isinstance(True, int))
# print(type(1) == int)


# with open('./data.txt', 'r') as rf:
#     lines = rf.readlines()
#     numbers = []
#     for line in lines:
#         list = line.strip().split(';')
#         if len(list) == 1:
#             numbers.append(list[0])
#     print(numbers)

# with open('./data.txt', 'r') as rf:
#     numbers = []
#     for line in rf:
#         line = line.strip()
#         if line.isdigit():
#             numbers.append(int(line))
#     print(numbers)



# Запишите в файл table.txt таблицу умножения 10
# 10 x 1 = 10
# 10 x 2 = 20
# 10 x 3 = 30
# ...
# 10 x 10 = 100

# with open('table.txt', 'w') as wf:
#     for i in range(1, 11):
#         wf.write(f'10 x {i} = {10 * i}\n')

# with open('family.txt', 'w') as wf:
#     familyMembers = int(input('How many members are in your family?'))
#     for i in range(1, familyMembers):
#         relation = input(f'What is {i} person\'s relation to you? ')
#         name = input(f'What is your {relation}\'s name? ')
#         wf.write(f'{relation} - {name}\n')
#     name = input('What is your name? ')
#     wf.write(f'Me - {name}')


# names = ['Timur', 'Shukhrat', 'Sanjar']
# TiMuR
# ShUkHrAt
# SaNjAr

# with open('names.txt', 'w') as wf:
#     for name in names:
#         newName = ''
#         for i, char in enumerate(name):
#             if i % 2 == 0: newName += char.upper()
#             else: newName += char
#         wf.write(f'{newName}\n')


nums = [123, 1000, 654, 12, 10093]

def multiply(number):
    return ()


with open('digits.txt', 'w') as wf:
    for num in nums:
        digitList = []
        while num > 0:
            digit = num % 10
            digitList.append(digit)
            num = num // 10
        digitList.reverse()
        str = ''
        for i, digit in enumerate(digitList):
            if i != len(digitList) - 1: str = str + f'{digit} + '
            else: str = str + f'{digit} = {multiply(num)}'
        wf.write(str)
# digits.txt

# 1 + 2 + 3 = 6
# 1 + 0 + 0 + 0 = 1
# 6 + 5 + 4 = 15
# ...