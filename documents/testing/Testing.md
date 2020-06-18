<h1>Testing</h1>

<p>In this document I am going to describe the various tests that I have carried out on my project in order to ensure that it is functional and meets the required web standards</p>

<hr>

## Unit Tests
<p>In my project, I used the Python and Django’s inbuilt testing suite “Pytest” in order to create a series of unit tests, which would help me test my project automatically. This was really beneficial to me, as it enabled me to always check my work without long periods of manual testing when I introduced a new feature. This gave me a level of confidence whilst creating my project , that I would be able to catch bugs early and as they happened.  </p>
<p>My methodology for writing the test was on separating areas of concern. I wanted to make sure that all of the tests were clearly laid out can could be easily identified and worked on at a future point. Keeping the tests split into sub application areas and then the further breakdown into view, urls, model and form tests which again helped to keep me organised throughout my development life cycle. </p>
<p>The unit tests are run on a local environment and use the built in DB SQLite. In order to run the tests the command “python manage.py test” can be used which will trigger all of the tests to be run.</p>
<p>Below is a summary of the 45 unit tests I have in my project:</p>

| App| Tests Details| file location| 
| :------------- |:-------------| :-------------| 
| Account Urls | testing login, register and logout urls to ensure that they call the correct view function| tests/test_urls.py|
| Account Views| testing the various account view functions such as ensuring that login function authenticates the user successfully | tests/test_views.py|
| Account Forms| testing the various account forms to ensure it can validate correct information and decline invalid | tests/test_forms.py|
| Product Urls | testing product listing and product detail urls to ensure that they call the correct view function| tests/test_urls.py|
| Product Views| testing the various account view functions such as ensuring that the product detail view returns a specific product & that the create comment function requires a logged in user | tests/test_views.py|
| Cart Urls | testing cart urls to ensure that they call the correct view functions| tests/test_urls.py|
| Cart Views| testing the cart view to ensure that functions return the correct templates and that adding an item to the cart redirects the user to the cart overview page. | tests/test_views.py|
| Checkout Urls | testing checkout url to ensure that its calls the correct view function| tests/test_urls.py|
| Checkout Views| testing the checkout views various functions such as checking authenticated access to the page and also that the ajax request returns a bad response if incorrect data is entered | tests/test_views.py|
| Checkout Forms| testing the checkout forms to ensure that both the billing and payment forms validate the information entered correctly and will not let bad data be entered.| tests/test_forms.py|


<hr>

## Client Stories
<p>This section will demonstrate the way in which I have been able to meet the various aspects of my client stories.</p>


### User Story 1 - As a user, I would like to be able to find interesting trips that I am able to purchase through the site.
#### Navigation
<ol>
<li>The navigation bar contains a link which allows the user to navigate straight to the store page, this means the user has access to this no matter where they are on the site. </li>
</ol>

#### Homepage
<ol>
<li>When the user loads the homepage , they are immediately presented with a callout section, which enables the user to navigate to the store page via its call to action button</li>
<li>The home page also contains 4 distinctive buttons below the landing area, which prompt the user to click one of them. Upon the user clicking the images, this will take the user to the store page and it will be prefiltered based upon the users selection. </li>
</ol>

#### Product listing
<ol>
<li>The product listing page contains a number of filters which can be adjusted in order for the user to find a trip they feel is “interesting ” and appeals to them. The user can change the filters at any time and are also able to select multiple filters at the same time.  </li>
<li>The product listing page shows the available products based on the users selection choices. The page features pagination, so that the user does not need to scroll endlessly in order to see all of the available trips</li>
</ol>

#### Product detail
<ol>
<li>The product detail page provides the user with all of the relevant information regarding the trip they have chosen. This includes information on the price, description , location and other users opinions. </li>
<li>The product detail page features the ability to add the product to the users cart. This enables them to purchase this item if they are wanting too.</li>
</ol>

#### Cart
<ol>
<li>The cart system features an overview page, which allows the user to see an overview of all the items the user has selected and is interested in. The checkout section can be accessed through this page.</li>
</ol>

