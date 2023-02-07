sentence = "What is the Airspeed Velocity of an Unladen Swallow"

# Remember it is {new_key:new_value for item in list}
result = {word: len(word) for word in sentence.split()}

print(result)
