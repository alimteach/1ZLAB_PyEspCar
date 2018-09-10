'''
电机测试
-----------------
左右轮设定特定的转速
'''
from car_config import gpio_dict, car_property
from motor import Motor
import time

# 左侧电机
lmotor = Motor(gpio_dict['LEFT_MOTOR_A'], gpio_dict['LEFT_MOTOR_B'], 
        motor_install_dir=car_property['LEFT_MOTOR_INSTALL_DIR'])
lmotor.pwm(300)

# 右侧电机
rmotor = Motor(gpio_dict['RIGHT_MOTOR_A'], gpio_dict['RIGHT_MOTOR_B'], 
        motor_install_dir=car_property['RIGHT_MOTOR_INSTALL_DIR'])
rmotor.pwm(300)

try:
    while True:
        pass
except:
    lmotor.deinit()
    rmotor.deinit()