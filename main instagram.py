import requests
import json
import json
from selenium.webdriver import Chrome
from time import sleep
from random import randint
import pandas as pd
driver = Chrome("C:/users/user/chromedriver/chromedriver.exe")
driver.get('https://instagram.com')
input("****Login*****")


# Add more usernames here
usernames = ["elenagrady.realtormiami","whoaview"]
all_d = []
for username in usernames:
	try:
		driver.get("https://www.instagram.com/" + username + '/?__a=1')
		inh = driver.find_element_by_xpath("//pre").get_attribute("innerHTML")
		data = json.loads(inh)
		f = dict()
		f['username'] = username
		try:
			f['web'] = data['graphql']['user']['external_url']
		except:
			pass

		try:
			f['bio'] = data['graphql']['user']['biography']
		except:
			pass

		try:
			f['business_address'] =  data['graphql']['user']['business_address_json']
		except:
			pass

		try:
			f['email'] =  data['graphql']['user']['business_email']
		except:
			pass

		try:
			f['phone'] =  data['graphql']['user']['business_phone_number']
		except:
			pass

		try:
			f['category'] =  data['graphql']['user']['category_name']
		except:
			pass

		try:
			f['follower'] =  data['graphql']['user']['edge_followed_by']['count']
		except:
			pass

		try:
			f['following'] =  data['graphql']['user']['edge_follow']['count']
		except:
			pass

		try:
			f['fullname'] =  data['graphql']['user']['full_name']
		except:
			pass

		
		for k,v in f.items():
			print(f'{k} - {v}')
		all_d.append(f)

		df = pd.DataFrame(all_d)
		df.to_csv('output.csv')
	except Exception as e:
		print(e)
		print("Chude Gese")

	print('\n')

	sleep(randint(10,15))
	# Code for saving output