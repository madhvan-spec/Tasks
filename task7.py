# Implement a function to merge two dictionaries
def merge_list(dict1,dict2):
    for k,v in dict2.items():
        dict1[k] = v
    print(dict1)

dict1 = {"Apple":1,"Banana":2,"Cherry": 3}
dict2 = {"Apple":3,"Orange":4,"Mango":5}
merge_list(dict1,dict2)