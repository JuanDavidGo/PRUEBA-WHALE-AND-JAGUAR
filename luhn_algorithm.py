from os import nice

def luhn_algorithm(card_number):

    # reverse the credit card number
    card_number = card_number[::-1]
    
    # convert to integer list
    card_number_list = [int(i) for i in card_number]
    
    # create a list with every second duplicate number
    duplicated_numbers_list = list()
    numbers = list(enumerate(card_number_list, start = 1))

    for i, number in numbers:
        
        if i % 2 == 0:
            duplicated_numbers_list.append(number * 2)
        else:
            duplicated_numbers_list.append(number)
    
    # if the number is more than 9, add the digits of the number
    final_numbers_list = list()
    for number in duplicated_numbers_list:
        
        if number < 9:
            final_numbers_list.append(number)
        else:
            sum = 0
            for digit in str(number):
                sum += int(digit)
            final_numbers_list.append(sum)
    
    # sum all numbers of the list 
    sum_numbers_list = 0
    for num in final_numbers_list:
        sum_numbers_list += num
    
    """ 
    To know the credit card network it is necessary to compare the first digits of the card, in this way:
    
        If the card starts with 4 it is VISA
        If it starts with 37 it is American Express
        If it starts with 5 it is MasterCard
        If it starts with 6 it is Discover 
    """
    
    credit_card_network = "INDEFINIDO"

    if card_number_list[::-1][0] == 4: credit_card_network = "VISA"
    if card_number_list[::-1][0] == 3 and (card_number_list[::-1][1] == 7 or card_number_list[::-1][1] == 4): credit_card_network = "American Express"
    if card_number_list[::-1][0] == 3 and card_number_list[::-1][1] == 5: credit_card_network = "JCB"
    if card_number_list[::-1][0] == 5: credit_card_network = "MasterCard"
    if card_number_list[::-1][0] == 6: credit_card_network = "Discover"

    # if the sum is divisible by 10 then the card number is valid, if not invalid

    if sum_numbers_list % 10 == 0:
        return 'El numero ' + card_number[::-1] + ' es VALIDO y pertenece a la franquicia :' + credit_card_network
    else:
        return 'El numero ' + card_number[::-1] + ' es INVALIDO'