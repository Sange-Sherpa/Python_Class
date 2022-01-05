# def users(*num):
#     total = 0
#     i = 0
#     while i < len(num):
#         total += num[i]
#         i += 1
#     print(f"Sum is: {total}")


# def users(*num, **key):
#     total = 0
#     for i in range(len(num)):
#         # total += num[i]
#         total = sum(num)
#
#     print(f"Sum is: {total}")
#
#
# users(1, 2, 3)


# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# print(fact(3))

# arr = []

# def arrange(*num):
#     for i in range(len(num)):
#         a = num[i]
#         b = num[i + 1]
#
#         if a > b:
#             a = b
#             arr.append(a, b)
#
#     print(arr)
#
#
# arrange(2, 1, 5)


# l = lambda x, y: x + y
# print(l)


def test(n):
    def get_name():
        return f"My name is {n}"
    return get_name


print(test(input("Enter your name: "))())
