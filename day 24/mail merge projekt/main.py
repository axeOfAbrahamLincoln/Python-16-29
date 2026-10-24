#TODO: Create a letter using starting_letter.txt 
#
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open("Input/Letters/starting_letter.txt") as text:
    letter = text.read()

with open("Input/Names/invited_names.txt") as names:
    list_of_names = names.readlines()
    
for name in list_of_names:
    invited_name = name.strip()
    new_letter = letter.replace("[name]", f"{invited_name}")
    file_name = f"letter_for_{invited_name}.txt"
    with open(f"Output/ReadyToSend/{file_name}", mode="w") as ready_to_send:
        ready_to_send.write(new_letter)


        

