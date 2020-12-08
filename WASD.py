from gpiozero import LED
from keyboard import is_pressed

green = LED(6)
red = LED(13)
blue = LED(19)
yellow = LED(26)

while True:
	if is_pressed('w'):
		green.on()
	if is_pressed('a'):
		blue.on()
	if is_pressed('s'):
		red.on()
	if is_pressed('d'):
		yellow.on()

	green.off()
	blue.off()
	red.off()
	yellow.off()
