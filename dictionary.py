import json
import difflib
data=json.load(open(r"C:\Users\samir\OneDrive\Desktop\python projects\Dictionary\data.json"))

def meaning(word):
    word=word.lower()
    if word in data:
        output=data[word]
        if type(output)==list:
            for item in output:
                print(item)

    elif word.title() in data:
        output =data[word.title()]
        if type(output)==list:
            for item in output:
                print(item)
        
    elif word.upper() in data:
        output=data[word.upper()]
        if type(output)==list:
            for item in output:
                print(item)

    elif len(difflib.get_close_matches(word,data.keys()))>0:
        print("Did you mean  %s"%difflib.get_close_matches(word,data.keys())[0])
        x=input("Press y for yes & n for no :")
        if x=="y":
            output=data[difflib.get_close_matches(word,data.keys())[0]]
            if type(output)==list:
                for item in output:
                    print(item)
                
        elif x=="n":
            print("word is not present in dictionary")

        else:
            print("you may have entered wrong word")

print("***************************")
print("        DICTIONARY         ")
print("***************************")
word=input("Enter the word whose meaning you need to find out :")
meaning(word)
