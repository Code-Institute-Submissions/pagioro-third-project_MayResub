# Census Survey

Census Survey is a tool for capturing data from a person, and the administrator will have a solid database for future analysis.

![Screenshot of the user data capture program.](./Readme_ScreenShots/census.png)

[Here is the live version of my software!](https://census-updated.herokuapp.com/)

[Here is the google sheets data!](https://docs.google.com/spreadsheets/d/1h8qsWk0Q3EEqi7zpqlX5rRxLMbBciOyYTID0DMKAOfU/edit?usp=sharing)

# Features

### Existing Features

   - The program starts with the Census welcome message and the message to put data in the fields below.       
   - The person must fill in seven fields for data validation to be recorded.

![person input data](./Readme_ScreenShots/inputData.png)

   - The program is connected to google sheets.
   - The data go to the main worksheet called Census.

![main sheet](./Readme_ScreenShots/mainSheet.png)

   - When we enter the data, they are also separated into other tabs by gender, who pays the rent and if they have children.

![other sheets](./Readme_ScreenShots/sheets.png)

   - In the program and the result tab, the total number of people is shown, how many are men or women if they have their own house, how many have children.

![result sheets](./Readme_ScreenShots/result.png)

### Future Features

   - Will be added a graph in the results tab.
   - Will be added more input data.

# Testing

   - Passed the code through a PEP8 linter and confirmed there are no problems.
   - All data inputs have been tested and are working perfectly.
   - The program presents an error when testing the blank name field and returns to the same field.
   - The program returns an error when testing the name field with a number and returns to the name field.
   - When testing the name field with letters and numbers, the program returns an error and returns to the name field.

![testing name field](./Readme_ScreenShots/testingName.png)


   - The program presents an error when testing the blank email field and returns to the same field.
   - The program returns an error when testing the email field with letters only and returns to the same field.
   - When testing the email field with letters and numbers, the program returns an error and returns to the same field.
   - When testing the email field with numbers, the program returns an error and returns to the same field.

![testing email field](./Readme_ScreenShots/testingEmail.png)


   - The program presents an error when testing the blank age field and returns to the same field.
   - The program returns an error when testing the age field with letters only and returns to the same field.
   - When testing the age field with letters and numbers, the program returns an error and returns to the same field.
   - When testing the age field with special character, the program returns an error and returns to the same field.   
   
![testing email field](./Readme_ScreenShots/testingAge.png)


   - The program presents an error when testing the blank gender field and returns to the same field.
   - The program returns an error when testing the gender field with special character and returns to the same field.
   - When testing the gender field with letters that are different from M and F, the program returns an error and returns to the same field.

![testing email field](./Readme_ScreenShots/testingGender.png)


   - The program presents an error when testing the blank country field and returns to the same field.
   - The program returns an error when testing the country field with special character and returns to the same field.
   - The program returns an error when testing the country field with names that are not in the world country list and returns to the same field.

![testing email field](./Readme_ScreenShots/testingCountry.png)


   - The program presents an error when testing the blank city field and returns to the same field.
   - The program returns an error when testing the city field with special character and returns to the same field.
   - The program returns an error when testing the city field with numbers and returns to the same field.  

![testing email field](./Readme_ScreenShots/testingCity.png)


   - The program presents an error when testing the blank rent field and returns to the same field.
   - The program returns an error when testing the rent field with special character and returns to the same field.
   - The program returns an error when testing the rent field with numbers and returns to the same field.  

![testing email field](./Readme_ScreenShots/testingRent.png)


   - The program presents an error when testing the blank children field and returns to the same field.
   - The program returns an error when testing the children field with special character and returns to the same field.
   - The program returns an error when testing the children field with letters and returns to the same field.
   - The program returns an error when testing the children field with numbers higher than 12 and returns to the same field.  

![testing email field](./Readme_ScreenShots/testingChildren.png)





  

   



# Unfixed Bugs    

   - No unfixed bugs.

# Fixed Bugs

   - I had difficulties validating capital and lowercase letters in a part of the code, and I solved this by using .upper(). 
       - user_gender = user_gender.upper() and user_rent = user_rent.upper()

   - I could not calculate the number of lines correctly because it always took the title. I solved it by subtracting by minus one in the code below.
       -  people_number = (len(SHEET.worksheet("census").get_all_values()) - 1)

   - To change a cell, I used the update_cell command and not .append, which was the error I was making.
       - census_worksheet.update_cell(2, 1, people_number)

## Validator Testing

   - No errors were returned from PEP8online.com

![pep8 online](./Readme_ScreenShots/pep8.png)

# Deployment

This project was deployed using Code Institute's mock terminal for Heroku.
   - Steps for deployment:
       - Fork or clone this repository
       - Create a new Heroku app
       - Link the Heroku app to this repository
       - Click on deploy

# Credits

   - Code institute for the deployment terminal
   - Love Sandwiches by the example given
   - Ultimate Battleships Sample README

