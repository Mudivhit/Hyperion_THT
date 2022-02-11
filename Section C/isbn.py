def user_input():

    isbn_number = input("Please enter the ISBN number to verify : ")
    x = len(isbn_number) 
    if isbn_number[0:8].isdigit() or not (isbn_number[9].isdigit() or isbn_number[9].lower() == "x"):
        return isbn_number
    if x < 10 and  x != 13:
        return user_input()
    if  x < 13 and  x != 10:
        return user_input()
    
    return isbn_number    

def start_verify(isbn_number):

    result = "Invalid"
    
    if len(isbn_number) == 10:
        result = verify_isbn10(isbn_number)
        if result == "Valid" :
            result = convert_isbn10(isbn_number)
    else:
            result = verify_isbn13(isbn_number)

    print(">>>", result)
    

def verify_isbn10(isbn_number):

    numbers = [10,9,8,7,6,5,4,3,2,1]
    sum_product = 0
    length = 10

    if isbn_number[9].lower() == "x":
        length = 9
        sum_product += 10

    for i in range(length):
        
        sum_product = sum_product + int(isbn_number[i]) * numbers[i]

    if sum_product % 11 == 0:
        return "Valid"
    return "Invalid"


def verify_isbn13(isbn_number):

    numbers = [1,3,1,3,1,3,1,3,1,3,1,3,1]
    sum_product = 0

    for i in range(13):
        sum_product = sum_product + int(isbn_number[i]) * numbers[i]

    if sum_product % 10 == 0:
        return "Valid"
    return "Invalid"


def convert_isbn10(isbn_number):

    isbn = '978' + isbn_number[:-1]
    number = 0
    for i in range(len(isbn)):
        if i % 2 == 0:
            number += int(isbn[i])
        else:
            number += int(isbn[i]) * 3
    number = number % 10
    isbn_13 = str(isbn) + str(number)
    
    return isbn_13


if __name__ == "__main__":
    
    isbn = user_input()
    start_verify(isbn)

