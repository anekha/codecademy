#function example
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print("With tax: %f" % bill)
  return bill


def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print("With tip: %f" % bill)
  return bill


meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

#call and response functions
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print("%d squared is %d." % (n, squared))
  return squared

#power function
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)  # Add your arguments here!

#functions calling functions
def one_good_turn(n):
  return n + 1

def deserves_another(n):
  return n + 2

#Built-in functions
def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"

#Calculating the trip cost
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print(trip_cost("Los Angeles", 5, 600))
