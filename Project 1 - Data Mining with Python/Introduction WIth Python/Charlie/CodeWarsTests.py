__author__ = "Connor Nelson"
from collections import Counter
import re
def array_diff(a, b):
    while b in a:
        a.remove(b)
    return a
import math 
import math
def sum_of_squares(n):
    # put your code here...
    j = n
    total = 0
    count = 0 
    arraySol = []
    while total < n and j > 0:
        if math.sqrt(j).is_integer() and total + j <= n:
            arraySol.append(j)
            total = total + j
            count = count + 1
            if n - total > j:
                j = j+ 1
        j = j - 1
    if total < n:
        count = count + n - total
    print (arraySol)
    return count
def top_3_words(text):
    return_list = []
    countFirst = 0
    first = ""
    countSecond = 0
    second = ""
    countThird = 0
    third = ""
    matcher = re.compile("[a-zA-Z']+")
    letterMatcher = re.compile("[a-zA-Z]+")
    words = matcher.findall(text) 
    for i in range(len(words)):
        words[i] = words[i].lower()
        if "'" in words[i] and letterMatcher.search(words[i]) == None:
            words.pop(i)
    if len(set(words)) == 2:
        list_tuples = Counter(words).most_common(2)
        for i in range(len(list_tuples)):
            return_list.append(list_tuples[i][0].lower())
        return return_list
    else:
        if len(set(words)) == 1:
            list_tuples = Counter(words).most_common(1)
            for i in range(len(list_tuples)):
                return_list.append(list_tuples[i][0].lower())
            return list(set(words))
    paras = Counter(words)
    list_tuples = paras.most_common(3)
    for i in range(len(list_tuples)):
        return_list.append(list_tuples[i][0].lower())
    return return_list
            
    



    # words.remove(first)
    # second = Counter(words).most_common()
    # words.remove(second)
    # third = Counter(words).most_common()
    # return [first.lower(), second.lower(), third.lower()]

    # countsFirst = words.count(words[0])
    # countsSecond = words.count(words[0])
    # countsThird = words.count(words[0])
    # for i in set(words):
    #     if words.count(i) > countFirst:
    #       thrid = second
    #       second = first
    #         first = i
    #         countFirst = words.count(i)
    #     else:
    #       if words.count(i) > countSecond:
    #         second = i
    #         countSecond = words.count(i)
    #     else:
    #       if words.count(i) > countThird:
    #         third = i
    #         countThird = words.count(i)
    # for i in range(len(set(words)))
    #   returnArray.append()
            
    

if __name__ == "__main__":
    print(top_3_words("In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income"))