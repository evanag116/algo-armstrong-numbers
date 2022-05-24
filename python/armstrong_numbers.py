def find_armstrong_numbers(numbers):
    armstrong_numbers = []
    for i in numbers:
        if sum([int(j)**(len(str(i))) for j in list(str(i))]) == i:
            armstrong_numbers.append(i)

    return armstrong_numbers


