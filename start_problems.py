def sum_of_digits (numbers):

    total = 0
    if numbers < 0:
        numbers *= -1

    strnum = str(numbers)

    for i in strnum:
        total += int(i)
    return (total)

def to_digits(n):
    out = []
    for i in str(n):
        out.append(int(i))
    return out

if __name__ == '__main__':
    '''
    sum_of_digits(1325132435356)
    sum_of_digits(123)
    sum_of_digits(6)
    sum_of_digits(-10)

    to_digits(123)
    to_digits(99999)
    to_digits(123023)



    to_number([1, 2, 3])
    to_number([9, 9, 9, 9, 9])
    to_number([1, 2, 3, 0, 2, 3])
    to_number([21, 2, 33])
    '''
