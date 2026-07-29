info_template = ["name", "uid", "salary"]
info = ["Akash", "237106002", "1000000"]
info_first_letter = [word[0] for word in info]
print(info_first_letter)
new_dict = dict(zip(info_template, info_first_letter))
print(new_dict)

#or

newdict = {(word for word in info_template): newword[0] for newword in info}
print(new_dict)