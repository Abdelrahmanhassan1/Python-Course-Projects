def prime_checker(number):
    prime_flag = True
    if number >= 2:
        for num in range(2, number):
            if number % num == 0:
                prime_flag = False
                break

        if prime_flag:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is a not prime number")
    else:
        print(f"{number} is a not prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
