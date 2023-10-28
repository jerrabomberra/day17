import json
data=[]

# Opening JSON file
with open('data.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    # print("Type:", type(data))

    print(data)

