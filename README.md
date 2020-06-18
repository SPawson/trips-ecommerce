

<h1>Trips | Code Institute Fourth Milestone Project</h1>

<p>This project has been completed as part of my submission for my fourth milestone stone project as part of my Code Institute Full stack software development course. The website is intended to replicate the look and functionality of other popular holiday and trip booking ecommerce sites. </p>

<p>The application includes a number of features, such as a full login system , ecommerce functionality, order history and other features expected in this type of site. In order to create this full stack application, I have used the Django framework with python and the Stripe API to handle the payment side. </p>

<p>The application can be viewed on Heroku via the following address:
<a target="_blank" href="https://trips-ecommerce.herokuapp.com/">https://trips-ecommerce.herokuapp.com/</a></p>

<p>This site has been created purely for educational purposes and does not provide any service/products to the user. Please do not enter any personal information. In order to use the Ecommerce functionality, please use stripes test card in order to make payments</p>
<p>Test Card Number: 4242 4242 4242 4242</p>
<p>Please see the Stripe Documentation for more information <a target="_blank" href="https://stripe.com/docs/testing”> https://stripe.com/docs/testing</a></ </p>

</hr>
<br>

# UX

## Overview

<p>The main focus of this application was to create a Full Stack app to demonstrate the knowledge and skills I have learned through the entirety of the course. As mentioned above I have used a variety of languages/technologies in order to demonstrate my proficiency. For this project I am using Django/Python on the backend and am using JQuery, JavaScript, SASS and Stripe in order to allow me to create this. </p>

<p>The main focus of the site experience is to allow users to find unique and interesting activities and trips to experience. This means that I have designed the site and included functionality in order to enhance the users experience when using the site and create a positive impression. </p>

## Wireframes
<p> During the development stage of my project I generated some wireframes for both the mobile and desktop approaches using Balsamiq. Throughout the course of developing the website, I have deviated from the wireframes in certain sections. This is mainly due to me discovering a better design during the development, or issues with implementing the feature. </p>

<p>The wireframes have been uploaded with the rest of my project and can be viewed <a target="_blank" href="documents/wireframes">here.</a></p>

## User Stories
<p>In the development stage of the project, I generated a number of user stories which heavily influenced the design decisions taken throughout the development of the application. They are as follows:</p>

<ul>
<li>As a user, I would like to be able to find interesting trips that I am able to purchase through the site.</li>
<li>As a user, I would like to be able to sort through the trips based on a variety of criteria in order to make it easier for me to find a trip I like. </li>
<li>As a user, I would like to see where abouts the trip is located so that I can plan more effectively.</li>
<li>As a user, I would like to see the comments and opinions of other users on the trip</li>
<li>As a user, I would like to be to add the products I find to a basket so that I can continue to browse.</li>
<li>As a user, I would like to see any orders I have made in the past with some of its key details. </li>
<li>As a user, I would like to be able to reset my login details incase I forget my credentials.</li>
</ul>

# Features

## Existing Features

### Feature 1 – User Registration
<p> The user is able to register as a member of the site, in order to access certain features, such as being able to use the ecommerce functionality. The feature was implemented as I needed to provide a secure way to enable users to interact with the site and give traceability to the orders, comments etc that were being left. It is not a necessity for users to register in order to browse the site, however this greatly enhances their experience and gives them access to all the functionality of the site </p>

### Feature 2 – User Login
<p> If the user has valid login details, they are able to log into the site which enables them to access more features. The feature was implemented in this way to allow only registered users certain privileges when interacting with the site. If this was not the case, anybody could access these features, which could lead to issues. </p>

### Feature 3 – User password reset system
<p> The site contains the ability for the user to be able to reset their user credentials if they were to forget them. The main reason this feature has been included was to give the user the ability to recover their account if they forgot their details. This means that the users account will not be lost, and they can keep the ability to review their order history etc. </p>

### Feature 4 – Search for trips using a variety of criteria
<p> The product finding system contains a comprehensive filtering system which allows users to search for products using a variety of different filters. The main reason this system was implemented was to enhance the users ability to find trips based on their specific wants and needs. This will improve the users experience when using the site. </p>

### Feature 5 – Google Maps Integration
<p> The trip detail page features Googles maps integration which allows the user to see the exact location of the trip. This will allow the user to be more informed on the details of the trip which will improve the users experience  . </p>

