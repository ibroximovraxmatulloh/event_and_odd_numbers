#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable

number = 1235
x1 = number//1000
x2 = number%1000//100
x3 = number%1000%100//10
x4 = number%1000%100%10

print((x1+1)%2+(x2+1)%2+(x3+1)%2+(x4+1)%2)


