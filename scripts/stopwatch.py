import time, os
seconds = 0
minutes = 0
hours = 0
days = 0

time.sleep(1)
while True:
	seconds += 60
	if seconds == 60:
		minutes += 1
		seconds = 0
	if minutes == 60:
		hours += 1
		minutes = 0
		seconds = 0
	if hours == 24:
		days += 1
		hours = 0
		minutes = 0
		seconds = 0
	os.system('clear')
	print days,"days",hours,'hours',minutes,'minutes',seconds,'seconds'
	#time.sleep(0.1)
