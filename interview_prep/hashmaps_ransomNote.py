#  easy

def checkMagazine(magazine, note):
    mag_dict = {}
    res = "Yes"
    # Step 1: create a dictionary with words in magazine with their frequencies as values
    for word in magazine:
        if word in mag_dict:
            mag_dict[word] += 1
        else:
            mag_dict[word] = 1

    # Step 2: create a loop of words to compare with words in magazine
    for word in note:
        if word in mag_dict and mag_dict[word] > 0:
            mag_dict[word] -= 1
        else:
            res = "No"

print(res)