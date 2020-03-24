#create definition to use in get_dressed()
def get_position(str,a):
    perm_list=str.split(" ")
    return perm_list.index(a)

#create definition to use in get_dressed()..converts numbers to words
def process_current_perm(position, item, processed_perm):
    processed_perm[position]=str(item)
    return processed_perm

#create dictionary to use in get_dressed()
items_dict = {"1":"hat", "2":"pants", "3":"shirt", "4":"shoes", "5":"socks", "6":"leave"}



def get_dressed(perm):
    #create a list of 0's to replace for the current permutation
    processed_perm=[]
    for i in range(0,len(perm.split(" "))):
        processed_perm.append("0")

    #convert numbers to words
    for key in items_dict:
        try:
            processed_perm=process_current_perm(get_position(perm,key), items_dict[key], processed_perm)
        except:
            pass

    # hat is optional but all others required
    all_terms_present=True
    for item in ["pants", "shirt", "shoes", "socks"]:
        if all_terms_present and item not in processed_perm:
            processed_perm.pop()
            processed_perm.append("fail")
            all_terms_present=False

    # you must put your socks on before your shoes
    if all_terms_present and processed_perm.index("socks") < processed_perm.index("shoes"):
        loc_rule1=10
    else:
        try:
            loc_rule1=processed_perm.index("shoes")
        except:
            pass

    # you must put on your pants before your shoes
    if all_terms_present and processed_perm.index("pants") < processed_perm.index("shoes"):
        loc_rule2=10
    else:
        try:
            loc_rule2 = processed_perm.index("shoes")
        except:
            pass

    # if hat, must put on shirt before hat
    if 'hat' in processed_perm:
        if all_terms_present and processed_perm.index("shirt") < processed_perm.index("hat"):
            loc_rule3=10
        else:
            try:
                loc_rule3 = processed_perm.index("hat")
            except:
                pass
    else:
        loc_rule3=10

    if all_terms_present and min(loc_rule1,loc_rule2,loc_rule3) != 10:
        earliest_rule_violation= min(loc_rule1,loc_rule2,loc_rule3)
        processed_perm=processed_perm[:earliest_rule_violation]
        processed_perm.append("fail")
        return processed_perm
    else:
        return processed_perm