#### Checkout
<ol>
<li>The checkout page allows the user to enter their payment details and actually purchase the product they have selected.</li>
</ol>

### User Story 2 - As a user, I would like to be able to sort through the trips based on a variety of criteria in order to make it easier for me to find a trip I like.
#### Homepage
<ol>
<li>As mentioned previously, the homepage features 4 call to action buttons which allow the user to prefilter the products before they arrive on the store page. This only covers the category filter, however this helps to narrow in on the users requests before they have even got to the store page. </li>
</ol>

#### Product Listing
<ol>
<li>The product listing page contains a number of filters which can be adjusted in order for the user to find a trip they feel is “interesting ” and appeals to them. The user can change the filters at any time and are also able to select multiple filters at the same time.  </li>
<li>The product listing page contains a search filter, this enables the user to enter key words into the search bar, which will then return any products with the matching keywords in its title.</li>
<li>The product listing page also contains a category filter which enables the user to filter the products based upon the categories they fall under such as being a sports trip.</li>
<li>The product listing page also contains a country filter which allows the products to be filtered based on the country in which the trip is located.</li>
<li>The product page also contains a sort by filter which allows the products to be filtered based upon the price using either the highest or lowest first, depending upon what the user selects. </li>
<li>The product listing page contains a date filter which will filter products to only show those which have a start date on or after the date selected by the user.</li>
</ol>

### User Story 3 - As a user, I would like to see where abouts the trip is located so that I can plan more effectively.
#### Product Listing
<ol>
<li>The product cards featured on the listing page show the area and country in which the trip is located. This can also be filtered by the user so that they can see trips which are only available in the area they are interested in. </li>
</ol>

#### Product Detail
<ol>
<li>The product detail page contains a more in depth look at the trip itself. One part of this is the google maps integration which shows the user the precise location of the trip. The maps element allows the user to use all of the expected features of google maps so that they can get all of the information they need. </li>
</ol>

### User Story 4 - As a user, I would like to see the comments and opinions of other users on the trip.
#### Product detail
<ol>
<li>The product detail page contains a comment section. The comments are generated by users with accounts and this enables them to leave a comment which features a title a like and the comment itself. This section shows the user the five most recent comments that have been left regarding the product and will enable them to get a good idea of the general opinion of the trip.</li>
<li>The product detail page also allows the user to leave a comment. Below the comments container is the create comment section. If the user is logged in, this will let the user leave a comment on the trip which can help to influence other users. The user can also leave a like with the comment, which will add to the overall number of likes on a product. </li>
</ol>

### User Story 5 - As a user, I would like to be to add the products I find to a basket so that I can continue to browse..
#### Cart
<ol>
<li>The cart system features an overview page, which allows the user to see an overview of all the items the user has selected and is interested in.  This will show the price of the item along with the quantity the user has selected. </li>
<li>The cart system allows the user to edit the items that are in their basket. They can do this by using the amend feature to alter the number of items in the basket or remove them completely. </li>
<li>The cart page allows the user to continue to shop by featuring a button which enables the user to return to the rest of the site, to continue browsing. The user doesn’t need to checkout until they are ready and have finished browsing. </li>
</ol>

### User Story 6 - As a user, I would like to see any orders I have made in the past with some of its key details.
#### Profile
<ol>
<li> The profile page contains all of the orders the user may have placed through the site. The list breaks down the multiple orders and contains information about its Id, the order line items, the quantity and the total price of the order. The page is also paginated, which means that the number of orders on the screen at any one time will always be manageable and will never force the user into scrolling infinitely to see all of their past orders.  </li>
</ol>

