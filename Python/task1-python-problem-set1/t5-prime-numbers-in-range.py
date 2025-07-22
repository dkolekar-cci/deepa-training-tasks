#Task 5: Prime numbers in a list

def primes_in_range(start, end):
    if start < 0 or end < 0:
        return "Please enter positive numbers only."
    if start > end:
        return "Invalid range. Starting number must be less than or equal to ending number."

    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)

    return "Prime numbers between " + str(start) + " and " + str(end) + " are: " + str(primes)

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
print(primes_in_range(start, end))

# Hardcoded call
print(primes_in_range(10, 30))
print(primes_in_range(50, 30))
print(primes_in_range(-10, 30))
print(primes_in_range(10, 10)) #empty list