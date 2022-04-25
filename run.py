import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CENSUS = Credentials.from_service_account_file('census.json')
SCOPED_CENSUS = CENSUS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CENSUS)
SHEET = GSPREAD_CLIENT.open('census')

"""
census_sheet = SHEET.worksheet('census')
data = census_sheet.get_all_values()
print(data)
"""

def get_users_data():
    """
    Get data from the user.
    """
    print('Welcome to the 2022 Census.') 
    print('Please fill in the requested data!\n')  

    user_name = input('Enter your name: ')
    print(user_name)
    user_email = input('\nEnter your email: ')
    print(user_email)
    user_age = input('\nEnter your age: ')
    print(user_age)
    user_gender = input('\nEnter your gender (M or F): ')
    print(user_gender)

    user_country = input('\nEnter your country: ')
    print(user_country)
    user_city = input('\nEnter your city: ')
    print(user_city)

    user_rent = input('\nDo you pay rent? (Y or N):  ')
    validate_data(user_rent)

    user_children = input('\nHow many children do you have? (0 for None):  ')
    print(user_children)

def validate_data(values):
    try:
        if (values not in ['Y','y','N','n']):
            raise ValueError('deu erro')    
    except ValueError as e:   
        print(f'{e}, tente novamente') 


get_users_data()    