### Feature 6 – Comments
<p> The trip detail page also contains a comment section which allows users to view and leave comments. This feature was added to allow users to see what others opinions on the trips are. This helps improve the user experience as reading others informative views will help the user to create their own opinion.  </p>

### Feature 7 – Cart System
<p> The site contains a cart system which allows the user to add products to their basket whilst they are using the site. This increases the usability of the site as it means that the user has the convenience of being able to pay for a number of different items all at once. In addition, the cart allows the user to adjust the quantity of items within the cart itself. This again improves the user experience as it is an easy system to use and is also very convenient. </p>

### Feature 8 – Checkout
<p>The site contains a fully functional checkout system which allows the user to purchase products that they have found on the site. The payment process is handled by the Stripe API, which provides industry standard security and protection for the user. </p>

Feature 9 – Profile (Order History)
<p>The site contains a profile section which allows users to track the orders placed by the user. This creates a convenient place for users to review what they have bought and also allows them to gather all the necessary information they may need about their booking. </p>

## Features left to implement

<p>The following features are things I would like to include in the future. Currently a limit in time or lack of understanding has prevented me from implementing these features in the current build. However, I will look to add these going forward. </p>
### Feature 1 – Refund/Cancellation System
<p>One feature I would like to add to the application in the future would be the ability for the site to process refund/return requests from the users. This would greatly increase the user experience as the convenience of being able to request a cancellation or refund on the site will be very valuable, as it will save them time and stress.</p>

### Feature 2 – Email Order Confirmation
<p>Another feature I would like to add to the application going forward would be an email confirmation upon the order being placed. I think this would further enhance the users interaction with the site and would provide further confirmation that the user has successfully purchased a product. </p>


<hr>

## Technologies Used

## HTML, CSS & JavaScript<
<p>Used as the base languages in this project:</p>
<ul>
<li>HTML: <a target="_blank" href="https://www.w3.org/html/">https://www.w3.org/html/</a></li>
<li>CSS: <a target="_blank" href="https://www.w3.org/Style/CSS/">https://www.w3.org/Style/CSS/</a></li>
<li>JavaScript: <a target="_blank" href="https://www.w3.org/standards/webdesign/script">https://www.w3.org/standards/webdesign/script</a></li>
</ul>

### Bootstrap
<p>The project uses Bootstrap 4.5 framework and a variety of imported classes in order assist with implementing the structure and modal features seen on the site.</p>
<a target="_blank" href="https://getbootstrap.com/">https://getbootstrap.com/</a>

### JQuery
<p>The project uses JQuery to help execute certain Materialize and JavaScript features such as with DOM manipulation and modal functionality .</p>
<a target="_blank" href="https://jquery.com/">https://jquery.com/</a>

### Google Fonts
<p>The project uses Google Fonts to provide the ‘Lato’ font that is used as the applications main font.</p>
<a target="_blank" href="https://fonts.google.com/">https://fonts.google.com/</a>

<h3>Font Awesome</h3>
<p>Used in order to provide a variety of Icons such as the ones used in the social section in the footer.</p>
<a target="_blank" href="https://fontawesome.com/">https://fontawesome.com/</a>

### Python
<p>The project uses python on the backend in order to process the server requests and process the logic of the site. </p>
<a target="_blank" href="https://www.python.org/">https://www.python.org/</a>

### Django
<p>The project uses Django which is a Python framework which provides an array of useful features and functions which assist with BE development. </p>
<a target="_blank" href="https://www.djangoproject.com/">https://www.djangoproject.com/</a>

### SQL
<p>The project uses an SQL database to store and manage the data behind the application. The application uses SQLite for the development database and uses Postgres for the production db.  </p>
<a target="_blank" href="https://www.sqlite.org/index.html">https://www.sqlite.org/index.html</a>
<a target="_blank" href="https://www.postgresql.org/">https://www.postgresql.org/</a>

### Microsoft’s VS Code
<p>VS Code has been used throughout the project as my IDE. </p>
<a target="_blank" href="https://code.visualstudio.com/">https://code.visualstudio.com/ </a>

### Git & GitHub
<p>Git and GitHub have been used throughout the project as a way to manage version control of the web application and its code. </p>
<a target="_blank" href="https://github.com/">https://github.com/</a>

<hr>

## Resources

