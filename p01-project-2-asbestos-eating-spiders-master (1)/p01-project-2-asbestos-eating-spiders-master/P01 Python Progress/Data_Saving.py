import time  # Will allow for time to be stalled so the results can be viewed if needed.
def repeat_scan():
    print("reached repeat") #makes sure we reach this point so we can write the repeat
def file_open():
    file=open("data_saving.txt","a+") #opens the file for writing in append mode
    return file
def file_write(file):
    file.write(information_entering()) # writes the new scanned information. In this case it is a test sentence
    file.write("\n") # Prints a line separating the new information from the old.
    return file
#def file_close(file):
    #file=file.close()     #FUnction we currently don't and probably won't need. Here in case we need it.
    #return file
def information_entering():  # where the scanned information will go. Test right now
    test=("this is a test")
    return test
def file_read_open():
    file_r=open("data_saving.txt","r+") # Opens the file in read mode.
    return file_r
def file_purpose():
    purpose=input("Would you like to read the contents? Type y for yes or n to start scanning. Any other answer will be rejected")
    # Allows you to chose if you want to read the file or start scanning.
    return purpose
def file_print(file_r):
    scans=file_r.readlines() # Reads the test in lines so it is easier to read.
    for x in scans:
        print(x)
def main():
    answer = file_purpose()
    if answer == "y":
        file_print(file_read_open()) # Reads the file for you.
        time.sleep(6) # Gives you time to read the file contents.
    if answer == "n":
        file_write(file_open())
        repeat_scan()
    if answer!="y" and answer!="n":  # if the input was invalid it makes you re input.
        print("Sorry, invalid input. Try again")
        time.sleep(4)
        main()
main()
