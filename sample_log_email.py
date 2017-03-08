#!/usr/bin/env python
# -*- coding: utf-8 -*-


# python sample log email.py       : runs code 
# python sample log email.py test  : tests the code without sending any emails
# python sample log email.py check : send only email to shaungarnett@gmail.com


import os
import sys
import fnmatch
import time
import datetime
import subprocess

base_path = '/blackburn3/scripts/email'
calibration_folder = '/blackburn3/RAW_Data/Q_Exactive_2014/Xcalibur/Calibration'
message_file = '%s/automated_message.txt' %(base_path)
time_file = '%s/time.txt' %(base_path)
sample_log_time_file = '%s/sample_log_time.txt' %(base_path)
path = '/blackburn3/RAW_Data/Q_Exactive_2014'
ref_path = "/mnt/BLACKBURNLAB/QC/Reference"
sample_log_path = '/mnt/BLACKBURNLAB/QC/Sample_Logs'

def copy_Ref(path,ref_path,last_time):

	#ref_time_file = '%s/ref_time.txt' %(base_path)
	#last_time = os.path.getmtime(ref_time_file)
	print '\n\nCOPY REF files\n'
	#print last_time
	#print(datetime.datetime.fromtimestamp(int("1284101485")).strftime('%Y-%m-%d %H:%M:%S'))
	word_date = datetime.datetime.fromtimestamp(int(last_time)).strftime('%Y %B %d')
	#print time.strftime("%B %d %Y", str(int(last_time)))
	#raw_input()
	print word_date
	#word_date = raw_input('enter word date : ') #ucomment to customise start date for ref
	date_split = word_date.split(' ')
	year_entry = date_split[0]
	month_entry = date_split[1]
	year_path = '%s/%s' %(path,year_entry)
	month_path = '%s/%s' %(year_path,month_entry)
	#print year_path
	#print month_path

	if not os.path.exists(month_path):
		print("\n\n*****************************\n\n%s \ndoes not exist\nfix this\nprobably misspelt on QE computer\n\n**************************\n\n" %(month_path))


	ref_year_path = '%s/%s' %(ref_path,date_split[0])
	if not os.path.exists(ref_year_path):
		cmd = 'mkdir %s' %(ref_year_path)
		os.system(cmd)
	ref_month_path = '%s/%s' %(ref_year_path,date_split[1])
	if not os.path.exists(ref_month_path):
		cmd = 'mkdir %s' %(ref_month_path)
		os.system(cmd)
	#raw_input()

	file_list = ['*REF*.raw','*Ref*.raw','*ref*.raw']
	refs = []
	for file_name in file_list:
		for root, dirnames, filenames in os.walk(month_path):
  			for filename in fnmatch.filter(filenames, file_name):
				refs.append(os.path.join(root, filename))
	

	for file_path in refs:
		#print file_path
		file_time = os.path.getmtime(file_path)
		if file_time > last_time:
			cmd = 'cp %s %s' %(file_path, ref_month_path)
			print(cmd)
			os.system(cmd)

			#raw_input('hit')
	#raw_input()
#standard_message = """
#\n\nThis is an automated mail service
#A program located in /blackburn3/scripts/email check is the a pptx file in D:Data on the QE has been updates 
#since the last email, if it has then the new file is emailed at 11am. 
#To remove yourself from this mailing list, remove your email from the email_list.txt file
#"""
#

read_message = open(message_file,'r')
message = read_message.readlines()
read_message.close()
#print(message)
message_line = '\n'.join(message)
#print message_line

#raw_input()



email_file_path = '%s/email_list.txt' %(base_path)
email_file_path = '/blackburn3/RAW_Data/Q_Exactive_2014/Xcalibur/Calibration/email_list.txt'
read_file = open(email_file_path,'r')
read_list = read_file.readlines()
read_file.close()
#print read_list
email_list = []
for entry in read_list:
	email_list.append(entry.replace('\n','').replace('\r',''))
email_line = ','.join(email_list)
developer_email_line = 'shaungarnett@gmail.com'
#print email_line
#raw_input()



last_sample_log = os.path.getmtime(sample_log_time_file)
last_time = os.path.getmtime(time_file)

print(last_time)
word_date = datetime.datetime.fromtimestamp(int(last_time)).strftime('%Y %B %d : %H %M')
print word_date
#raw_input()
#print(datetime.datetime.fromtimestamp(last_time))
#last_time = 1434400000
#print(datetime.datetime.fromtimestamp(last_time))
#raw_input()
folder_list = os.listdir(path)
#print(folder_list)



################### TEST ##########################

