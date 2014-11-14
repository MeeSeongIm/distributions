import numpy as np
 

n = 1000

values = ("a", "b", "c", "d")  # list of possible values 
weights = (0.1, 0.2, 0.5, 0.2)  # weights of the values 

string = "".join(np.random.choice(values, size=n, replace = True, p = weights))

print("string: %s" % string)
  
number_a = 0
number_b = 0
number_c = 0
number_d = 0

string_list = []

for i in range(len(string)):
    string_list.append(string[i])

for i in range(len(string)):
    if string[i] == "a":
        number_a += 1
        
    if string[i] == "b":
        number_b += 1

    if string[i] == "c":
        number_c += 1

    if string[i] == "d":
        number_d += 1

print("number of a appearing in the string: %d" % number_a)
print("number of b appearing in the string: %d" % number_b)
print("number of c appearing in the string: %d" % number_c)
print("number of d appearing in the string: %d" % number_d)


avg_num_a = float(number_a/n)
avg_num_b = float(number_b/n)
avg_num_c = float(number_c/n)
avg_num_d = float(number_d/n)

print(weights)
print(avg_num_a)    # proportional number of a appearing in the string
print(avg_num_b)    # proportional number of b appearing in the string
print(avg_num_c)    # proportional number of c appearing in the string
print(avg_num_d)    # proportional number of d appearing in the string


