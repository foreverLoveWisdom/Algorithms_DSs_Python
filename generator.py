def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


def square_numbers_generator(nums):
    for i in nums:
        yield (i * i)


my_nums = square_numbers_generator([1, 2, 3, 4, 5])
# print(my_nums)
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