test = False
try:
	test = sys.argv[1] 
	#is test == 'test' command will be printed but email not actually sent
	#ckeck will send email to me, but not update time file
	email_line = 'shaungarnett@gmail.com'
	#last_time = 1434400000
	#print test
	#print email_line
	#print last_time
	os.system('clear')
	print email_line
	print '\nLast time'
	print last_time
	print datetime.datetime.fromtimestamp(int(last_time)).strftime('%d %B %Y : %H %M')
	if test != 'check':
		day = 86400
		last_time = last_time-day
		print '\nOne Day Before'
		print last_time
		print datetime.datetime.fromtimestamp(int(last_time)).strftime('%d %B %Y : %H %M')
		if test == 'test':
			print '\nOne Month Before (default for test)'
			last_time = last_time - 29*day
			print last_time
			print datetime.datetime.fromtimestamp(int(last_time)).strftime('%d %B %Y : %H %M')
		new_time = raw_input('enter new time as integer : ')
		if new_time != '':
			last_time = float(new_time)
			print last_time
		while new_time != '':
			print new_time
			print datetime.datetime.fromtimestamp(int(new_time)).strftime('%d %B %Y : %H %M')
			new_time = raw_input('enter new time as integer : ')
			print [new_time]
			if new_time != '':
				last_time = float(new_time)
				print last_time
		print '\n This is the date to be used to run the test \n'
		print last_time
		print datetime.datetime.fromtimestamp(int(last_time)).strftime('%d %B %Y : %H %M')
		raw_input('test : enter to continue ...')
except:
	print "EMAIL LIST\n"
	print email_line

#raw_input()	

############# SAMPLE LOG ############################


print '\n\n SAMPLE LOG \n'
print path

matches = []
for root, dirnames, filenames in os.walk(path):
  for filename in fnmatch.filter(filenames, '*.pptx'):
    matches.append(os.path.join(root, filename))


file_list = []

#print matches
ppt_time = 0
for file_path in matches:
	file_time = os.path.getmtime(file_path)
	#print file_time
	#print file_path
	#print 'file : ' + str(datetime.datetime.fromtimestamp(file_time))
	#print 'last : ' + str(datetime.datetime.fromtimestamp(last_time))
	#print file_time
	#print last_time
	#print '\n'
	if file_time > last_time:
		#file_path_name = file_path.replace(' ','\ ')
		file_list.append(file_path)
		#print file_path
		#print file_path_name
		#print file_time
		#print 'file : ' + str(datetime.datetime.fromtimestamp(file_time))
		#print last_time
		#print 'last : ' + str(datetime.datetime.fromtimestamp(last_time))
	if '.pptx' in file_path:
		if file_time > ppt_time:
			ppt_time = file_time

		#raw_input('enter ...')
        	
#raw_input()
print file_list
#raw_input()
hit = 0
now_date = str(datetime.datetime.fromtimestamp(file_time)).split(' ')[0]
if file_list == []:
	print '\n\nno changes to SAMPLE LOG\n'
	#cmd = "echo 'The sample log has not been updated toady' | mail -s 'Sample Log - No Update' %s" %(email_line)
	#cmd = "mail -s 'Sample Log - Not Updated' %s < %s" %(email_line,message_file)
	#print cmd
	now_ms = time.time()
	#print ppt_time
	#print  now_ms
	diff_time = now_ms - ppt_time
	hour_time = diff_time/3600
	#print(diff_time)
	#print hour_time
	day_time = round(diff_time/86400,1)
	#print day_time
	hour = datetime.datetime.fromtimestamp(int(now_ms)).strftime('%H')
	#raw_input(hour)
	if day_time < 0:
		if day_time > 1 and int(hour) < 11:
			cmd = "mail -s 'Sample Log - %s days since last update' %s < %s" %(round(day_time,0),email_line,message_file)
			print cmd
			if test != 'test':
				os.system(cmd)
	else:
		cmd = "mail -s 'Sample Log - WORKING BUT NOT BEING USED : %s days since last update' %s < %s" %(round(day_time,0),developer_email_line,message_file)
		print cmd
		if test != 'test':
			os.system(cmd)
	
