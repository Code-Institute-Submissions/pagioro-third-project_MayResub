# Sensu Survey

Sensu survey is a tool for capturing data from a person, and the administrator will have a solid database for future analysis.

![Screenshot of the user data capture program.](./readmeScreenshots/)

Here is the live version of my software!

# Features

### Existing Features

   - The program starts with the Census welcome message and the message to put data in the fields below.       

   - The person must fill in seven fields for data validation to be recorded.

![person input data](./assets/docs/screenshots/header.png)

   - The program is connected to google sheets.

   - They go to the main worksheet called Census as we enter the data.

![main sheet](./assets/docs/screenshots/header.png)

   - When we enter the data, they are also separated into other tabs by gender, who pays the rent and if they have children.

![other sheets](./assets/docs/screenshots/header.png)

   - In the program and the result tab, the total number of people is shown, how many are men or women if they have their own house, how many have children.

![result sheets](./assets/docs/screenshots/header.png)

### Future Features

- Will be added a graph in the results tab.

- Will be added more input data.










   



- __The Game Options__

    - The games options include clear instruction in the footer and the choice of buttons: Rock, Paper and Scissors. 

    - These options are interactive, and the user can click to make their choice.

![game choice](./assets/docs/screenshots/choice.png)

- __Game results__

    - If the user chooses an option, the image will change to the one he chooses and randomly, the computer image will also change.

    - After the computer randomly chooses one, it will be determined the victory of one of the two.

    - The winner is announced to the user above the options button, and the score is updated for either the user or the computer, depending on who on.

    - The results ans score are clear to the user, making the game easy to play, understand who won and waht the score is.

  ![game results](./assets/docs/screenshots/results.png)

  - __Footer__

     - The footer section show the rules to the user.

  ![footer](./assets/docs/screenshots/footer.png)

    # Testing

    - I tested the game in different browsers and they all work.   

    - I tested the game results and are always correct.

    - The header, instructions, options and footer text are all readable and easy to understand.

    - The colour and fonts are easy to read and accessible by running it through lighthouse in devtools.

    ![accessibility](./assets/docs/screenshots/lighthouse.png)

    - This project is responsive, and works on all screens using devtools device toolbars.

    # Unfixed Bugs    

    - No unfixed bugs.

    # Fixed Bugs

    - The tie was not appearing and was resolved with the code let div = document.getElementById('messages') div.innerHTML = 'Tie!' in the game function

    - The images were not showing up, and I forgot to redirect the code to the correct folder.  

    ## Validator Testing

    - HTML
        - No errors were returned when passing through the official W3C validator

    ![html w3c validator](./assets/docs/screenshots/w3chtml.png)

    - CSS
        - No errors were returned when passing through the official (Jigsaw) validator

    ![w3c css validator](./assets/docs/screenshots/w3ccss.png)


    # Deployment

    - The site was deployed to GitHub pages. The steps to deploy are as follows:

    - In the GitHub repository, navigate to the Settings tab In the pages section, go to select branch drop-down menu, select Main Once the Main branch has been selected, a link to the site is provided

    - The live link can be found here - https://pagioro.github.io/second-project/

    # Credits

    ### content

    - When making my project, I was inspired by the Code Institute Rock, Paper, Scissors project where I use as an example the HTML structure to build my project.

    - Font was sourced from Google Fonts https://fonts.google.com/

    ### media

    - Pictures were taken from the Google Images.

### Existing Features
