# cool trick
l = ['qwer', 'asdf', 'zxcv']
# [
#   'qwer',
#   'asdf',
#   'zxcv',
# ]

(list(zip(*l)))
# [('q', 'a', 'z'), ('w', 's', 'x'), ('e', 'd', 'c'), ('r', 'f', 'v')]


a = [1, 5, 3]
b = [4, 2, 6]
my_sum = map(lambda x, y: x + y, a, b)
print(list(my_sum))

biggest = map(lambda x, y: x if x > y else y, a, b)
print(*biggest)



big_nums = filter(lambda x: x > 3, a)
print(list(big_nums))

    