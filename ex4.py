#Defining the amount of cars
cars = 100
#Defining the space in a car
space_in_a_car = 4.0
#Defining the amount of drivers
drivers = 30
#Defining the number of passengers
passengers = 90
#Calculating how many cars are not driven
cars_not_driven = cars - drivers
#Calculating how many cars are indeed driven
cars_driven = drivers
#Calculating the carpool capacity
carpool_capacity = cars_driven * space_in_a_car
#Calculating the average passengers in a car
average_passengers_per_car = passengers / cars_driven

#Now to output everything

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


#I still don't understand when to have a 4.0 vs a 4, for the space_in_a_car variable. The output's looked the same, unless I missed something
