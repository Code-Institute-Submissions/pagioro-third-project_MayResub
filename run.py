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
    print('bit.ly/3MQfbb8\n')

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


def countries(value2):
    Country = ['US', 'UNITED STATES',
               'AF', 'AFGHANISTAN',
               'AL', 'ALBANIA',
               'DZ', 'ALGERIA',
               'AS', 'AMERICAN SAMOA',
               'AD', 'ANDORRA',
               'AO', 'ANGOLA',
               'AI', 'ANGUILLA',
               'AQ', 'ANTARCTICA',
               'AG', 'ANTIGUA AND BARBUDA',
               'AR', 'ARGENTINA',
               'AM', 'ARMENIA',
               'AW', 'ARUBA',
               'AU', 'AUSTRALIA',
               'AT', 'AUSTRIA',
               'AZ', 'AZERBAIJAN',
               'BS', 'BAHAMAS',
               'BH', 'BAHRAIN',
               'BD', 'BANGLADESH',
               'BB', 'BARBADOS',
               'BY', 'BELARUS',
               'BE', 'BELGIUM',
               'BZ', 'BELIZE',
               'BJ', 'BENIN',
               'BM', 'BERMUDA',
               'BT', 'BHUTAN',
               'BO', 'BOLIVIA',
               'BA', 'BOSNIA AND HERZEGOWINA',
               'BW', 'BOTSWANA',
               'BV', 'BOUVET ISLAND',
               'BR', 'BRAZIL',
               'BN', 'BRUNEI DARUSSALAM',
               'BG', 'BULGARIA',
               'BF', 'BURKINA FASO',
               'BI', 'BURUNDI',
               'KH', 'CAMBODIA',
               'CM', 'CAMEROON',
               'CA', 'CANADA',
               'CV', 'CAPE VERDE',
               'KY', 'CAYMAN ISLANDS',
               'CF', 'CENTRAL AFRICAN REP',
               'TD', 'CHAD',
               'CL', 'CHILE',
               'CN', 'CHINA',
               'CX', 'CHRISTMAS ISLAND',
               'CC', 'COCOS ISLANDS',
               'CO', 'COLOMBIA',
               'KM', 'COMOROS',
               'CG', 'CONGO',
               'CK', 'COOK ISLANDS',
               'CR', 'COSTA RICA',
               'CI', 'COTE D`IVOIRE',
               'HR', 'CROATIA',
               'CU', 'CUBA',
               'CY', 'CYPRUS',
               'CZ', 'CZECH REPUBLIC',
               'DK', 'DENMARK',
               'DJ', 'DJIBOUTI',
               'DM', 'DOMINICA',
               'DO', 'DOMINICAN REPUBLIC',
               'TP', 'EAST TIMOR',
               'EC', 'ECUADOR',
               'EG', 'EGYPT',
               'SV', 'EL SALVADOR',
               'GQ', 'EQUATORIAL GUINEA',
               'ER', 'ERITREA',
               'EE', 'ESTONIA',
               'ET', 'ETHIOPIA',
               'FK', 'FALKLAND ISLANDS MALVINAS',
               'FO', 'FAROE ISLANDS',
               'FJ', 'FIJI',
               'FI', 'FINLAND',
               'FR', 'FRANCE',
               'GF', 'FRENCH GUIANA',
               'PF', 'FRENCH POLYNESIA',
               'TF', 'FRENCH S. TERRITORIES',
               'GA', 'GABON',
               'GM', 'GAMBIA',
               'GE', 'GEORGIA',
               'DE', 'GERMANY',
               'GH', 'GHANA',
               'GI', 'GIBRALTAR',
               'GR', 'GREECE',
               'GL', 'GREENLAND',
               'GD', 'GRENADA',
               'GP', 'GUADELOUPE',
               'GU', 'GUAM',
               'GT', 'GUATEMALA',
               'GN', 'GUINEA',
               'GW', 'GUINEA-BISSAU',
               'GY', 'GUYANA',
               'HT', 'HAITI',
               'HN', 'HONDURAS',
               'HK', 'HONG KONG',
               'HU', 'HUNGARY',
               'IS', 'ICELAND',
               'IN', 'INDIA',
               'ID', 'INDONESIA',
               'IR', 'IRAN',
               'IQ', 'IRAQ',
               'IE', 'IRELAND',
               'IL', 'ISRAEL',
               'IT', 'ITALY',
               'JM', 'JAMAICA',
               'JP', 'JAPAN',
               'JO', 'JORDAN',
               'KZ', 'KAZAKHSTAN',
               'KE', 'KENYA',
               'KI', 'KIRIBATI',
               'KP', 'KOREA NORTH',
               'KR', 'KOREA SOUTH',
               'KW', 'KUWAIT',
               'KG', 'KYRGYZSTAN',
               'LA', 'LAOS',
               'LV', 'LATVIA',
               'LB', 'LEBANON',
               'LS', 'LESOTHO',
               'LR', 'LIBERIA',
               'LY', 'LIBYA',
               'LI', 'LIECHTENSTEIN',
               'LT', 'LITHUANIA',
               'LU', 'LUXEMBOURG',
               'MO', 'MACAU',
               'MK', 'MACEDONIA',
               'MG', 'MADAGASCAR',
               'MW', 'MALAWI',
               'MY', 'MALAYSIA',
               'MV', 'MALDIVES',
               'ML', 'MALI',
               'MT', 'MALTA',
               'MH', 'MARSHALL ISLANDS',
               'MQ', 'MARTINIQUE',
               'MR', 'MAURITANIA',
               'MU', 'MAURITIUS',
               'YT', 'MAYOTTE',
               'MX', 'MEXICO',
               'FM', 'MICRONESIA',
               'MD', 'MOLDOVA',
               'MC', 'MONACO',
               'MN', 'MONGOLIA',
               'MS', 'MONTSERRAT',
               'MA', 'MOROCCO',
               'MZ', 'MOZAMBIQUE',
               'MM', 'MYANMAR',
               'NA', 'NAMIBIA',
               'NR', 'NAURU',
               'NP', 'NEPAL',
               'NL', 'NETHERLANDS',
               'AN', 'NETHERLANDS ANTILLES',
               'NC', 'NEW CALEDONIA',
               'NZ', 'NEW ZEALAND',
               'NI', 'NICARAGUA',
               'NE', 'NIGER',
               'NG', 'NIGERIA',
               'NU', 'NIUE',
               'NF', 'NORFOLK ISLAND',
               'MP', 'NORTHERN MARIANA ISLANDS',
               'NO', 'NORWAY',
               'OM', 'OMAN',
               'PK', 'PAKISTAN',
               'PW', 'PALAU',
               'PA', 'PANAMA',
               'PG', 'PAPUA NEW GUINEA',
               'PY', 'PARAGUAY',
               'PE', 'PERU',
               'PH', 'PHILIPPINES',
               'PN', 'PITCAIRN',
               'PL', 'POLAND',
               'PT', 'PORTUGAL',
               'PR', 'PUERTO RICO',
               'QA', 'QATAR',
               'RE', 'REUNION',
               'RO', 'ROMANIA',
               'RU', 'RUSSIAN FEDERATION',
               'RW', 'RWANDA',
               'KN', 'SAINT KITTS AND NEVIS',
               'LC', 'SAINT LUCIA',
               'VC', 'ST VINCENT/GRENADINES',
               'WS', 'SAMOA',
               'SM', 'SAN MARINO',
               'ST', 'SAO TOME',
               'SA', 'SAUDI ARABIA',
               'SN', 'SENEGAL',
               'SC', 'SEYCHELLES',
               'SL', 'SIERRA LEONE',
               'SG', 'SINGAPORE',
               'SK', 'SLOVAKIA',
               'SI', 'SLOVENIA',
               'SB', 'SOLOMON ISLANDS',
               'SO', 'SOMALIA',
               'ZA', 'SOUTH AFRICA',
               'ES', 'SPAIN',
               'LK', 'SRI LANKA',
               'SH', 'ST. HELENA',
               'PM', 'ST.PIERRE',
               'SD', 'SUDAN',
               'SR', 'SURINAME',
               'SZ', 'SWAZILAND',
               'SE', 'SWEDEN',
               'CH', 'SWITZERLAND',
               'SY', 'SYRIAN ARAB REPUBLIC',
               'TW', 'TAIWAN',
               'TJ', 'TAJIKISTAN',
               'TZ', 'TANZANIA',
               'TH', 'THAILAND',
               'TG', 'TOGO',
               'TK', 'TOKELAU',
               'TO', 'TONGA',
               'TT', 'TRINIDAD AND TOBAGO',
               'TN', 'TUNISIA',
               'TR', 'TURKEY',
               'TM', 'TURKMENISTAN',
               'TV', 'TUVALU',
               'UG', 'UGANDA',
               'UA', 'UKRAINE',
               'AE', 'UNITED ARAB EMIRATES',
               'UK', 'UNITED KINGDOM',
               'UY', 'URUGUAY',
               'UZ', 'UZBEKISTAN',
               'VU', 'VANUATU',
               'VA', 'VATICAN CITY STATE',
               'VE', 'VENEZUELA',
               'VN', 'VIET NAM',
               'VG', 'VIRGIN ISLANDS BRITISH',
               'VI', 'VIRGIN ISLANDS U.S.',
               'EH', 'WESTERN SAHARA',
               'YE', 'YEMEN',
               'YU', 'YUGOSLAVIA',
               'ZR', 'ZAIRE',
               'ZM', 'ZAMBIA',
               'ZW', 'ZIMBABWE']

    found = False
    for i in Country:
        if value2 == i:
            found = True

    return(found)


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
        if (value1 == 4):
            if ((any(chr.isdigit() for chr in value2))):
                raise ValueError()
            if (value2 == ''):
                print('The field must be filled!')
                raise ValueError()

            result = countries(value2)
            if not result:
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