### User Story 7 - As a user, I would like to be able to reset my login details incase I forget my credentials. 
#### Reset password system
<ol>
<li> The first page that is presented in the reset system is the , email entry form. This prompts the user to enter their email into the form. Once the user has done this, the site will send the user an email with a reset link and will take them to the email submission screen.</li>
<li>The email that is sent to the user contains brief information about the user such as their username and also the site. The email also contains a reset link that is uniquely generated for each user and provides them an area on the site to be able enter a new password. </li>
<li> The reset password form is very similar to the registration form but only uses the password fields. The user is able to enter a new password that will be used to enable to login to the site. Upon entry of a new valid password, the user is told the reset has been successful enabling them to login to the site once again. </li>
</ol>

<hr>

## Manual Testing
<p>Alongside my unit tests, I also carried out manual testing of my site. I ensured I spent time doing this as there are certain elements that unit tests may miss such as style issues and other such bugs. </p>
<p>To carry out my manual testing I followed my user stories and made sure that the user was able to successfully perform each of the user stories successfully. Through doing this I was able to find a number of bugs which could have prevented the user from being able to successfully complete the story.  </p>
<p>Please note that all of the tests were performed on a number of different browsers including Chrome, Firefox, Edge & Safari. I also performed each of these tests on both desktop and mobile devices to check it worked consistently across all devices. I will specify unique tests that were performed on either screen size</p>

### User Story 1 - As a user, I would like to be able to find interesting trips that I am able to purchase through the site.
<ul>
<li>Checked that the navigation element for the store when clicked loaded the store successfully. </li>

<li>Mobile – Checked that the store navigation element could be clicked and that it would take the user to the store page on the mobile nav menu. </li>
<li> Checked that the homepage store call to action store buttons worked when clicked and that they successfully loaded the store page with the correct filters applied.  </li>
<li>When the store page loaded, checked that trips actually appeared in the list and that the filters could be used to change the type and amount of trips being shown. </li>
<li>Checked that clicking on the trip view button loaded the product detail page correctly. </li>
<li>Checked that pressing the add to cart button actually added the item to the cart. Confirmed this by following the redirect through to the cart overview page and seeing the item and its details in there. Furthermore, I also validated this by checking that the number of items in the cart icon appeared. </li>
<li>On the cart overview screen, I checked that you were able to click the checkout button and that it allows the user to be redirected to the checkout screen when logged in. </li>
<li>Checked that the navigation element for the store when clicked loaded the store successfully. </li>
<li>When the checkout page loaded, checked that I could enter correct information into both the billing and payment forms and that these forms would validate the input. I also checked that the validation messages were visible on both mobile and desktop screens. Finally I checked that when valid information was entered, this notified the user of the success and placed the order.</li>
</ul>

### User Story 2 - As a user, I would like to be able to sort through the trips based on a variety of criteria in order to make it easier for me to find a trip I like.
<ul>
<li> On the homepage, I checked that each of the store call to action buttons worked correctly and would filter to the correct category based on the button that was selected.  </li>
<li>Mobile – Checked that the buttons appeared correctly on mobile view and that the resolution of the images was correct. Repeated the above test of clicking the icons and checking the prefiltered trips were correct. </li>
<li>On the store page, I checked that the filters all appeared and that I could interact with each of the category items and the submission buttons. </li>
<li> Mobile – I checked that the filters were hidden on page load and were instead replaced with a show filters button. After confirming this, I pressed the show filters button and checked that the filters then displayed to the user and that all of the filter elements could still be interacted with.</li>
<li> I checked each of the filters one by one to ensure that when I selected them, they applied filters to available trips. After I had tested and confirmed each of the filters functionality, I then started to test the filters in various combinations, to confirm that the products filtered even when 3-4 filters were active at the same time. As before I repeated this step on mobile.</li>
</ul>

### User Story 3 - As a user, I would like to see where abouts the trip is located so that I can plan more effectively.
<ul>
<li> Checked that on the store page, I could clearly see the location of the trip. I also verified that I could filter based on the location, when I performed my tests on the previous user story. </li>
<li>Mobile - Checked that the location of the trip could still be clearly seen on the mobile layout and that again the country filter could be applied. </li>
<li> When I accessed the trip detail page, I checked that the google maps API loaded the google maps client correctly and displayed at an appropriate size for the screen the site was being viewed on. </li>
<li> Checked that the google map client showed the correct location and that a pin was clearly dropped on the location of the trip. I then tested that I could successfully interact with the map and checked things like the zoom function. </li>
<li> I loaded a product that didn’t have and location details and checked that the map client was not shown, to avoid errors on the maps client.</li>
</ul>

