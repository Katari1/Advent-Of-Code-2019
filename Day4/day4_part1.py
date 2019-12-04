#6 digit number
#Must have two adjacent digits
#Left to Right values only increase



def duplicatadjacentdigit(number):
    number = map(int, str(number))
    if len(number) != len(set(number)):
        count = {i:number.count(i) for i in number}
        for key in count:
            if count[key] > 1:
                if number[number.index(key)] == number[number.index(key) + 1]:
                    return True
                else:
                    return False

def isincreasing(number):
    number = map(int, str(number))
    for i in range(len(number) - 1):
        if number[i] <= number[i + 1]:
            pass
        else:
            return False
    return True

def calculate(number):
    if duplicatadjacentdigit(number):
        if isincreasing(number):
            return True
    return False

count = 0
for i in range(272091,815432):
    if calculate(i):
        count +=1
print count