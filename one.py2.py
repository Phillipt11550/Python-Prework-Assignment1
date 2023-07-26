def hello_name(user_name):
    print("Hello, " + user_name +"!")

def first_odds(n):
    return[x for x in range(1, n + 1, 2) if x % 1 == 0]
print(first_odds(101))
def max_num_in_list(a_list):
    return max(a_list)

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 100 == 0 and year % 400 != 0:
        leap = False
    elif year % 400 == 0:
        leap = True
    elif year % 4 != 0:
        leap = False
    return leap
print(is_leap_year(1900))


def is_consecutive(a_list):
    if len(a_list) < 2:
        return True
    for i in range(len(a_list)-1):
        if a_list[i+1] - a_list[i] != 1:
            return False
    return True

print(is_consecutive([2,3,4,5,6,7])) # True
print(is_consecutive([1,2,4,5])) # False




        
                        
