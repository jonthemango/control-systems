# constants 
group_number = 20
mass_of_the_load = 100 + group_number
mass_of_the_cart = 20
length = 12
gravity = 10 

# inputs 
force = 99
kp = 1 # INCREASING kp => DECREASE rise_time, INCREASE overshoot, SMALL CHANGES in settling_time, DECREASE steady_state_error
ki = 1 # INCREASING ki => DECREASE in rise_time, INCREASE overshoot, INCREASE in settling_time, DECREASE steady_state_error
kd = 1 # INCREASING kd => SMALL CHANGES in rise_time, DECREASE overshoot, DECREASE in settling_time, NO CHANGE in steady_state_error

a = -((mass_of_the_load+mass_of_the_cart)*gravity)/(mass_of_the_cart*length)
b = (mass_of_the_cart*length)
c = (mass_of_the_load*gravity)/mass_of_the_cart
d = mass_of_the_cart