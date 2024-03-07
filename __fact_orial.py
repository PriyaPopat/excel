def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

fact=factorial(5)
print(fact)

#palidrome check

def is_palidrome(word):
    return word==word[::-1]
result_palindrome=is_palidrome("radar") #read from left side and right side both are same
print(result_palindrome)

