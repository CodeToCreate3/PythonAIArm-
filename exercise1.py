'''
 file name: exercise1.py
 author: Denho
 date: 13/02/2025
'''

# this python file allows us to understand on the usage/ working of loops
# declare some global variables

number = 234
name_of_user = "Denho"
gender = "male"

# A function to print the name 10 times
def loop_name(username):
    state = True
    count = 0
    total_count = 10
    
    # if to check on the state of the loop
    while state:
        if count < total_count:
            # increment the count
            count += 1
            print(f"My name is {username}")
            if count == 5:
               continue
        elif count == total_count:
            break


# user to enter the user name
my_name = input("Enter your name: ")
# call / invoke the function
loop_name(my_name)
print("Hello bye!!")
        

