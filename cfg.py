import random as rd
rules = {
    "Dec":[["DT","ID","Init","List"]], 
      "Init":[["=","ID","Init"],["=","1"],["=","2"],["=","3"],["=","4"],["=","5"],["=","6"],["=","7"],["=","8"],["=","9"],["=","0"],[""]],
    "List":[[",","ID","Init","List"],[";"]],
    "DT":[['string'],['int']],
    "ID":[['a'],['b']]
}


def generate_items(items): 
    for item in items: 
        if isinstance(item, list):
            for subitem in generate_items(item):
                yield subitem 
                
        else:
            yield item       

def expansion(start): 
    for element in start:
        if element in rules:
            loc = start.index(element)
            start[loc] = rd.choice(rules[element])
        result = [item for item in generate_items(start)]


    for item in result:
        if not isinstance(item, list):
            if item in rules:
                result = expansion(result)
    
    return result

def to_string(result):
    return ' '.join(result)

flag = False
x = input("enter expression eg string a = 7 ; \n enter : ")

count = 0
while flag == False:
    if(count > 100000):
        break;
    result = ["Dec"]
    result = expansion(result)  
    final = to_string(result)
    if x == final: 
        flag = True 
    else:
        flag=False
        count+=1;
if(flag):
    print("valid => ",final)
else:
    print("invalid => ",final)
