

# Facebook_Username=(input ("Username: ")) #this is where it prompts username/password
# Facebook_Password =(input ("Password: "))
Saved_Username= ("JoshuaScaife")
Saved_Password = ("mine")
running = True

while running:
    Facebook_Username=(input ("Username: ")) #this is where it prompts username/password
    if Facebook_Username == Saved_Username :
        Facebook_Password = (input ("Password: "))
        if (Facebook_Password) == (Saved_Password) :
            print ("Is this you? "), print (Facebook_Username)
            YesOrNo = input("yes or no: ")
            if YesOrNo == "yes" :
                print (("Welcome to Facebook"),(Facebook_Username))
                running= False
            elif YesOrNo == "no":
                running = False
            else: print ("Try again")
    else: print ("Unknown User")
    
    
    

# number = 23


# while running:
#     guess = int(input('Enter an integer : '))

#     if guess == number:
#         print('Congratulations, you guessed it.')
#         # this causes the while loop to stop
#         running = False
#     elif guess < number:
#         print('No, it is a little higher than that.')
#     else:
#         print('No, it is a little lower than that.')
# else:
#     print('The while loop is over.')
#     # Do anything else you want to do here

# print('Done')


# # comment out = ctr + /