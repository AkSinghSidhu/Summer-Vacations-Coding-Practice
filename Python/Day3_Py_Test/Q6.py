# Write `text_analyzer(text)` that returns a dict with: word count, character count (no spaces), most common letter (case-insensitive), and count of each vowel. Call it on any sentence and print the result neatly.

def text_analyzer(text):
    arr = text.split()
    str1 = text.lower().replace(" ", "")
    my_dict = {}
    for x in str1:
        my_dict[x] = str1.count(x)
    dictionary = {"No. of words" : len(arr),
                  "No. of Characters without spaces" : len(str1),
                  "Most common letter (case-insensitive)" : max(my_dict, key = str1.count),
                  "Count of each vowel" : {"a" : str1.count("a"),
                                           "e": str1.count("e"),
                                           "i": str1.count("i"),
                                           "o": str1.count("o"),
                                           "u": str1.count("u"),
                                           }
                  }
    return dictionary

sentence = "I am a Btech Student"
print(text_analyzer(sentence))