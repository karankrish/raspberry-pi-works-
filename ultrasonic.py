import RPi.GPIO as GPIO
import subprocess
import time
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(16,GPIO.OUT)
GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)
while(True):
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()
	
	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration*17150
	distance = round(distance, 2)
	print "Distance:",distance,"cm"
	
	if(distance<50):
		subprocess.Popen('sudo python pccoesms.py',shell=True)
		time.sleep(1)
		subprocess.Popen('sudo espeak -f speech.txt',shell=True)
		time.sleep(1)
		subprocess.Popen('sudo fswebcam image.jpg',shell=True)
		time.sleep(10)
		subprocess.Popen('sudo python mail.py',shell=True)
		time.sleep(1)

GPIO.cleanup()

