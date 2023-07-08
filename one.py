def hello_name(user_name):
    print("Hello, " + user_name)

def first_odds():  
    first_odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
    first_odds =  (1, 100)

def max_num_in_list(a_list):
      return max(a_list)  
def is_leap_yeat(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def is_consecutive(a_list):
    return len(set(a_list)) == len(a_list)    
