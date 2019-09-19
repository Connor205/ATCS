import re
import email.utils
""" This module is python practice exercises to cover more advanced topics.
    Many of the exercises can be found at: 
        http://www.practicepython.org/exercises/
        https://www.hackerrank.com/domains/python/py-introduction
        (hackerrank will ask you to sign up, but you can just close the popup)
    You may submit them there to get feedback on your solutions, and for a
        discussion of how to do each exercise.
    Put the code for your solutions to each exercise in the appropriate function.
    DON'T change the names of the functions!
    You may change the names of the input parameters.
    Put your code that tests your functions in the if __name__ == "__main__": section
    Don't forget to regularly commit and push to github.
    Please include an __author__ comment so I can tell whose code this is.
"""
__author__ = "Connor Nelson"

# Practice Python Exercise
# found at http://www.practicepython.org/exercises/

# 7: List Comprehensions
def even_list_elements(input_list):
    """ Use a list comprehension/generator to return a new list that has 
        only the even elements of input_list in it.
    """
    mylist = [x for x in input_list if x % 2  == 0]
    return mylist



# 10: List Overlap Comprehensions
def list_overlap_comp(list1, list2):
    """ Use a list comprehension/generator to return a list that contains 
        only the elements that are in common between list1 and list2.
    """ 
    mylist = [x for x in list1 if x in list2]
    return mylist


# More List Comprehension Practice!
# Implement the following function:

def cube_triples(input_list):
    """ Use a list comprehension/generator to return a list with the cubes
        of the numbers divisible by three in the input_list.
    """
    mylist = [x**3 for x in input_list if x % 3 == 0]
    return mylist



# # More practice with Dictionaries, Files, and Text!
# # Implement the following functions:

def longest_sentence(text_file_name):
    """ Read from the text file, split the data into sentences,
        and return the longest sentence in the file.
    """
    print (text_file_name)
    with open(text_file_name) as f:
        passage = f.read()
        passage = passage.replace("?",".")
        passage = passage.replace("!",".")
        passage = passage.replace(";",".")
        sentences = passage.split(".")
        longest = sentences[0]
        for item in sentences:
            if len(item) > len(longest):
                longest = item
    return longest



def longest_word(text_file_name):
    """ Read from the text file, split the data into words,
        and return the longest word in the file.
    """

    print (text_file_name)
    with open(text_file_name) as f:
        passage = f.read()
        matcher = re.compile("\w+[-]?\w*[-]?\w*[-]?\w*")
        words = matcher.findall(passage)
        longest = words[0]
        for item in words:
            if len(item) > len(longest):
                longest = item
    return longest



def num_unique_words(text_file_name):
#     """ Read from the text file, split the data into words,
#         and return the number of unique words in the file.
#         HINT: Use a set!
#     """
    with open(text_file_name) as f:
        passage = f.read()
        passage = passage.lower()
        passage = passage.replace(";"," ")
        passage = passage.replace("?"," ")
        passage = passage.replace("!"," ")
        passage = passage.replace(","," ")
        passage = passage.replace("."," ")
        passage = passage.replace("("," ")
        passage = passage.replace(")"," ")
        passage = passage.replace("\n"," ")
        passage = passage.replace('"'," ")
        passage = passage.replace(":"," ")
        words = passage.split(" ")
        wordsSet = set(words)
        wordsSet = wordsSet - set({'','-'})

        return len(wordsSet)
        



def most_frequent_word(text_file_name):
    """ Read from the text file, split the data into words,
        and return a tuple with the most frequently occuring word 
        in the file and the count of the number of times it appeared.
    """
    with open(text_file_name) as f:
        passage = f.read()
        passage = passage.lower()
        passage = passage.replace(";"," ")
        passage = passage.replace("?"," ")
        passage = passage.replace("!"," ")
        passage = passage.replace(","," ")
        passage = passage.replace("."," ")
        passage = passage.replace("("," ")
        passage = passage.replace(")"," ")
        passage = passage.replace("\n"," ")
        passage = passage.replace('"'," ")
        passage = passage.replace(":"," ")
        words = passage.split(" ")
        while '' in words:
            words.remove('')
        mostPopular = words[0]
        for item in words:
            if words.count(item) > words.count(mostPopular):
                mostPopular = item
        returnString = (mostPopular, words.count(mostPopular))
    return returnString







# # Hackerrank Class Exercises
# # found at https://www.hackerrank.com/domains/python/py-classes

#Class 2 - Find the Torsional Angle
class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, other):
        newPoint = Points(other.x - self.x,other.y - self.y, other.z - self.z)
        return newPoint

    def dot(self, other):
        return self.x * other.x + self.y*other.y + self.z*other.z
    def cross(first, second):
        newPoint = Points(first.y*second.z - first.z*second.y, first.z*second.x - first.x*second.z, first.x*second.y - first.y*second.x)
        return newPoint
    def absolute(self):
         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)



