def cities():
    list1 = ["NIECE", "BERLIN", "LONDON", "PARIS", "AMSTERDAM", "ROME", "OSLO", "STOCKHOLM", "HAMBURG",
             "MADRID", "BOLOGNA"]
    return list1


def get_info():
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    email = input('Enter email: ')
    phone = input('Enter phone: ')
    location = input('Enter your current location')
    requires = input('Enter requires:(Smoking-No,Pet-Yes,Luggage-No)')
    passengers = input('How many passengers?')
    print('name: ', name
          , ' \nsurname: ', surname
          , '\nFrom: ', location
          , '\nwith these requires: ', requires
          , '\nwith ', passengers, 'passengers')


def services():
    print('1:Find ride\n'
          '2:Offer ride\n'
          '3:How it works\n'
          'Q:Quit')







# BlaBlaCar is a French online marketplace for carpooling.
#   Its website and mobile apps connect drivers and passengers willing to travel together
#       between cities and share the cost of the journey
#                 The platform had 70 million users in 2019 and is available in 22 countries.
#     \nAlmost all of which are in Europe and Latin America – countries include:\n Belgium, Brazil, Croatia,
#     Czech Republic, France, Germany, Hungary, India, Italy, Luxembourg, Mexico, \nThe Netherlands,
#     Poland, Portugal, Romania, Russia, Serbia, Slovakia, Spain, Turkey, Ukraine, and the United Kingdom
