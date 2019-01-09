# Create an empty set:
showroom = set()

# Add four cars to the showroom:
showroom.add('tacoma')
showroom.add('tundra')
showroom.add('four-runner')
showroom.add('rav-4')

# Print the length of the set:
print('Number of cars in the showroom: ', len(showroom))

# Try to add to the set and print out the list of cars:
showroom.add('tacoma')
print('Cars in the showroom: ', showroom)

# Add another set to the showroom using update:
new_cars = set({'camry', 'corolla'})
showroom.update(new_cars)
print('New showroom of cars: ', showroom)

# Use discard to remove the car you sold:
showroom.discard('corolla')
print('The cars that remain: ', showroom)

# add cars to a set called junkyard.  Some will be new and others will be from the showroom:

junkyard = set({'mustang', 'F-150', 'ranger', 'tundra', 'tacoma'})

# use intersection to display common models in both sets:
buyer_yard = showroom.intersection(junkyard)
print('Cars from that exist in both showroom and junkyard: ', buyer_yard)

# Use union to combine the 2 yards:
combined_yards = showroom.union(junkyard)
print('This is the combined inventory: ', combined_yards)

# Use discard to print the cars that you want to display in your showroom:
combined_yards.discard('mustang')
combined_yards.discard('camry')
combined_yards.discard('rav-4')

print('These are the cars on display in the final showroom: ', combined_yards)