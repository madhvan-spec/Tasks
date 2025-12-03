# Write a program to find duplicates in a list
def find_duplicates(l):
    duplicate_items_list=[]
    for i in l:
        if(l.count(i)>1):
            if i not in duplicate_items_list:
                duplicate_items_list.append(i)
            else:
                pass

    print(f"Duplicate Items are {duplicate_items_list}")

l=['apple','banana',2,'orange',2,'apple','kiwi','kiwi']
find_duplicates(l)