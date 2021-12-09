import utility

passport_id = None
utility.services()
nationality = input('Please enter your nationality: ').lower()
while True:
    if nationality == 'native':
        pass
    elif nationality == 'foreign':
        passport_id = input('Please enter your passport id:')
    else:
        print('Invalid operation!')
        break
    operation = input('Enter operation: ')
    if operation == '1':
        where = input('Where do you want to go?').upper()

        if utility.cities().__contains__(where):
            print('There are available trips for ', where)

        else:
            print('There are no available trips for ', where)
            break
        utility.get_info()
        print('Passport id: ', passport_id)

    elif operation == '2':
        car_type = input('Enter your car type: ')
        passengers = input('How many passengers can you carry? ')
        where = input('Where do you go?')
        utility.get_info()
        print('Passport id:', passport_id)
        print('To ', where)
        break
    elif operation == '3':
        string = 'BlaBlaCar is a French online marketplace for carpooling.\n' \
                 'Its website and mobile apps connect drivers and passengers willing to travel together\n' \
                 'Between cities and share the cost of the journey The platform had 70 million users in 2019 and\n' \
                 ' is available in 22 countries.'
        print(string)
    elif operation == 'Q':
        break
