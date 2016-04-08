# ---------------------------
# py_suzanne 1.4
# Arnaud Juracek
# github.com/arnaudjuracek

import RPi.GPIO as GPIO
import glob, pygame, time, os, random

# --------------------------
# startup notification
print 'py_suzanne started'
os.system('omxplayer data/hello_world.aiff')

# --------------------------
# GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# --------------------------
# USB handling/mounting
usb = '/home/pi/Suzanne/usb/'
files = []
def getfile():
	if not os.listdir(usb):
		print 'getfile(): usb not mounted, mounting...'
		for drive in glob.glob('/dev/sd*'):
			os.system('sudo mount '+ drive + ' ' + usb +' -o uid=pi,gid=pi')

	files = soundfiles(usb)
	if len(files)>0:
		file = random.choice(files)
		print 'getfile(): '+ file +' selected'
		return file
	else:
		print "getfile():error: couldn't get file : usb directory empty or not mounted correctly"
		return 'data/error.mp3'

# -------------------------
# sound files filter
# see http://stackoverflow.com/a/4568638
def soundfiles(path):
	ext = (path + '*.mp3', path + '*.wav')
	sounds = []
	for files in ext:
		sounds.extend(glob.glob(files))
	return sounds

# -------------------------
# instantiate pygame.mixer, player, etc
# see http://www.pygame.org/docs/ref/music.html#module-pygame.mixer.music
mixer = pygame.mixer
player = mixer.music
mixer.init(frequency=48000, size=-16, channels=1, buffer=1024)

# -------------------------
# lid open/close listenning
# see http://razzpisampler.oreilly.com/ch07.html
while not os.path.isfile(usb + 'debug'): 
	time.sleep(.5)
	# GPIO.input(18) == False when 18 linked to GND
	# GPIO.input(18) == True when 18 not linked to GND
	if GPIO.input(18) == True:
		if player.get_busy() == False:
			player.load(getfile())
			player.play()
	else:
		player.fadeout(1000)
