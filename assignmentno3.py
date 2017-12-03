# Author : Kishor shrestha
#  Write a function which accepts your friend's name as a argument and prints a Happy Birthday song for him/her.

def singasong(nameoffriend = ''):
    print(" {0} \n {0} \n Happy Birthday dear {1}".format("Happy Birthday to you",nameoffriend))

singasong(str(input("Enter Your Friend name : ")))