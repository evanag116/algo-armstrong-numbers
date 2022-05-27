def find_armstrong_numbers(numbers):
    armstrong_numbers = []
    for i in numbers:
        if sum([int(j)**(len(str(i))) for j in list(str(i))]) == i:
            armstrong_numbers.append(i)



    # easier to read

    # nums_list = list(numbers)
    # for i in nums_list:
    #     sums = []
    #     for j in str(i):
    #         sums.append(int(j) **len(str(i)))
    #         if sum(sums) == i:
    #             armstrong_numbers.append(i)

    return numbers
    


print(find_armstrong_numbers(3))