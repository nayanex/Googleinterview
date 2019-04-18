import sys
import datetime

def query_timestamp(timestamp_list, query):
    for item in timestamp_list:
        if item[1] == query:
            return item
    return -1

def get_value(key_query, timestamp, dictionary):
    match_value = ""
    for key, value in dictionary.items():
        if key == key_query:
            match_value = query_timestamp(dictionary[key], timestamp)
        else:
            return "Key not found"
    return match_value[0]

def put_value(key_query, timestamp, dictionary, value_input):
    for key, value in dictionary.items():
        if key == key_query:
            timestamp = datetime.datetime.strptime(timestamp, '%d%b%Y')
            dictionary[key].append((value_input, timestamp))
        else:
            dictionary[key] = (value, timestamp)
    return dictionary

dictionary = {}

# Adding some initial values to the dictionary
dictionary["a"] = [(1, datetime.datetime.strptime('16Sep2012', '%d%b%Y'))]

# Getting values for the put interface
print("Please type a key and a value and timestamp")
input = sys.stdin.read()
a, b, timestamp = input.split()
dictionary = put_value(a, timestamp, dictionary, b)

# Querying values for the get interface
print("Please type the key and timestamp you want to query")
input = sys.stdin.read()
key_query, timestamp = input.split()
timestamp = datetime.datetime.strptime(timestamp, '%d%b%Y')
print(get_value(key_query, timestamp, dictionary))

