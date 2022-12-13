weight = 4.8
cost = 0.00
premium_ground = 125.00
#Ground shipping

if weight <= 2:
  cost = weight * 1.25 + 20
elif weight > 2 and weight <= 6:
  cost = weight * 3 + 20
  
elif weight > 6 and weight <= 10:
  cost = weight * 4 + 20
  
elif weight > 10:
  cost = weight * 4.75 + 20
  
print("Ground shipping cost is : $", cost,)
print("Premium Ground Shipping cost is : $", premium_ground)

#Drone Shipping

if weight <= 2:
  cost = weight * 4.50
  
elif weight > 2 and weight <= 6:
  cost = weight * 9.00
 
elif weight > 6 and weight <= 10:
  cost = weight * 12.00
 
elif weight > 10:
  cost = weight * 14.25
 

print("The cost to ship by Drone is :$", cost)

