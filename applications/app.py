import functions

operator_a = {
    1: 0.9,
    268: 5.1,
    46: 0.17,
    4620: 0.0,
    468: 0.15,
    4631: 0.15,
    4673: 0.9,
    46732: 1.1
}
operator_b = {
    1: 0.92,
    44: 0.5,
    46: 0.2,
    467: 1.0,
    48: 1.2
}
operators = [operator_a, operator_b]
operator_names = ['Operator A', 'Operator B']

functions.find_cheapest(functions.get_contact_input(), operators, operator_names)
