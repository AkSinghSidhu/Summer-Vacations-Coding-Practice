# Write `text_analyzer(text)` that returns a dict with: word count, character count (no spaces), most common letter (case-insensitive), and count of each vowel. Call it on any sentence and print the result neatly.

def text_analyzer(text):
    arr = text.split()
    str1 = text.lower().replace(" ", "")
    print("Number of words:", len(arr))
    print("Number of Characters without spaces:", len(str1))
    my_dict = {}
    for x in str1:
        my_dict[x] = str1.count(x)

    print("Most common letter (Case Insensitive):", max(my_dict, key = str1.count) + " repeating " , max(my_dict.values()) , "times")
    countVowels = (
        str1.count("a")
        + str1.count("e")
        + str1.count("i")
        + str1.count("o")
        + str1.count("u")
    )
    print("Total Number of Vowels:", countVowels)

str = "I am a Btech Student"
text_analyzer(str)