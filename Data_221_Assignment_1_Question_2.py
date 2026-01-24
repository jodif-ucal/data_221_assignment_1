def lay_out_string_structure(list_of_strings):
    dictionary_of_string_structure = {}

    for each_string in list_of_strings:
        dictionary_of_string_structure[each_string] = {
            "length": len(each_string),
            "parity": "even" if len(each_string) & 2 == 0 else "odd"
        }

    return dictionary_of_string_structure

sample_list_of_strings = ["data", "science", "computer", "course"]

print(lay_out_string_structure(sample_list_of_strings))