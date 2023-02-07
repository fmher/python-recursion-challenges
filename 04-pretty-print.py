'''
Write a function called pretty_print that accepts a complex dictionary and prints out all of it's keys and all of its values. 
The dictionary can have dictionaries nested inside of it.

HOW TO:

Make the function accept two parameters: pretty_print(dictionary, indent).
* dictionary is the dictionary that's currently being iterated over.
* indent is a string representing the current level of indentation.

Whenever you make a recursive call increase the level of indentation by adding two spaces to indent:

It's useful to know how to detect if an object is an instance of a specific class in Python. 
Use the isinstance method to see if a value is an instance of a certain class.

Examples:

dicts:
o1 = {"a": 1, "b": 2}
o2 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero"}, "d": 4}

pretty_print(o1, "")
a: 1
b: 2

pretty_print(o2, "")
a: 1
b: 2
c:
  name: Bruce Wayne
  occupation: Hero
d: 4
'''

# use these for testing
o1 = {"a": 1, "b": 2}
o2 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero"}, "d": 4}
o3 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero", "friends": {"spiderman": {"name": "Peter Parker"}, "superman": {"name": "Clark Kent"}}}, "d": 4}


# Write a function called pretty_print that accepts a complex dictionary and prints out all of it's keys and all of its values.
# The dictionary can have dictionaries nested inside of it.
def pretty_print(dictionary, indent):
    # base case
    if isinstance(dictionary, dict):
        for key in dictionary:
            if isinstance(dictionary[key], dict):
                print(indent + key + ":")
                pretty_print(dictionary[key], indent + "  ")
            else:
                print(indent + key + ": " + str(dictionary[key]))
    # recursive case
    else:
        print(indent + dictionary)
# test
pretty_print(o3, "")