### User Story 4 - As a user, I would like to see the comments and opinions of other users on the trip.
<ul>
<li> Loaded the product detail page and checked that I could see the comment section loaded on the page. I also made sure that all of the details surrounding the comment such as the title, like status date posted etc.</li>
<li> Checked that if I was not logged in, I could still see the comment section, however I made sure that the user could not see the create comment element.</li>
<li>I loaded the page as a logged in user to check that I could see the comment section.</li>
<li>I checked when using an authenticated account that I could leave a comment. I tested the validation on the form when bad data was entered. I also tested that the like button would activate when clicked and would check the hidden checkbox through the element inspector in chrome. Finally I checked that when I submitted valid data, that it created the comment and showed this in the comment section. </li>
<li>I checked on a comment entry that the like counter increased when I left a like with the comment. </li>
</ul>

### User Story 5 - As a user, I would like to be to add the products I find to a basket so that I can continue to browse.
<ul>
<li>I loaded a product page up and checked that I could add the product being viewed to the cart. I experimented with the quantity that I could choose and made sure that when I clicked add, it redirected me to the cart overview page.</li>
<li>Checked when the cart over page loaded that it detailed all of the products I had added and their various details such as price, quantity etc. </li>
<li>When I added a product, I checked to see if the cart icon number showed and reflect the amount of items currently in the cart.</li>
<li> Tested that when I altered the quantity value for each product, it changed the show quantity in the cart and also altered the icon number.</li>
<li> Tested that when the quantity was changed to 0 , it deleted the item from the quantity and successfully removed it from the cart.</li>
</ul>

### User Story 6 - As a user, I would like to see any orders I have made in the past with some of its key details.
<ul>
<li> Checked that when a user wasn’t logged in, I couldn’t access the profile page, through the UI or via its URL. </li>
<li> Checked when using an account with no orders that it displayed this clearly to the user so there was no confusion as to the purpose of the page.</li>
<li> I tested an account which I knew had multiple orders and loaded the profile page. Upon the load, I checked that all of the users past orders when listed. I checked that all of the details of the order could be seem including its ID, total price, line items etc. I checked that the pagination worked when there was more than the set limit per page.</li>
<li> I tested that when I placed an order with one of the products on the store that it appeared in the list of orders on the profile page.</li>
</ul>

### User Story 7 - As a user, I would like to be able to reset my login details incase I forget my credentials.
<ul>
<li> Checked that I could load the reset email form. I tested the form by entering invalid data to check its validation. I then entered a correct email for an account and checked that it redirected me to the sent screen to confirm an email has been sent.</li>
<li> After submitting my accounts email for reset, I checked the actual email account to see if a reset email was sent. I checked that I could click the link and that it sent me to the reset password form.</li>
<li> I checked the password fields by entering invalid data for validation. I then entered good data and checked that the password reset and that I was redirected to the password success screen.</li>
<li> I then confirmed that I could login to the account with the new password. </li>
</ul>

<hr>
<h3>Validation</h3>
<p>In order to ensure my code has meet the various standards, I have used the following validation services to test different elements of my code. </p>
<ul>
<li><a href=”https://validator.w3.org/” target="_blank">W3C Markup Validation</a> was used to validate HTML code.</li>
<li><a href=”https://jigsaw.w3.org/css-validator/” target="_blank">W3C CSS Validation</a> was used to validate CSS code.</li>
<li><a href=”https://jshint.com/” target="_blank">JS Hint</a> was used to validate Javascript code.</li>
</ul>
<p>All of the validation tests resulted in a few minor changes that I needed to make, and all my files now conform to the latest web standards. </p>

