import os

address = "requirements.txt"  ##change the address

def file_reader():
    
    try:
        text = 'pip install -r "{}"'.format(address)
        os.system(text)        
        
    except FileNotFoundError: print("Sorry, we could not found the requrirements file in the specified directory, try giving the full address")

file_reader()