else:
	#file_line = ','.join(file_list)
	for file_path in file_list:
		
		#print file_path
		file_time = os.path.getmtime(file_path)
		file_date = str(datetime.datetime.fromtimestamp(file_time)).split(' ')[0]
		file_entry_list = file_path.split('/')
		file_entry_name = file_entry_list[len(file_entry_list)-1]
		print datetime.datetime.fromtimestamp(int(file_time)).strftime('%d %B %Y : %H %M')
		cmd = "echo 'sample log : %s' | mail -s 'Sample Log' -a %s %s" %(file_entry_name,file_path.replace(' ','\ '),email_line)
		#cmd = "mail -s 'Sample Log' -t %s -A %s < %s" %(email_line,file_path,message_file)
		#cmd = 'echo "automated message from : \\blackburn3\\scripts\\email\\email_log.py" | mail -s "Sample Log" -a %s %s' %(file_path,email_line)
		print cmd
		if test != 'test':
			os.system(cmd)
		hit == 1
		if test != 'test' and test != 'check':
			append_file = open(sample_log_time_file,'a')
			append_file.write('%s\n%s\n\n' %(now_date,cmd))
			append_file.close()
			print '\nupdated %s\n' %(sample_log_time_file)
		word_date = datetime.datetime.fromtimestamp(int(file_time)).strftime('%Y %B %d')
		date_split = word_date.split(' ')
		sample_log_path = '/mnt/BLACKBURNLAB/QC/Sample_Logs'
		sample_log_year_path = '%s/%s' %(sample_log_path,date_split[0])
		if not os.path.exists(sample_log_year_path):
			cmd = 'mkdir %s' %(sample_log_year_path)
			os.system(cmd)
		cmd = "cp %s %s" %(file_path,sample_log_year_path)
		print cmd
		#raw_input()
		if test != 'test':
			os.system(cmd) 
		#raw_input('enter 2 ...')
print '\n\nDocuments\n'
print calibration_folder
calibration_list = []		
extra_file_list = ['QE_Operation_Proceedure.docx','QE_Calibration_Log.xlsx','Sample_Log_Template.pptx','email_list.txt']
for extra_name in extra_file_list:
	file_list = os.listdir(calibration_folder)
	if extra_name in file_list:
		calibration_file = '%s/%s' %(calibration_folder,extra_name)		
		file_time = os.path.getmtime(calibration_file)
		if file_time > last_time:
			print '\n\nDocuments\n\n'
			#print extra_name
			file_date = str(datetime.datetime.fromtimestamp(file_time)).split(' ')[0]
			if extra_name == 'QE_Operation_Proceedure.docx':			
				update_file_name = '%s/%s'%(calibration_folder,'update.txt')
				update_file = open('%s/%s'%(calibration_folder,'update.txt'),'r')
				update_list = update_file.readlines()
				update_file.close()
				update_line = '\n'.join([file_date]+update_list)
				#raw_input(update_list)
				#raw_input(update_line)
				#cmd = "echo '%s' | mail -s '%s' -a %s '%s'" %(update_line,extra_name,calibration_file,email_line)
				#cmd = "mail -s 'Sample Log - %s days since last update' %s < %s" %(day_time,email_line,message_file)
				#cmd = '(cat "%s"; uuencode "%s" "%s") | mail -s "%s" %s' %(update_file_name,calibration_file,calibration_file,extra_name,email_line)
				print datetime.datetime.fromtimestamp(int(file_time)).strftime('%d %B %Y : %H %M')
				cmd = "echo '%s' | mail -s '%s' -a %s %s" %(file_date,extra_name,calibration_file,email_line)
				print cmd
				#raw_input()
				if test != 'test':   
					os.system(cmd)
				#raw_input()
				hit = 1
			else:
				cmd = "echo '%s' | mail -s '%s' -a %s %s" %(file_date,extra_name,calibration_file,email_line)
				print cmd
				if test != 'test':
					os.system(cmd)
				hit = 1
			os.system('cp %s /mnt/BLACKBURNLAB/Proteomic_Documents/Protocols/Q_Exactive/' %(calibration_file))
		else:
			print '\n\nNO CHANGES IN %s\n\n' %(extra_name)



################# METHODS #############################


methods_dir = "/blackburn3/RAW_Data/Q_Exactive_2014/Xcalibur/methods/Dionex"	
print "\n\nMethods\n"
print methods_dir
methods = []
meth_hit = 0

file_list = ['*.meth']
refs = []
for file_name in file_list:
	for root, dirnames, filenames in os.walk(methods_dir):
		for filename in fnmatch.filter(filenames, file_name):
			methods.append(os.path.join(root, filename))
#print methods

