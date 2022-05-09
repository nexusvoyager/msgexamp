import random
import socket
import time

print("Do you want to start this program? \n disclaimer: This program is meant for demonstration and educational purposes, no data will be sent to the developers of this test tool, its just a fun tool to play with! Have fun <3 and be sure to star the project on github")
print("FYI This was created as a thing as a school to demonstrate what data is usually associated with messages, some help was from github copiolet (mainly the ip grabbing and your data is not being stolen, you can check the code if you'd like!)")
starter = input("Y/N: ")

if starter == "Y" or starter == "y":
    print("Starting...")
    ##Add a 3 second waiting time
    time.sleep(3)
    usr_name = input("> Prompt a Name \n> ")
    msg_contents = input("> Message please! \n> ")

    ##generate a random string of 7 digits
    msg_id = ''.join(random.choice('0123456789') for i in range(7))

    ## Detect ip adresss
    ip_address = socket.gethostbyname(socket.gethostname())


    ## Print the message
    print("-----------------------")
    print("Name:", usr_name)
    print("Message:", msg_contents)
    print("Message ID:", msg_id)
    print("IP Address:", ip_address)
    print("-----------------------")

