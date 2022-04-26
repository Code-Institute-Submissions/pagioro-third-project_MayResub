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

    while True:
        user_name = input('Enter your name: ')        
        if validate_data(0,user_name):            
            break         

    while True:
        user_email = input('\nEnter your email: ')
        if validate_data(1,user_email):            
            break    
    
    while True:
        user_age = input('\nEnter your age: ')
        if validate_data(2,user_age):            
            break    
    
    while True:
        user_gender = input('\nEnter your gender (M or F): ')
        if validate_data(3,user_gender):            
            break    
    
    user_country = input('\nEnter your country: ')    

    user_city = input('\nEnter your city: ')
    

    while True:
        user_rent = input('\nDo you pay rent? (Y or N):  ')
        if validate_data(4,user_rent):            
            break    
    
    while True:
        user_children = input('\nHow many children do you have? (0 for None):  ')
        if validate_data(5,user_children):            
            break

    return user_name, user_email, user_age, user_gender, user_country, user_city, user_rent, user_children
    
    
def validate_data(value1,value2):
    try:
        """
        In the first if checks if the value2 has at least one number.
        """        
        if ((value1 == 0) and (any(chr.isdigit() for chr in value2))):
            raise ValueError()        
        if ((value1 == 1) and ('@' not in value2)):
            raise ValueError() 
        if ((value1 == 2) and (int(value2) > 110)):
            raise ValueError() 
        if ((value1 == 3) and (value2 not in ['M','m','F','f'])):
            raise ValueError()    
        if ((value1 == 4) and (value2 not in ['Y','y','N','n'])):
            raise ValueError()  
        if ((value1 == 5) and (int(value2) >= 12)):
            raise ValueError()     
    except ValueError as e:   
        print(f'Invalid data.\n')
        return False

    return True 

def update_census_worksheet(data):
    """
    Update Census worksheet with data
    """
    print('Updating Census worksheet...\n')
    census_worksheet = SHEET.worksheet("census")
    census_worksheet.append_row(data)
    print('Census worksheet updated successfully.\n')

def update_female_data(census_row):
    """
    Insert the female information into the female worksheet.
    """
    print('Saving female data.../n')
    """
    if (SHEET.worksheet('census').col_values(4) in ('F','f')):       
        val = SHEET.worksheet('census').row_values()
        print(val)
    """


def main():
    data = get_users_data() 
    update_census_worksheet(data)
    update_female_data(data)

main()