for method_path in methods:
	file_time = os.path.getmtime(method_path)
	method_split = method_path.split('/')
	method_name = method_split[len(method_split)-1]
	#print method_path
	#print datetime.datetime.fromtimestamp(int(file_time)).strftime('%d %B %Y : %H %M')
	if file_time > last_time:
		meth_hit = 1		
		file_date = str(datetime.datetime.fromtimestamp(file_time)).split(' ')[0]
		print datetime.datetime.fromtimestamp(int(file_time)).strftime('%d %B %Y : %H %M')
		cmd = "echo '%s : %s' | mail -s 'Method Changed' -a %s %s" %(method_name,file_date,method_path,email_line)
		print cmd
		if test != 'test':
			os.system(cmd)
if meth_hit == 0:
	print '\n\nNO CHANGES IN %s\n\n' %("Methods")
			
		


#################### PILOTS ###########################

#print 
pilot_path = "/mnt/BLACKBURNLAB/QC/Pilots/TSQ/"
print '\n\nPILOTS\n'
print pilot_path

email_file_path = '%s/pilot_email_list.txt.txt' %(pilot_path)
#email_file_path = '/blackburn3/RAW_Data/Q_Exactive_2014/Xcalibur/Calibration/email_list.txt'
read_file = open(email_file_path,'r')
read_list = read_file.readlines()
read_file.close()
#print read_list
pilot_email_list = []
for entry in read_list:
	pilot_email_list.append(entry.replace('\n','').replace('\r',''))
pilot_email_line = ','.join(pilot_email_list)
#print pilot_email_line

pilots = []
for root, dirnames, filenames in os.walk(pilot_path):
  for filename in fnmatch.filter(filenames, '*.pptx'):
    pilots.append(os.path.join(root, filename))

ppt_time = 0
pilot_hit = 0
for file_path in pilots:
	file_time = os.path.getmtime(file_path)
	if file_time > last_time:
		#print file_path

		pilot_hit = 1
		file_time = os.path.getmtime(file_path)
		file_date = str(datetime.datetime.fromtimestamp(file_time)).split(' ')[0]
		file_entry_list = file_path.split('/')
		file_entry_name = file_entry_list[len(file_entry_list)-1]
		print datetime.datetime.fromtimestamp(int(file_time)).strftime('%d %B %Y : %H %M')
		cmd = "echo 'Pilot log : %s' | mail -s 'Pilot Log' -a %s %s" %(file_entry_name,file_path.replace(' ','\ '),pilot_email_line)
		print cmd
		if test != 'test':
			os.system(cmd)
		hit = 1
if pilot_hit == 0:
	print '\n\nNO CHANGES IN %s\n\n' %("Pilot Log")




################# Reference Log ########################


print '\n\nReference Log\n'
print ref_path
refs = []
for root, dirnames, filenames in os.walk(ref_path):
  for filename in fnmatch.filter(filenames, '*.pptx'):
    refs.append(os.path.join(root, filename))
ref_hit = 0
for file_path in refs:
	file_time = os.path.getmtime(file_path)
	
	if file_time > last_time:
		#print file_path
		ref_hit = 1

		file_time = os.path.getmtime(file_path)
		file_date = str(datetime.datetime.fromtimestamp(file_time)).split(' ')[0]
		file_entry_list = file_path.split('/')
		file_entry_name = file_entry_list[len(file_entry_list)-1]
		if file_entry_name[0] != '':
			print file_entry_name[0:2]
			if file_entry_name[0:2] != '~$':
				print datetime.datetime.fromtimestamp(int(file_time)).strftime('%d %B %Y : %H %M')
				cmd = "echo 'Reference Log : %s' | mail -s 'Reference Log' -a %s %s" %(file_entry_name,file_path.replace(' ','\ '),email_line)
				print cmd
				if test != 'test':
					os.system(cmd)
			else:
				print 'Reference Log not saved yet'
		else:
			print 'not emailing %s' %(file_entry_name)
if ref_hit == 0: 
	print '\n\nNO CHANGES IN %s\n\n' %("Reference Log")




######### MQ SUMMARY - summary ###############

print '\n\nSummarising the Summary files\n'
print ref_path
refs = []
for root, dirnames, filenames in os.walk(ref_path):
  for filename in fnmatch.filter(filenames, 'summary.txt'):
    refs.append(os.path.join(root, filename))


summary_hit = 0
time_list = []
for file_path in refs:
	file_time = os.path.getmtime(file_path)
	time_list.append(file_time)
	if file_time > last_time:
		summary_hit = 1
