print(''' 
=======================================
         ☆*WANDERWISE✈️*☆
========================================

''')
def choose_valid_number(question, dictionary):
    while True:
        answer = input(question)

        if answer in dictionary:
            return(answer)
        else:
            print('Please enter a valid number...')


country_dict = {
    '1' : 'SOUTH KOREA',
    '2' : 'JAPAN'
}

country = '''Type the number of the country you want to travel- 
    1. 🇰🇷 SOUTH KOREA
    2. 🇯🇵 JAPAN
    >'''

country = choose_valid_number(country, country_dict)

duration_dict = {
'1' : 'MINI ESCAPE - 7 days',
'2' : 'CLASSIC GETAWAY - 14 days',
'3' : 'DREAM VACAY - 15+ days'
}

duration = '''Type the number of the duration u wish to choose for your stay-
    🩵1 for MINI ESCAPE - 7 days
    🩵2 for CLASSIC GETAWAY - 14 days
    🩵3 for DREAM VACAY - 15+ days
    >'''

duration = choose_valid_number(duration,duration_dict)

budget_dict = {
'1' : 'under 75k' ,
'2' : '75k-1,75,000',
'3' : '1,75,000 - 5,00,000'
}

budget = '''Type the number of the budget range you wish to choose for your stay-
    💵1 for under 75k 
    💶2 for 75k-1,75,000
    💷3 for 1,75,000 - 5,00,000
    > '''

budget = choose_valid_number(budget,budget_dict)

print(f'''WANDERWISE SUMMARY🌠
{country_dict[country]} 
{duration_dict[duration]} 
{budget_dict[budget]}''')

def choose_valid_activity(question, dictionary):
    valid_number = False
    while valid_number == False:
        activities = input(question)
        valid_number = True
        activity = activities.split()
        for number in activity:
            if number in dictionary:
                pass
            else:
                valid_number = False
                print('⚠input invalid try again...')

        if valid_number == True:
            return activity



if country == '1':

    activities_sk = {
        '1' : 'Gyeongbokgung Palace🏯 ',
        '2' : 'N Seoul Tower🗼',
        '3' : 'Haeundae Beach🏖️ ',
        '4' : 'Lotte World🪄 '
    }
    prices_sk = {
        '1':1000,
        '2': 1200,
        '3' : 3000,
        '4' : 4500
    }
    style_sk = {
        '1': '🏯',
        '2': '🗼',
        '3': '🏖️ ',
        '4': '🪄'
    }
    activities1 = '''add a space bar after each number-
                1 : Gyeongbokgung Palace
                2 : N Seoul Tower
                3 : Haeundae Beach
                4 : Lotte World

                >'''
    activities = choose_valid_activity(activities1, activities_sk)

    total = 0
    cart = []
    emojis = ''
    for number in activities:
        cart.append(activities_sk[number])
        total += prices_sk[number]
        emojis += style_sk[number]

elif country == '2':
    activities_jp = {
        '1' : 'Shibuya Crossing',
        '2' : 'Senso-ji Temple',
        '3' : 'Harajuku' ,
        '4' : 'Fushimi inari shrine'
    }
    prices_jp = {
        '1' : 1000,
        '2' : 1800,
        '3' : 3000,
        '4' : 4500
    }
    style_jp = {
        '1' : '🚦',
        '2'  : '☸️',
        '3' : '🏘️',
        '4' : '⛩️'
    }
    activities2 = '''add a space bar after each number-
                1 : Shibuya Crossing
                2 : Senso-ji Temple
                3 : Harajuku
                4 : Fushimi inari shrine
                > '''
    activities = choose_valid_activity(activities2, activities_jp)


    total = 0
    cart = []
    emojis = ''
    for number in activities:
        cart.append(activities_jp[number])
        total += prices_jp[number]
        emojis += style_jp[number]


print(f'YOUR TRAVELING STYLE = {emojis} ')
print('''
===========================
      🌸YOUR CART🌸
============================
''')
for item in cart:
    print(item)
print(f'''
----------------------------
Total = ₹{total}
''')


while True:
    confirm = input('''Confirm your trip?
          1. yes
          2.no
          >''')
    if confirm == '1':
        print('Booking your dream trip...')
        break
    elif confirm == '2':
        print('Returning to menu...')
        break
    else:
        print('oops! Invalid input, try again..⚠️')
