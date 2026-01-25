def lay_out_string_structure(list_of_strings):
    #Even though this function was written for lists, it will work for tuples and sets anyway
    #It won't work with anything else however
    if not isinstance(list_of_strings, (list, tuple, set)):
        print("Invalid input. Argument type must be of type list, tuple or set")
        return None
    else:
        #Each item inside the data structure passed in must be a string, though
        for item in list_of_strings:
            if not isinstance(item, str):
                return None

    dictionary_of_string_structure = {}

    for each_string in list_of_strings:
        #Saving data about each string ina dictionary as a value, having the string itself as the key
        dictionary_of_string_structure[each_string] = {
            "length": len(each_string),
            "parity": "even" if len(each_string) & 2 == 0 else "odd"
        }

    return dictionary_of_string_structure

sample_list_of_strings = ["data", "science", "computer", "course"]

print(lay_out_string_structure(sample_list_of_strings))