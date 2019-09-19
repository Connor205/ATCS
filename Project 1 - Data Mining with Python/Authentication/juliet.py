import requests
import re
import datetime
import pickle
import json
import ast
from tqdm import tqdm
from bs4 import BeautifulSoup
def get_cookie():
	""" 
	Just has my individual cookie in it
	"""
	cookie = {"PHPSESSID": "gaulgqro6fbqmr0946snt9i2r5"}
	return cookie
def get_student_dictionary_mainpage():
	"""
	Creates a dictionary of all students. The key is the id number for the student and then the value for the 
	id number is a dictionary with keys: name, gender, grade, and birthday and days_birthday. Uses datetime objects to turn 
	the days until birthday to a birthday. 
	"""
	main_page = requests.get("https://knightbook.menloschool.org/", cookies = get_cookie())
	main_page_bs = BeautifulSoup(main_page.text, "html.parser")
	student_list = main_page_bs.findAll("div", {"class" : "student-box"})
	student_dictionary = {}
	for i in student_list:
		name = i["data-name"]
		gender = i["data-gender"]
		grade = i["data-grade"]
		days_till = int(i["data-days-until-birthday"])
		today = datetime.datetime.today()
		birthday = today + datetime.timedelta(days=days_till)
		birthday = str(birthday.strftime("%B %d"))
		id_number = i["data-rid"]
		individual_dictionary = {id_number : {"name": name, "gender" : gender, "grade" : grade, "days_birthday" : days_till, "birthday" : birthday}}
		student_dictionary = {**student_dictionary, **individual_dictionary}
	return student_dictionary

def save_dictionary_to_file(dictionary, file_name):
	"""
	Saves a dictionary to a text file with the name file_name
	"""
	with open(file_name, 'w') as f:
		json.dump(dictionary, f)
	
def load_dictionary_from_file(file_name):
	"""
	loads a dictionary with the name file_name and returns it as a dictionary
	"""
	with open(file_name, 'r') as f:
		return ast.literal_eval(f.read())

def print_10_soonest_birthdays(student_dictionary):
	"""
	Uses and sorts the student dictionary in order to print out the people with the 10 soonest birthdays
	"""
	sorted_student_dict = sorted(student_dictionary.items(), key=lambda x : int(x[1]["days_until_birthday"]))
	for i in range(10):
		name = sorted_student_dict[i][1]["name"]
		grade = sorted_student_dict[i][1]["grade"]
		gender = sorted_student_dict[i][1]["gender"]
		birthday = sorted_student_dict[i][1]["birthday"]
		print(str(i + 1) +  ".", name + ", Gender:", gender + ", Grade: ", grade + ", Birthday: " + birthday)

def get_city_student(student_Id):
	"""
	Makes a request using a student id and returns the city that the student lives.
	Uses regex to parse the page for the name of the city. 
	"""
	page = requests.get("https://knightbook.menloschool.org/get_student_info.php?lookup=student_detail", cookies = get_cookie(), params = {"lookup":"student_detail", "id" : student_Id})
	page_data = str(BeautifulSoup(page.text, "html.parser"))
	city_finder = re.compile("(?<=<br\/>).+(?=,)")
	city = city_finder.findall(page_data)[0]
	return city
	#print(page_data)

def get_id_list(student_dictionary):
	"""
	Takes the student dicitonary and returns a list of studnet IDs.
	"""
	return student_dictionary.keys()

def get_city_dict(student_info):
	"""
	Uses the student dictionary to use student ids to use get_city_student() to create a dictionary 
	where the keys are the name of the city and the value is the number of menlo kids that live in 
	that city. 
	"""
	id_list  = get_id_list(student_info)
	city_dict = {}
	for i in id_list:
		city = student_info[i]["city"]
		if city not in city_dict:
			city_dict[city] = 1
		else:
			city_dict[city] = city_dict[city] + 1
	return city_dict

def print_city_count(city_dictionary):
	"""
	Uses get_city_dict and outputs turns the dictionary into readable output
	then it prints them all in order from most students to least students.
	"""
	city_dict_sorted = sorted(city_dictionary.items(), key=lambda x: -x[1])
	for i in city_dict_sorted:
		if i[1] == 1:
			print(i[0], "Has", i[1], " Menlo Student")
		else:
			print(i[0], "Has", i[1], " Menlo Students")
	# print(city_dict_sorted)

def get_all_student_info_dict(student_dictionary):
	id_list = get_id_list(student_dictionary)
	student_info = {}
	for i in tqdm(id_list):
		page = requests.get("https://knightbook.menloschool.org/get_student_info.php?lookup=student_detail", cookies = get_cookie(), params = {"lookup":"student_detail", "id" : i})
		page_data = str(BeautifulSoup(page.text, "html.parser"))
		address_finder = re.compile("(?<=target=\"_blank\">).+(?=<\/a><\/div>\n<\/div>\n<div>\n<h4>Contact<\/h4>)")
		address = address_finder.findall(page_data)[0].replace("<br/>", " ")
		birthday_string_finder = re.compile("(?<=<h4>Birthday<\/h4><div>).+(?=<\/div><\/div><\/div>\n<\/div>)")
		#birthday_string = birthday_string_finder.findall(page_data)[0]
		city_finder = re.compile("(?<=<br\/>).+(?=,)")
		city = city_finder.findall(page_data)[0]
		days_until_birthday = student_dictionary[str(i)]["days_birthday"]
		today = datetime.datetime.today()
		birthday = today + datetime.timedelta(days=int(days_until_birthday))
		birthday = str(birthday.strftime("%B %d"))
		gender = student_dictionary[str(i)]["gender"]
		grade = student_dictionary[str(i)]["grade"]
		name = student_dictionary[str(i)]["name"]
		individual_dictionary = {i : {"name" : name, "address" : address, "city" : city, "days_until_birthday" : days_until_birthday, "gender" : gender, "grade" : grade, "birthday" : birthday}}
		student_info = {**student_info, **individual_dictionary}
	save_dictionary_to_file(student_info, "student_info.json")

def change_dict_string_length(dictionary, key):
	

def load_dictionaries():
	"""
	Uses the methods to save and update the dictionaries to my computer as files
	"""
	student_dictionary = get_student_dictionary_mainpage()
	# city_dictionary = get_city_dict(student_dictionary)
	student_info = get_all_student_info_dict(student_dictionary)
	save_dictionary_to_file(student_dictionary, "mainpage_dictionary.json")
	# save_dictionary_to_file(city_dictionary, "city_dictionary.json")
	save_dictionary_to_file(student_info, "student_info.json")

if __name__ == '__main__':
	# load_dictionaries()
	loaded_city_dictionary = load_dictionary_from_file("city_dictionary.json")
	loaded_student_dictionary = load_dictionary_from_file("mainpage_dictionary.json")
	student_info = load_dictionary_from_file("student_info.json")
	# id_list = get_id_list(loaded_student_dictionary)
	# get_all_student_info_dict(loaded_student_dictionary)
	print_10_soonest_birthdays(student_info)
	print_city_count(get_city_dict(student_info))
	# print_10_soonest_birthdays(student_dictionary)
	# print(get_city_list(student_dictionary))
	# print(get_city_student("102100"))