#Classes: Dealing with Complex Numbers
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(x, y):
        newNum = Complex(x.real + y.real, x.imaginary + y.imaginary)
        return newNum
    def __sub__(x, y):
        newNum = Complex(x.real - y.real, x.imaginary - y.imaginary)
        return newNum
    def __mul__(x, y):
        newNum = Complex(x.real*y.real - x.imaginary*y.imaginary, x.real * y.imaginary + x.imaginary * y.real)
        return newNum
    def __truediv__(x, y):
        conjugate = Complex(y.real, -y.imaginary)
        real = x.__mul__(conjugate).real/(y.real*y.real - y.imaginary*conjugate.imaginary)
        img = x.__mul__(conjugate).imaginary/(y.real*y.real - y.imaginary*conjugate.imaginary)
        return Complex(real, img)
    def mod(self):
        real = pow(self.real*self.real + self.imaginary*self.imaginary, 1/2)
        img = 0
        return Complex(real,img)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

def runNumberTest(C, D):
    print(C.__add__(D).__str__())
    print(C.__sub__(D).__str__())
    print(C.__mul__(D).__str__())
    print(C.__truediv__(D).__str__())
    print(C.mod().__str__())
    print(D.mod().__str__())



# Hackerrank RegEx Exercises
# found at https://www.hackerrank.com/domains/python/py-regex
# If you are unfamiliar with RegEx, look here:
# A gentle introduction about what RegEx is: 
#   https://docs.python.org/3/howto/regex.html#regex-howto
# The library reference for regex in python3: 
#    https://docs.python.org/3/library/re.html

#Validating and Parsing Email Addresses
def validate_email_addresses(tester):
    """ Take a list of names and email addresses and return a list with
        only the valid ones. See the webpage for validity requirements.
    """
    print(tester)
    matcher = re.compile("[a-zA-Z]*[" "]{1}<[a-zA-Z]{1}[\w\.-]*@[a-zA-Z]+\.[A-Za-z]{1,3}>$")
    validAdresses = matcher.findall(tester)
    print (validAdresses)
    for item in validAdresses:
        print (item)

 #Regex Substitution
def sub_and_or(string_list):
#     """ Take a list of strings and return a list of strings with:
#             ' && ' replaced by ' and '
#             ' || ' replaced by ' or '
#     """
    for i in range(len(string_list)):
        repAnd = re.sub(" && ", " and ", string_list[i])
        repOr = re.sub(" \|\| ", " or ", repAnd)
        string_list[i] = repOr
    return string_list

# #Validating Credit Card Numbers
def validate_cc_numbers(ccnumber_list):
#     """ Take a list of strings and return a list with 'Valid' or 'Invalid'
#         strings in the appropriate place in the list. See the webpage for 
#         validity requirements.
#     """
    matcher = re.compile("([4-6][0-9]{15}$)|([4-6][0-9]{3}[-][0-9]{4}[-][0-9]{4}[-][0-9]{4}$)")
    notMatcher = re.compile("[0000]|[1111]|[2222]|[3333]|[[4444]|[5555]|[6666]|[7777]|[[8888]|[9999]")
    returnList = []
    for i in range(len(ccnumber_list)):
        valid = True
        if not ccnumber_list[i] == '' and re.match(matcher, ccnumber_list[i]):
            tester = ccnumber_list[i]
            tester = tester.replace("-", "")

            for i in range(len(ccnumber_list[i]) - 4):
                if tester[i] == tester[i+1] and tester[i] == tester[i+2] and tester[i] == tester[i+3]:
                    valid  = False
            if valid:
                returnList.append("Valid")
            else:
                returnList.append("Invalid")

        else:
            returnList.append("Invalid")
    return returnList      






#  Validating Postal Codes
def validate_postal_code(zipcode_list):
# #     """ Take a list of strings and return a list of 'True' or 'False' strings
# #         in the appropriate place in the list. See the webpage for validity
# #         requirements.
# #     """
    returnList = []
    for i in range(len(zipcode_list)):
        for i in range(len(zipcode_list[i]) - 2):
            numRepeats = 0
            if zipcode_list[i] == zipcode_list[i]:
                numRepeats = numRepeats + 1
            if numRepeats < 2 and int(zipcode_list[i][0]) > 0:
                returnList.append("True")
            else:
                returnList.append("False")
    return returnList









if __name__ == "__main__":
    # put your test code here
    # list = [1,2,3,4,5,6,7,8,9,10]
    # newList = [-1,0,1,2,3,4,5]
    # print (even_list_elements(list))
    # print (list_overlap_comp(list, newList))
    # print ("sentence: ", longest_sentence("permutation.txt"))
    # print ("word: ", longest_word("permutation.txt"))
    # print (num_unique_words("permutation.txt"))
    # A = Points(5,5,5)
    # B = Points(1,1,1)
    # C = A.__sub__(B)
    # print(A.dot(B))
    # A = Complex(5,5)
    # B = Complex(9,9)
    # runNumberTest(A,B)
    # with open ("i.txt") as f:
    #     input = f.read()
    #     validate_email_addresses(input)
    # print(sub_and_or([" || ", "sjfnjsb", " && hsdhdf"]))
    print (validate_postal_code(["012345", "112233", "121345"]))
    print(most_frequent_word("rj_prologue.txt"))
    print(validate_cc_numbers(['4253625879615786', '4424424424442444', '5122-2368-7954-3214', '42536258796157867', '4424444424442444 ', '5122-2368-7954 - 3214', '44244x4424442444', '0525362587961578', '4123456789123456', '5123-4567-8912-3456', '61234-567-8912-3456', '4123356789123456', '5133-3367-8912-3456', '5123 - 3567 - 8912 - 3456', '']))