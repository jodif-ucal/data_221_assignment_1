def distribution_analysis(list_of_numbers: list):
    list_of_numbers_in_list = []
    distribution_analysis_dictionary = {}

    for number in list_of_numbers:
        if number not in list_of_numbers_in_list:
            list_of_numbers_in_list.append(number)

    list_of_numbers_in_list.sort()

    for current_number in list_of_numbers_in_list:
        number_of_numbers_less_than_or_equal_to_current_number = 0

        for number in list_of_numbers:
            if current_number >= number:
                number_of_numbers_less_than_or_equal_to_current_number += 1

        distribution_analysis_dictionary[current_number] = number_of_numbers_less_than_or_equal_to_current_number/len(list_of_numbers) * 100

    return distribution_analysis_dictionary

sample_list_of_numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis(sample_list_of_numbers))