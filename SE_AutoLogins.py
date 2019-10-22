## check chrome browser version and download/update chrome driver: http://chromedriver.chromium.org/downloads

import time
from selenium import webdriver
print('{}: START'.format(time.strftime('%d%b%Y %H:%M:%S:')))
# inputs
email = 'EMAIL'
password = 'PASSWORD'
account = 'ACCOUNT'
# open Chrome browser in incognito mode in the background
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('headless')
# sites to visit
dict_urls = {'Meta SE': 'https://meta.stackexchange.com/users/login?ssrc=head&returnurl=https%3a%2f%2fmeta.stackexchange.com%2fusers%2f399814%2f' + account,
             'SO': 'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f' + account,
             'Meta SO': 'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fmeta.stackoverflow.com%2fusers%2f4676290%2f' + account,
             'CodeReview': 'https://codereview.stackexchange.com/users/login?ssrc=head&returnurl=https%3a%2f%2fcodereview.stackexchange.com%2fusers%2f126196%2f' + account,
             'DBA SE': 'https://dba.stackexchange.com/users/login?ssrc=head&returnurl=https%3a%2f%2fdba.stackexchange.com%2fusers%2f124060%2f' + account}
# run the loop
for kk, vv in dict_urls.items():    
    # open browser and go to link
    driver = webdriver.Chrome(chrome_options = chrome_options)
    print('{}: Opening {}'.format(time.strftime('%d%b%Y %H:%M:%S:'), kk))
    driver.get(vv)
    # where to type
    field_email = driver.find_element_by_id('email')
    field_pw = driver.find_element_by_id('password')
    # text to type
    field_email.send_keys( email )
    field_pw.send_keys( password )
    # hit Enter
    field_pw.send_keys(u'\ue007')
    # sleep for some time; 7 seconds
    time.sleep(7)
    # close browser
    driver.quit()
print('{}: END\n'.format(time.strftime('%d%b%Y %H:%M:%S:')))