#summary_hit = 1
if summary_hit == 1:
	cmd = 'python /mnt/BLACKBURNLAB/scripts/QC/QC_summary.py /mnt/BLACKBURNLAB/QC/Reference/ %s' %(last_time)
	print cmd

	#p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	os.system(cmd)
	file_1 = '/mnt/BLACKBURNLAB/QC/Reference/summary/Peptide.Sequences.Identified_email.png'
	file_2 = '/mnt/BLACKBURNLAB/QC/Reference/summary/RAW_email.png'
	for summary_file_name in [file_1]:
		print_file_name = summary_file_name.split('/')[-1]
		message = """
		Image generated from the MaxQuant summary.txt file for the Reference Samples
		
		An interactive R Shiny app can be found at

		http://watson:3838/MQ_summary.Rmd
		Horizontal lines
		green 		 	: maximum for C1 600ng
		lightgreen 	 	: 80% of maximum for C1
		greenyellow 	: mean for C1 600ng

		red 			: maximum for C2 600ng
		lightcoral 		: 80% of maximum for C2
		magenta 		: mean for C1 600ng 
		"""

		cmd = "echo '%s' | mail -s 'MaxQuant summary.txt' -a %s -a %s %s" %(message,file_1,file_2,email_line)
		print cmd
		#if test != 'test':
		os.system(cmd)
else:
	print 'no new summmary.txt file since \t:\t%s' %(datetime.datetime.fromtimestamp(int(max(time_list))).strftime('%d %B %Y : %H %M'))
	#print max(time_list)

#raw_input('MQ - summary')
##### Calibration Summary  ##########

# print '\n\nSummarising the Calibration Log files\n'
# calibration_path = '/blackburn3/RAW_Data/Q_Exactive_2014/Xcalibur/system/Exactive/log'
# refs = []
# for root, dirnames, filenames in os.walk(calibration_path):
#   for filename in fnmatch.filter(filenames, 'Thermo*'):
#     refs.append(os.path.join(root, filename))

# #print refs
# time_list = []
# for file_path in refs:
# 	file_time = os.path.getmtime(file_path)
# 	time_list.append(file_time)
# 	if file_time > last_time:
# 		summary_hit = 1

# #summary_hit = 1
# if summary_hit == 1:
# 	cmd = 'python /mnt/BLACKBURNLAB/scripts/QC/run_calibration_summary.py /mnt/BLACKBURNLAB/scripts/QC/ /mnt/BLACKBURNLAB/QC/QE_calibration/ %s' %(last_time)
# 	print(cmd)
# 	os.system(cmd)
# 	message = """
# 	Summary of the information in Xcalibur/system/Exactive/log/Thermo Exactive ...
# 	"""
# 	calibration_summary_file_name = '/mnt/BLACKBURNLAB/QC/QE_calibration/calibration.pdf'
# 	cmd = "echo '%s' | mail -s 'MaxQuant summary.txt' -a %s %s" %(message,calibration_summary_file_name,'shaungarnett@gmail.com')
# 	print cmd
# 	#if test != 'test':
# 	#	os.system(cmd)
# else:
# 	print 'no new calibration log file since \t:\t%s' %(datetime.datetime.fromtimestamp(int(max(time_list))).strftime('%d %B %Y : %H %M'))




######## must be at the end, it where the time file gets updated

if test != 'test':
	#ref_last_time = 1475737799
	ref_time_file = '%s/ref_time.txt' %(base_path)
	ref_last_time = os.path.getmtime(ref_time_file)
	copy_Ref(path,ref_path,ref_last_time)

	append_file = open(ref_time_file,'a')
	append_file.write('%s\n\n' %(now_date))
	append_file.close()
	#raw_input('copy ref')

if test != 'test' and test != 'check':
	append_file = open(time_file,'a')
	append_file.write('%s\n\n' %(now_date))
	append_file.close()
	print '\nupdated %s\n' %(time_file)
	last_sample_log = os.path.getmtime(sample_log_time_file)
	last_time = os.path.getmtime(time_file)

###############rsync#######################
rsync = False
if rsync == True:
	cmd = 'rsync -aP /blackburn3/RAW_Data/Q_Exactive_2014/ /blackburn3/RAW_BACKUP'
	print(cmd)
	if test != 'test':
		os.system(cmd)
	cmd = 'rsync -aP --exclude ".git" /blackburn3/scripts /mnt/BLACKBURNLAB/Proteomic_Documents/scripts/'
	print(cmd)
	if test != 'test':
		os.system(cmd)

print 'current time\t:\t%s\t:\t%s' %(last_time,datetime.datetime.fromtimestamp(int(last_time)).strftime('%d %B %Y : %H %M'))
print 'last sample log\t:\t%s\t:\t%s' %(last_sample_log,datetime.datetime.fromtimestamp(int(last_sample_log)).strftime('%d %B %Y : %H %M'))




print 'complete'
os.system('exit')




