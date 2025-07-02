#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as invited_people:
    list_of_people = invited_people.read().splitlines()

with open("./Input/Letters/starting_letter.txt") as starting_email:
    content = starting_email.read()
    for name in list_of_people:
        file_with_new_name = content.replace("[name]",f"{name}")
        with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as email:
            email.write(file_with_new_name)
