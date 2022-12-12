# Receipts for Lovely Loveseats
# We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.

# In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

# Please note: Projects do not run tests against your code. This experience is more open to your interpretation and gives you the freedom to explore. Remember that all variables must be declared before they are referenced in your code.


#Let’s add in our first item, the Lovely Loveseat that is the store’s namesake. Create a variable called lovely_loveseat_description and assign to it the following string:

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

# Great, now let’s create a price for the loveseat. Create a variable lovely_loveseat_price and set it equal to 254.00.
lovely_loveseat_price = 254.000

# Let’s extend our inventory with another characteristic piece of furniture! Create a variable called stylish_settee_description and assign to it the following string:


stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

# Now let’s set the price for our Stylish Settee. Create a variable stylish_settee_price and assign it the value of 180.50.

stylish_settee_price = 180.50

#Fantastic, we just need one more item before we’re ready for business. Create a new variable called luxurious_lamp_description and assign it the following:
#Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. And set the price to 52.15
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15 


# Add the sales tax
sales_tax = 0.088

#initialize the total and itemization

customer_one_total = 0
customer_one_itemization = ""

# They bought a love seat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description 

#They bought a lamp
customer_one_total += luxurious_lamp_price 
customer_one_itemization += luxurious_lamp_description

#Calculate the sales tax
customer_one_tax = customer_one_total * sales_tax

#Add it to the total
customer_one_total = customer_one_total + sales_tax

#Now we print the receipt
print("Customer One Items: ")

print(customer_one_itemization)

print("Customer One Total: ")

print(customer_one_itemization)

print("Customer One Total: ")

print(customer_one_total)
