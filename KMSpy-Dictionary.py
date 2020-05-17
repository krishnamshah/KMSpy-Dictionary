import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    if w in data:
        w = w.lower()
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn= input("Did you mean %s instead? Enter Y for yes, or N for no." % get_close_matches(w,data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didnt understand your entry."
    else:
        return "The word doesn't exist. Please double check it"
print(" ----- Dictionary -----")
word = input("Enter word to find the meaning: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print("-"+item)
else:
    print(output)
