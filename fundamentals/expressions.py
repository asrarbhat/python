# for booleans
age = 22
is_adult = age > 18
has_penis = True
is_man = age > 18 and has_penis
is_nibba = True if age < 18 and has_penis else False
is_nibbi = True if age < 18 and not has_penis else False

boolean = True and True or False  # True
boolean_one = True+True  # True is 1 and False is 0
boolean_two = True == 1
boolean_three = False == 0
boolean_four = True+True == 2

# mod operations
modulus = 12 % 7 == 5
floor_division = 12//7


# for integers and floats using equations of linear motion
initial_velocity = 30
acceleration = 9.81
time = 2.3
initial_position = 4
final_velocity = initial_velocity + acceleration * time
final_position = initial_position+initial_velocity*time+1/2*acceleration*time*time
distance = (final_velocity*final_velocity-initial_velocity *
            initial_velocity)/(2*acceleration)

# for the complex
compex_one = 2+3j + 7+8j
complex_two = 2+3j/5+5j
