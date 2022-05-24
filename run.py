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

def get_users_data():
    """
    Get data from the user.
    """
    print('Welcome to the 2022 Census.')
    print('Please fill in the requested data!\n')    
    print('To access the results, use the link below:')
    print('https://docs.google.com/spreadsheets/d/1h8qsWk0Q3EEqi7zpqlX5rRxLMbBciOyYTID0DMKAOfU/edit?usp=sharing\n')

    while True:
        user_name = input('Enter your name:\n')
        if validate_data(0, user_name):
            break

    while True:
        user_email = input('Enter your email:\n')
        if validate_data(1, user_email):
            break

    while True:
        user_age = input('Enter your age:\n')
        if validate_data(2, user_age):
            break

    while True:
        user_gender = input('Enter your gender (M or F):\n')
        user_gender = user_gender.upper()
        if validate_data(3, user_gender):
            break
   
    while True:
        user_country = input('Enter your country:\n')
        user_country = user_country.upper()
        if validate_data(4, user_country):
            break

    while True:
        user_city = input('Enter your city:\n')
        if validate_data(5, user_city):
            break

    while True:
        user_rent = input('Do you pay rent? (Y or N):\n')
        user_rent = user_rent.upper()
        if validate_data(6, user_rent):
            break

    while True:
        user_children = input('How many children do you have?(0 for None):\n')
        if validate_data(7, user_children):
            break

    return (user_name, user_email, user_age, user_gender,
            user_country, user_city, user_rent, user_children)


def validate_data(value1, value2):
    try:
        """
        In the first if checks if the value2 has at least one number.
        """
        if ((value1 == 0) and ((any(chr.isdigit() for chr in value2)))):
            raise ValueError()
        if ((value1 == 0) and (value2 == '')):
            print('The field must be filled!')
            raise ValueError()
        if ((value1 == 1) and ('@' not in value2)):
            raise ValueError()
        if ((value1 == 2) and (int(value2) > 110)):
            raise ValueError()
        if ((value1 == 3) and (value2 not in ['M', 'm', 'F', 'f'])):
            raise ValueError()
        if ((value1 == 4) and ((any(chr.isdigit() for chr in value2)))):
            raise ValueError()
        if ((value1 == 4) and (value2 == '')):
            print('The field must be filled!')
            raise ValueError()

        Country = ['US', 'United States', 'AF', 'Afghanistan']

        if (value1 == 4):
            found = 'N'
            for i in Country:
                if value2 == i:
                    found = 'Y'
            if found == 'N':
                raise ValueError()

        if ((value1 == 5) and ((any(chr.isdigit() for chr in value2)))):
            raise ValueError()
        if ((value1 == 5) and (value2 == '')):
            print('The field must be filled!')
            raise ValueError()
        if ((value1 == 6) and (value2 not in ['Y', 'y', 'N', 'n'])):
            raise ValueError()
        if ((value1 == 7) and (int(value2) >= 12)):
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

    """
    Insert the female information into the female worksheet.
    """
    census_last_row = len(SHEET.worksheet("census").get_all_values())
    census_gender = SHEET.worksheet("census").cell(census_last_row, 4).value
    if census_gender == 'F':
        census_worksheet = SHEET.worksheet("female")
        census_worksheet.append_row(data)

    """
    Insert the male information into the male worksheet.
    """
    if census_gender == 'M':
        census_worksheet = SHEET.worksheet("male")
        census_worksheet.append_row(data)

    """
    Insert who has children information into the children worksheet.
    """
    census_children = SHEET.worksheet("census").cell(census_last_row, 8).value
    if int(census_children) >= 1:
        census_worksheet = SHEET.worksheet("with_children")
        census_worksheet.append_row(data)

    """
    Insert who pay rent information into the rent worksheet.
    """
    census_rent = SHEET.worksheet("census").cell(census_last_row, 7).value
    if census_rent == 'Y':
        census_worksheet = SHEET.worksheet("pay_rent")
        census_worksheet.append_row(data)


def update_result_worksheet():
    """
    The number of people searched.
    """
    people_number = (len(SHEET.worksheet("census").get_all_values()) - 1)
    census_worksheet = SHEET.worksheet("result")
    census_worksheet.update_cell(2, 1, people_number)

    """
    The number of men.
    """
    men_number = (len(SHEET.worksheet("male").get_all_values()) - 1)
    census_worksheet = SHEET.worksheet("result")
    census_worksheet.update_cell(2, 2, men_number)

    """
    The number of women.
    """
    women_number = (len(SHEET.worksheet("female").get_all_values()) - 1)
    census_worksheet = SHEET.worksheet("result")
    census_worksheet.update_cell(2, 3, women_number)

    """
    People who pay rent.
    """
    rented_number = (len(SHEET.worksheet("pay_rent").get_all_values()) - 1)
    census_worksheet = SHEET.worksheet("result")
    census_worksheet.update_cell(2, 4, rented_number)

    """
    People who own their own homes.
    """
    owner_number = 0
    owner_number += (people_number - rented_number)
    census_worksheet = SHEET.worksheet("result")
    census_worksheet.update_cell(2, 5, owner_number)

    """
    How many people have children?
    """
    children_number = ((len(SHEET.worksheet("with_children")
                        .get_all_values())-1))
    census_worksheet = SHEET.worksheet("result")
    census_worksheet.update_cell(2, 6, children_number)
    """
    Result
    """
    print(f'The number of people searched: {people_number} \n')
    print(f'The number of men: {men_number} \n')
    print(f'The number of women: {women_number} \n')
    print(f'People who pay rent: {rented_number} \n')
    print(f'People who own their own homes: {owner_number} \n')
    print(f'How many people have children?: {children_number} \n')


def main():
    data = get_users_data()
    update_census_worksheet(data)
    update_result_worksheet()
main()
