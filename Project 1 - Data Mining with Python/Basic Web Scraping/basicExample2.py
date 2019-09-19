from urllib.request import urlopen
from urllib.request import Request
req_url = Request("http://diggercomic.com", headers={ "User-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.112 Safari/537.36 Vivaldi/1.91.867.48"})
html = urlopen(req_url)
print(html.read())