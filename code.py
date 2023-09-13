
# These lines import the necessary libraries to run this code
import time
import board
import digitalio
import pwmio

from adafruit_motor import motor # Imports a function from the adafruit_motor library

left_motor_foward = board.GP12 # initializes the variable left_motor_foward and attatches it to GP12
left_motor_backward = board.GP13 # initializes the variable left_motor_backward and attatches it to GP13
right_motor_foward = board.GP14
right_motor_backward = board.GP15

pwm_La = pwmio.PWMOut(left_motor_foward, frequency=10000) # Tells the controller that the motor is an output
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)
pwm_Lc = pwmio.PWMOut(right_motor_foward, frequency=10000)
pwm_Ld = pwmio.PWMOut(right_motor_backward, frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) # Configuration line (it is required)
Left_Motor_speed = 0 #Initiates the variable for the left_motot_speed and starts it at 0
Right_Motor = motor.DCMotor(pwm_Lc, pwm_Ld)
Right_Motor_speed = 0



while True:
    Left_Motor_speed = .5 # Makes left motor roll foward
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(.2)
    Left_Motor_speed = .5
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(.2)
    Right_Motor_speed =   .5 # Makes left motor roll foward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(.2)
    Right_Motor_speed = .5
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(.2)
