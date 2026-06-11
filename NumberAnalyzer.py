num = input("Enter a number: ")
og_num = num

def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a - 1)

ans = [int(ch) if ch != "0" else 0 for ch in num]
print("Digits: ", ans)

add = 0
prod = 1
for n in ans:
    add += n
    prod *= n
print("Sum: ", add)
print("Product: ", prod)

print("Reverse: ", "".join(str(digit) for digit in ans)[::-1])
print("Palindrome:", True if ans == ans[::-1] else False)
print("Largest:", max(ans))
print("Smallest:", min(ans))
print("Factorials:", factorial(int(og_num)))
print("Even digits:", len([e for e in ans if e % 2 == 0]))
print("Odd digits:", len([o for o in ans if o % 2 != 0]))