
import requests
from bs4 import BeautifulSoup
import re

url = "https://knightbook.menloschool.org"

human_headers = { "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "accept-language" : "en-US,en;q=0.9",
                    "accept-encoding" : "gzip, deflate, br",
                    "upgrade-insecure-requests" : "1",
                    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1147.64"
                }

session = requests.Session()
    
response = session.get(url, headers=human_headers)

#print(response.text)

response_bs = BeautifulSoup(response.text, "html.parser")

login_page = response_bs.form['action']
#print(login_page)

login_method = response_bs.form['method']
#print(login_method)

inputList =  response_bs.findAll('input')
#print(inputList)

login_inputs = {}
for tag in inputList:
	if 'name' in tag.attrs:
		login_inputs[tag['name']] = tag.get('value','')
	# print(tag.attrs)
#print(login_inputs)

#login_inputs['username'] = 'wcesarotti'

#print(response.headers)
# print(response.status_code)
# print(response.history)
print(response.history[0].headers)
#print(response.history[0].headers['Location'])
location = response.history[0].headers['Location']

server = re.match("^(https://\w+\.\w+\.\w{1,3}:?\d*)[/a-zA-Z]*",location).group(1)
print(server)

kb = session.post(server+login_page, data=login_inputs)
print(kb)
