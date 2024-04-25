import OPi.GPIO as GPIO
import os
import time

test = 12 #红外模块接口号码
power_out = 18 #连接屏幕的电源接口号码，检测是否亮屏
power_in = 22 #连接屏幕驱动板的电源接口号码，控制屏幕开关
GPIO.setmode(GPIO.BOARD)
GPIO.setup(test, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(power_out, GPIO.IN) 
GPIO.setup(power_in, GPIO.OUT) 

#红外模块未检测到人时，屏幕熄灭，检测到人时，屏幕亮起
while(1):
	if( GPIO.input(power_out)):
		print("light")
		if(GPIO.input(test)):
			print("not detected")
			GPIO.output(power_in, GPIO.LOW)
			time.sleep(2)
			GPIO.output(power_in, GPIO.HIGH)
			time.sleep(2)
		else:
			print("detected")
		
	else:
		print("shutdown")
		if(not GPIO.input(test)):
			print("detected")
			GPIO.output(power_in, GPIO.LOW)
			time.sleep(2)
			GPIO.output(power_in, GPIO.HIGH)
			time.sleep(2)
			time.sleep(300)
		else:
			print("not detected")
	print("\n")

GPIO.cleanup()		
