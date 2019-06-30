def get_contact_input():
    contact_number = input('Please enter your number: ').replace(' ', '')
    if contact_number.isnumeric():
        return contact_number
    elif contact_number == '':
        return -1
    else:
        return -2


def get_operator_name(index, service_operator_names):
    if not isinstance(index, int):
        raise TypeError('The list index must be an integer value!')
    else:
        return service_operator_names[index]


def find_cheapest(contact_number, service_operators, service_operator_names):
    if contact_number == -1:
        print('Please enter your contact number!')
    elif contact_number == -2:
        print('Please enter only numbers!')
    else:
        cheapest_cost = 0
        count_to_get_name = 0
        operator_name_index = 0
        for operator in service_operators:
            no = contact_number
            while len(no) != 0:
                for code_int in operator:
                    code = str(code_int)
                    if code == no:
                        if isinstance(cheapest_cost, int):  # entered area code matches for the 1st time with a operator
                            cheapest_cost = operator[int(code)]
                            operator_name_index = count_to_get_name
                        elif operator[int(code)] < cheapest_cost:
                            cheapest_cost = operator[int(code)]
                            operator_name_index = count_to_get_name
                        no = ''
                        break
                no = no[0:-1]
            count_to_get_name += 1
        if isinstance(cheapest_cost, int):
            print('There is no operator who provide services to the area code you dialed')
        else:
            operator_name = get_operator_name(operator_name_index, service_operator_names)
            print(f'The lowest cost for your call would be $ {cheapest_cost}/min from "{operator_name}"')