<p>Throughout the course of the project I also used the following resources to assist me in creating the application:</p>

<ul>
<li><a target="_blank" href="https://www.w3schools.com/">https://www.w3schools.com/</a></li>
<li><a target="_blank" href="https://stackoverflow.com">https://stackoverflow.com</a></li>
<li><a target="_blank" href="https://tinypng.com/">https://tinypng.com/</a></li>
<li><a target="_blank" href="https://developer.mozilla.org/en-US/">https://developer.mozilla.org/en-US/</a></li>
<li><a target="_blank" href="https://www.quora.com/">https://www.quora.com</a></li>
<li><a target="_blank" href="https://www.google.com/">https://www.google.com</a></li>
<li><a target="_blank" href="https://www.youtube.com/">https://www.youtube.com</a></li>

</ul>

<hr>

## Testing
<p>All testing that I have completed in regards to the user story can be viewed on a separate document <a target="_blank" href="documents/testing/testing.md">here</a></p>

<h3>Issues Encountered</h3>
<p>Throughout the course of my testing, I discovered a few bugs which I have detailed below:</p>
<ul>
<li>One issue that I encountered was with trying to get my pagination to work with filtered content. The main issue I was encountering was that I could get pagination to show when I selected a filter type, however when I went to the next page, the filters would be lost. In order to resolve this, I had to create a template helper for my pagination, which checked every element of the query string and retrieve these key value pairs. After doing this, I made it so that these elements of the query string where then appended to the next and previous buttons on the pagination, so that the filter options were persisted no matter where you were in the pagination sequence. </li>

<li>Another issue that I encountered in my testing was with the google maps API when the product didn’t have any latitude or longitude properties set. This led to a number of errors in the console surrounding properties being set etc. In order to resolve this, I added data attributes to the map element that and then checked whether these were set or not in my code. I then wrapped the google maps code in an if else statement and the google maps API call would only be called if the latitude and longitude variables had values. </li>
</ul>

## Deployment

<p>I have deployed this project using Heroku and this can be found here: <a target="_blank" href="https://trips-ecommerce.herokuapp.com/">https://trips-ecommerce.herokuapp.com/</a></p>
<p>In order to run Trips locally the following steps can be taken:</p>

1. To download or clone the site to your local machine you will need to go to my [repo]( https://github.com/SPawson/trips-ecommerce) see steps in https://help.github.com/en/articles/cloning-a-repository .
2.  Before you download or clone the site you will need to ensure you have [Python 3.7](https://www.python.org/downloads/) installed. 
3. Once you have Python installed, create a virtual environment as appropriate to you chosen IDE and os. I recommend using [Microsoft visual code] (https://code.visualstudio.com/)
4. In order to install all  of the dependencies required to run the project, you can do this via the requirements.txt file using the *****pip _install_ -r _requirements_.txt***** command once you have activated your virtual environment. This should install all of the packages listed in the file.
5. Use the command ***python manage,py runserver*** to get the project running on your localhost.
6. You will need to change the email settings in **settings.py** to get the project  to send password reset emails via your own email services.
7. In order to deploy the site I used Heroku to my site. On Heroku I used a postgres to host my production database and used Heroku’s config vars in order to set the necessary environment variables to allow the site to run. I linked the Heroku app to the github repo via the deployment section of the Heroku app and set the automatic deployment option, so that the site would deploy on me pushing work to Github. I used gunicorn to run the app in heroku and whitenoise to manage the static files with AWS. A procfile is also needed by heroku with the line ***web: gunicorn dev_assist.wsgi:application*** to let heroku know how to run the web app. Heroku also requires the **requirement.txt** file to inform it of any relative dependencies for the app.

<hr>

<h2>Credits</h2>
<h3>Images</h3>
<h4>Disclaimer</h4>
<p>Please note this project is for educational purposes only. </p>
<ul>
<li>Static images used in various parts of the site were obtained from<a href=”https://unsplash.com/” target=”_blank”>Unsplash</a></li>
<li>The landing page video was obtained from <a href=”https://coverr.co/” target=”_blank”>Coverr</a></li>

</ul>
<h3>Acknowledgements</h3>
<p>The website takes inspiration from the Code Institutes Ecommerce mini project </p>
<p>Thank you to members of the Code Institute slack community for assistance when I was encountering issues during the development and to my family friends for assisting with the testing of this website.</p>

