import sys

def fizz_buzz(range_max):
    range_max = int(range_max)
    for n in range (1,range_max+1): 
        if n%3 != 0 and n%5 != 0:
            print(n)
        elif n % 3 == 0:
            if n % 5 == 0:
                print('FizzBuzz')
            else:
                print('Fizz')
            
        elif n % 5 == 0:
            print('Buzz')



if __name__ == "__main__":
    fizz_buzz(sys.argv[1])