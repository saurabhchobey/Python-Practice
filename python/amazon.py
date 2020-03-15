from lxml import html
import requests
from time import sleep
import time 
import schedule
import smtplib
receiver_email_id="email id of user"
def check(url):
	header={'user-agent'}

	page=requests.get(url,header=headers)
	for i in range(20):
		sleep(3)
		doc=html.fromstring(page.content)
		xpath_availablity=()
		raw_availablity=()
		availablity=()
		if raw_availablity else none
		return availablity