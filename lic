# Marcin Kapiszewski

def change_digit(letter, index, new_value):
    global input_debt, output_debt, debt
    index = -int(index)
    new_value = int(new_value)
    if letter == 'W':
        difference = new_value - input_debt[index]
        input_debt[index] = new_value
    else:
        difference = new_value - output_debt[index]
        output_debt[index] = new_value

    number = int(debt[index]) + difference
    str_number = str(number)
    if number >= 10:
        debt[index] = int(str_number[1])
        while debt[index-1] == 9:
            debt[index-1] = 0
            index -= 1
        debt[index-1] = debt[index-1] + 1
    elif number >= 0:
        debt[index] = number
    else:
        debt[index] = 10 + number
        while debt[index - 1] == 0:
            debt[index-1] = 9
            index -= 1
        debt[index-1] = debt[index - 1] - 1

if __name__ == "__main__":
    n, z = list(map(int, input().split()))
    input_debt = input()
    output_debt = input()
    the_sum = str(int(input_debt) + int(output_debt))
    debt = '0'*(n - len(the_sum)) + the_sum
    input_debt = list(map(int, list(input_debt)))
    output_debt = list(map(int, list(output_debt)))
    debt = list(map(int, list(debt)))

    for _ in range(z):
        data = input().split()
        if data[0] == 'S':
            print(debt[-int(data[1])])
        else:
            change_digit(*data)
