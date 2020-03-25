


def show_info(data_csv, first_name, second_name):
    first_name = (first_name.replace(" ", "")).capitalize()
    second_name = (second_name.replace(" ", "")).capitalize()
    full_name = first_name + " " + second_name
    data_list = []
    if second_name == "":
        dict_of_found_data = dict(
            filter(lambda item: first_name in (item[0].split())[0], data_csv.items()))
        for keys, values_list in dict_of_found_data.items():
            for value_pair_list in values_list:
                print(keys + " - " +
                      value_pair_list[0]+' - ' + value_pair_list[1])
                data_list.append(
                    keys + " - " + value_pair_list[0]+' - ' + value_pair_list[1])
    elif first_name == "":
        dict_of_found_data = dict(
            filter(lambda item: second_name in (item[0].split())[1], data_csv.items()))
        for keys, values_list in dict_of_found_data.items():
            for value_pair_list in values_list:
                print(keys + " - " +
                      value_pair_list[0]+' - ' + value_pair_list[1])
                
                data_list.append(
                    keys + " - " + value_pair_list[0]+' - ' + value_pair_list[1])
    else:
        dict_of_found_data = dict(
            filter(lambda item: full_name in item[0], data_csv.items()))
        for keys, values_list in dict_of_found_data.items():
            for value_pair_list in values_list:
                print(keys + " - " +
                      value_pair_list[0]+' - ' + value_pair_list[1])
                data_list.append(
                    keys + " - " + value_pair_list[0]+' - ' + value_pair_list[1])
    return data_list