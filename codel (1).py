import os
#IMPORTING OS LIBRARY TO USE LINUX OPERATING SYSTEM COMMAND

import time
#IMPORTING TIME LIBRARY TO VIEW CURRENT DATE AND TIME

import webbrowser
#IMPORTING WEBBROWSER LIBRARY TO OPEN WEBBROWSER



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



x='''
print "1. CHANGE CURRENT DATE AND TIME"
print "2. TO CREATE A FILE"
print "3. TO CREATE A DIRECTORY"
print "4. TO SEARCH SOMETHNG ON GOOGLE"
print "5. LOGOUT YOUR SYSTEM"
print "6. REBOOT YOUR OS"
print "7. TO CHECK INTERNET CONNECTION IN YOUR PC/LAPTOP"
print "8. TO LOGIN WATSAPP ON BROWSER"
print "9. TO CHECK ALL CONNECTED IP IN YOUR NETWORK"
'''
print x


choice=int(raw_input("ENTER YOUR CHOICE: "))
#TAKIING THE CHOICE FROM USER

if choice==1 :
#CHOICE 1 i.e., TO DISPLAY CURRENT DATE AND TIME

	print "SHOWING CURRENT DATE....", time.ctime().split()[1:3]
	#SHOWING CURRENT DATE

	print "SHOWING CURRENT TIME...", time.ctime().split()[3]
	#SHOWING CURRENT TIME

elif choice==2 :
#CHOICE 2 i.e., TO CREATE A FILE

	msg3='CREATING A FILE...'
	os.system('echo '+msg3+' | festival --tts')
	#SENDING THE MESSAGE TO USER IN VOICE FORMAT

	time.sleep(3)
	#TO MAKE DELAY BY 3 SECONDS

	os.system('touch file.txt')
	#CREATING FILE


elif choice==3 :
#CHOICE 3 i.e., TO CREATE A DIRECTORY

	msg4='CREATING A DIRECTORY...'
	os.system('echo '+msg4+' | festival --tts')
	#SENDING THE MESSAGE TO USER IN VOICE FORMAT
	
	time.sleep(4)
	#TO MAKE DELAY BY 4 SECONDS

	os.system('mkdir directory')
	#CREATING DIRECTORY
	

elif choice==4 :
#CHOICE 4 i.e., TO SEARCH SOMETHNG ON GOOGLE

	print "SEARCHING ON GOOGLE..."
	msg=raw_input("Type to search")
	#TAKING WHAT TO SEARCH FROM USER AS INPUT

	webbrowser.open_new_tab('http://www.google.com/search?q='+msg)
	#OPENS GOOGLE AND SEARCH FOR WHAT INPUT

elif choice==5 :
#CHOICE 5 i.e., TO LOGOUT 

	msg5='LOGGING OUT..'
	os.system('echo '+msg5+' | festival --tts')
	#SENDING THE MESSAGE TO USER IN VOICE FORMAT

	time.sleep(4)
	#TO MAKE DELAY BY 4 SECONDS
	
elif choice==6 :
#CHOICE 6 i.e., TO REBOOT SYSTEM

   	msg1='CLOSE ALL YOUR APPS, SYSTEM IS REBOOTING'
	os.system('echo '+msg1+'| festival --tts')
	#SENDING THE MESSAGE TO USER IN VOICE FORMAT

	time.sleep(2)
	#TO MAKE DELAY BY 2 SECONDS


	msg2='WAITITNG FOR APPS TO GET CLOSED'
	os.system('echo '+msg2+'| festival --tts')
	#SENDING THE MESSAGE TO USER IN VOICE FORMAT

	time.sleep(3)
	#TO MAKE DELAY BY 3 SECONDS

	os.system('reboot')
	#TO REBOOT SYSTEM
	
elif choice==7 :
#CHOICE 7 i.e., TO CHECK INTERNET CONNECTION	

	msg6='CHECKING INTERNET COLLECTION...'
	os.system('echo '+msg6+' | festival --tts')
	#SENDING THE MESSAGE TO USER IN VOICE FORMAT

	time.sleep(4)
	#TO MAKE DELAY BY 4 SECONDS

	os.system('ping www.google.com')
	

elif choice==8 :
#CHOICE 8 i.e., LOGGING INTO WATSAPP



	msg7='LOGING WATSAPP...'
	os.system('echo '+msg7+' | festival --tts')
	#SENDING THE MESSAGE TO USER IN VOICE FORMAT

	time.sleep(3)
	#TO MAKE DELAY BY 3 SECONDS
	
	 
	# Replace below path with the absolute path
	# to chromedriver in your computer
	driver = webdriver.Chrome('/root/Downloads')
	 
	driver.get("https://web.whatsapp.com/")
	wait = WebDriverWait(driver, 600)
	 
	# Replace 'Friend's Name' with the name of your friend 
	# or the name of a group 
	target = '"Monika"'
	 
	# Replace the below string with your own message
	string = "Message sent using Python!!!"
	 
	x_arg = '//span[contains(@title,' + target + ')]'
	group_title = wait.until(EC.presence_of_element_located((
	    By.XPATH, x_arg)))
	group_title.click()
	inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
	input_box = wait.until(EC.presence_of_element_located((
	    By.XPATH, inp_xpath)))
	for i in range(100):
	    input_box.send_keys(string + Keys.ENTER)
	    time.sleep(1)

elif choice==9 :
#CHOICE 9 i.e., CHECKING HOW MANY COMPUTERS ARE CONNECTED TO THE IP ADDRESS

	msg8='CHECKING IPs...'
	os.system('echo '+msg8+' | festival --tts')
	#SENDING THE MESSAGE TO USER IN VOICE FORMAT

	time.sleep(3)
	#TO MAKE DELAY BY 3 SECONDS

	msg9='WHAT IS MY IP ADDRESS'
	os.system('ifconfig')

else :
#ANY OTHER CHOICE i.e., THE USER ENTERED A WRONG CHOICE

	print "WRONG CHOICE"





