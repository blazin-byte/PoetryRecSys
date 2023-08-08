#%%
#Imports
import pandas as pd
import random


#%% 

#Downloaded Poetry Data
df = pd.read_csv('Data\\poetryfoundation.csv')
print(df.head(5))


def getFloat():
    """
    Repeatedly prompts user until a float is recieved
    """
    while True:
        try:
            num = float(input("Please Enter Rating (0.0-5.0): \n"))
            return num
        except ValueError:
            promptselect = random.randint(1,5)
            if promptselect == 1: print("Alright haha very funny. Just give me a number")
            if promptselect == 2: print("Listen up bitch. Did I ask for this funny business?")
            if promptselect == 3: print("Can I get them digits? Pweaseee")
            if promptselect == 4: print("Dont fuck with me bitch! I asked for a motherfucking number, not this fucking bullshit!")

def getValidateRating():
    """
    No input, returns a float rating between 0 and 5
    """
    while True:
        num = getFloat()
        if num < 0.0:
            print("Wow really hated that poem huh? 0 is the lowest acceptable answer")
            continue
        if num > 5.0:
            print("Jesus, I get that you liked the poem but please keep it in the specified bounds")
            continue
        else: 
            return num

#rating = getValidateRating()                

#Now what?



# %%
"""
Here's your plan:
1. Get 1 basic dataset to feed into the rec sys process
2. Build the model out
3. Then go back and add further more datasets
4. Use more algorithms to possibly translate poems and classify the language'

But hey! Focus. Grab just one dataset and build the model!
I'm trying to select a dataset but how important are tags and which tags do I need?
    Need to watch the videos for this I think
"""
