import requests as requests
from bs4 import BeautifulSoup



url = 'http://rate.am/'
response = requests.get(url, headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'})

response_html = response.text
soup = BeautifulSoup(response_html, 'html.parser')


curr_lst = []
for bobo in soup.select('table#rb option'):
    curr_lst.append(bobo.get_text())

curr_lst = curr_lst[0:4]


value_lst = []

for bobo in soup.findAll('td', class_="fhd"):
    value_lst.append(bobo.get_text())
value_lst = value_lst[-9:-1]




arq_val = []
for i in range(0,8,2):
    arq_val.append(value_lst[i])
    arq_dict = dict(zip(curr_lst, arq_val))


vach_val = []
for i in range(1,8,2):
    vach_val.append(value_lst[i])
    vacharq_dict = dict(zip(curr_lst, vach_val))



