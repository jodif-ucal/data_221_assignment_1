def distribution_analysis(list_of_numbers: list):
    list_of_numbers_in_list = [] #This list is in order to sort the eventual keys of the dictionary
    distribution_analysis_dictionary = {}

    for number in list_of_numbers:
        if number not in list_of_numbers_in_list:
            list_of_numbers_in_list.append(number)

    list_of_numbers_in_list.sort()

    for current_number in list_of_numbers_in_list:
        number_of_numbers_less_than_or_equal_to_current_number = 0

        #Counting how many numbers are less than or equal to the current number being checked
        for number in list_of_numbers:
            if current_number >= number:
                number_of_numbers_less_than_or_equal_to_current_number += 1

        #Adding the results to the dictionary
        distribution_analysis_dictionary[current_number] = number_of_numbers_less_than_or_equal_to_current_number/len(list_of_numbers) * 100

    return distribution_analysis_dictionary

#To test
sample_list_of_numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis(sample_list_of_numbers))