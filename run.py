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

    user_email = input('\nEnter your email: ')
    validate_data(0,user_email)

    user_age = input('\nEnter your age: ')
    print(user_age)

    user_gender = input('\nEnter your gender (M or F): ')
    validate_data(1,user_gender)

    user_country = input('\nEnter your country: ')
    user_city = input('\nEnter your city: ')

    user_rent = input('\nDo you pay rent? (Y or N):  ')
    validate_data(2,user_rent)

    user_children = input('\nHow many children do you have? (0 for None):  ')

def validate_data(value1,value2):
    try:
        if ((value1 == 0) and ('@' not in value2)):
            raise ValueError('@ required') 
        if ((value1 == 1) and (value2 not in ['M','m','F','f'])):
            raise ValueError('M or F required')    
        if ((value1 == 2) and (value2 not in ['Y','y','N','n'])):
            raise ValueError('Y or N required')      
    except ValueError as e:   
        print(f'Invalid data: {e}, please try again.\n') 

get_users_data()    
