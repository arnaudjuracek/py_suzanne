# ----------------------------
# updater for py_suzanne
# Arnaud Juracek
# running at startup, before run.py

import glob, time, os

usb = '/home/pi/Suzanne/usb/'
if not os.listdir(usb):
	print 'updater.py: usb not mounted, trying to mounting...'
	for drive in glob.glob('/dev/sd*'):
		os.system('sudo mount '+ drive + ' ' + usb + ' -o uid=pi,gid=pi')
	
if len(os.listdir(usb))>0:
	print 'updater.py: checking update...'
	if os.path.isfile(usb + 'run.py'):
		os.system('omxplayer data/update.aiff')
		print 'updater.py: update found'
		print 'updater.py: backing up...'
		os.system('mv /home/pi/Suzanne/run.py /home/pi/Suzanne/bak.run.py')
		print 'updater.py: updating...'
		os.system('mv ' + usb + 'run.py /home/pi/Suzanne/')
		print 'updater.py: successfully updated !'
	else:
		print 'updater.py: no new update.'
