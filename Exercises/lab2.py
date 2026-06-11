# def myFun(*args, **kwargs):
#     print("Args")
#     for arg in args:
#         print("Args:", arg)
#     print("Kwargs")
#     for key, value in kwargs.items():
#         print("Kwargs:", key, "=", value)
# myFun("Hey", "Ruth", 1, 2, 3, city="Addis Ababa", school="AAU")

# def f1():
#     s = "This is function 1"
#     print("this is function")
#     def f2():
#         print(s)
#     f2()
# f1()

# def c1(x): return x**2
# c2 = lambda x: x**2
# print(c1(5))
# print(c2(5))

# def myFun(x):
#     if x % 2 == 0:
#         print("Even")
#         return x**2
#     else:
#         print("Odd")
#         return x**3
    
# print(myFun(int(input("Enter a number:"))))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# num = int(input("Enter a number: "))
# print(factorial(num))

# def add(x):
#     if x == 1:
#         return 1
#     return x + add(x-1)
# num = int(input("Enter a number: "))
# print(add(num))

# data = [1, 2, 3, 4, 5]
# res = [val**2 + val/2 for val in data]
# print(res)

# range_val = range(0, 15)
# res = [val**2 if val % 2 == 0 else val**3 for val in range_val]
# print(res)

# c = [(x, y) for y in range(3) for x in range(3)]
# print(c)

# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = [val for row in mat for val in row]
# print(res)

function = [lambda arg=x: arg*10 for x in range(1, 5)]
for f in function:
    print(f())