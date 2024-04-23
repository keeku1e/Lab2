def display_main_menu():
    print("Enter some numbers seperated by commas (e.g 5, 6, 7, 8)")
    
def get_user_input():
    string1 = input()
    list1 = string1.split(",")
    for i in range(len(list1)):
        list1[i] = float(list1[i])
    
    return list1

def calc_average_temperature(list1):
    return sum(list1)/len(list1)

def calc_min_max_temperature(list1):
    return min(list1), max(list1)
        
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    x = get_user_input()
    print(calc_average_temperature(x))
    print(calc_min_max_temperature(x))


if __name__ == "__main__":
    main()