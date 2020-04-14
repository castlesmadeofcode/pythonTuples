# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("lion", "tiger", "bear", "zebra", "flamingo", "penguin", "kangaroo", "giraffe", "dog", "cat")

# Find one of your animals using the tuple.index(value) syntax on the tuple.
zoo.index("flamingo") 
# print(zoo.index("flamingo"))


# Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = "kangaroo"
# if animal_to_find in zoo:
# Print that the animal was found
    # print(f"{animal_to_find} was found")


# Create a variable for the animals in your zoo tuple, and print them to the console.
(first_child, second_child, third_child, fourth_child, fifth_child, sixth_child, seventh_child, eighth_child, ninth_child, tenth_child) = zoo
# print(first_child) 
# print(second_child) 
# print(third_child) 
# print(fourth_child)
# print(fifth_child) 
# print(sixth_child) 
# print(seventh_child) 
# print(eighth_child) 
# print(ninth_child) 
# print(tenth_child) 


# Convert your tuple into a list.
zooList = list(zoo)
# print(zooList)


# Use extend() to add three more animals to your zoo.
zooList.extend(["Mary", "Joseph", "Bob"])
# print(zooList)


# Convert the list back into a tuple.
tuple(zooList)
# print(tuple(zooList))
