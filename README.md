[![Build Status](https://travis-ci.org/jonw83/issue-tracker-jw.svg?branch=master)](https://travis-ci.org/jonw83/issue-tracker-jw)

# [Issue Tracker](https://issue-tracker-jw.herokuapp.com/)

This game has been developed for my Full Stack Frameworks Milestone Project as part of the Code Institute’s Diploma in Full Stack Web Development course.

## UX

### User Stories

The purpose of the website is for developers to submit requests to resolve bugs or add features to their existing websites and applications. Visitors to the site will therefore:

- Need to understand what services are offered.
- Be able to resigster and subsquently log in and out to access the services.
- Be able to submit a request for a Bug resolution or Feature implementation.
- For Features, which all command a £99.99 charge, be able to add the request to the shopping cart.
- For Features, be able to checkout the request and submit payment details.
- Be able to see the status of their submitted Bug or Feature request.
- Be ale to search for a Bug or Feature.
- Be able to upvote a Bug or Feature if they like it.
- For superusers only, edit a Bug or Feature to update the status of the request.

## Features

### Existing Features

1. The home app explains the purpose of the website and the servies that are availabe to visitors. All Bug and Feature requests are also displayed here, where details can be viewed, including the current status.
1. The accounts app allows the user to register, log in, log out and view their profile details.
1. The issues app displays the list of all requested Bugs and Features and their respective details. It also provides registered users with the ability to add a new issue. Registered superuser's can edit an issue to update the status.
1. The search app allows registered users to search for a Bug or Feature request.
1. The cart app allows registered users who request a Feature development to add their Feature request to a shopping cart.
1. The checkout app allows registered users who have added a Feature request to the cart to checkout the request and pay for the service.

## Technologies Used

The app was built using [Python](https://www.python.org/) code.

Other technologies used in this project are:

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), the most basic building block of the Web.
  - for writing the basic front-end content.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), a stylesheet language.
  - for styling the page.
- [Django](https://www.djangoproject.com/), A high-level Python Web framework.
  - for creating a SQLite database.
- [PostgreSQL](https://www.postgresql.org/), An open source object-relational database.
  - for hostinmg in the cloud on Heroku.
- [Stripe Payments](https://stripe.com/gb?utm_campaign=paid_brand-UK_en_Search_Brand_Stripe-2032860449&utm_medium=cpc&utm_source=google&ad_content=355351450259&utm_term=stripe%20pay&utm_matchtype=e&utm_adposition=1t1&utm_device=c&gclid=CjwKCAjwm4rqBRBUEiwAwaWjjGwZ1ODfsQvfW_8NiIR3ZVihr9MmvBpeO1YBQ0YRPqldzoZ8JeZYfxoCnaUQAvD_BwE)
  -  to allow registered users to make payments over the Internet.
- [JQuery](https://jquery.com)
  - for allowing the Javascript functionality in Stripe to work.
- [Bootstrap](http://getbootstrap.com/), a front-end framework
  - for general responsiveness.
  - for inegral components such as navbar and mobile friendly pages. 

## Testing

Automated testing has been written for the models within the issues and checkout app. Testing has been performed and passed. 

All other testing has been performed manually. This includes the following manual tests:

### Log in and out

1. When logged out the visitor to the site should only see "register" and "login" in the Navbar. Manual tests confirm this.
1. Only registered users should be able to log in and an error message will be displayed if a non-registered user tries to log in. Manual tests confirm this.
1. When a registered user logs in the navbar options should change to display "add issue", "profile", "logout" and "cart". Manual tests confirm this.
1. When a registered user logs in the user should be redircted to the index page. Manual tests confirm this.

### Navbar

1. Navbar links have been created for ease of navigation. All navigation links has been manually tested and correct navigation has been confirmed.
1. The search feature is positioned within the navbar. Manual testing has confirmed that the search feature works and users can search for an issue title with success.

### Index / Issues Page

1. The index page should show a list of all submitted issue requests. When clicked each issue will drop down to display details of the issue. Manual tests confirm this.
1. If the user is a superuser an edit button should be displayed so that the superuser can click to edit the issue. if the user is not a superuser the edit button will not display. Manual tests confirm this.
1. Any logged in user should be able to click on the upvote icon to upvote an issue. Manual testing confirms this is working.

### Edit Issue Page

1. For the issue that has been selected for editing, all existing detail for that particular issue from the database should be displayed. Manual testing confirms this.
1. The superuser should be able to change all existing detail. This includes changing the status of an issue from 'not started' to 'in progress' and 'complete'. Manual testing confirms this.
1. Once the submit button is clicked the issue should be updated in the database and display this updated detail in the index / issue page. Manual testing confirms this.

### Add Issue Page

1. The user should be able to enter details of the new issue request into the fields provided. The user should be able to select either add a Bug or a Feature from the dropdown provided. Manual testing confirms this.
1. If the user selects a Bug issue, once they click submit they should be redirected to the index / issue page where the bug should be visible in the list of all bugs. Manual testing confirms this.
1. If the user selects a Feature issue, once they click submit they should be redirected to the cart page. Manual testing confirms this. 

### Cart Page

1. The cart icon in the navbar should display a '1' after a Feature request has been submitted. This should display in all pages of the website during a user session. Manual testing confirms this. 
1. The cart page should display detail of the Feature issue that has been requested. This includes the issue title, description, requested by and price (£99.99). A button for removing the Feature request from the cart, the total cart value and a button the go to the checkout page should be displayed. Manual testing confirms this.
1. If the remove button is clicked, the Feature request should be removed from the cart. The cart icon in the navbar should no longer display '1'. Manual testing confirms this. 
1. If the checkout button is clicked the user should be redircted to the checkout page. Manual testing confirms this.

### Checkout Page

1. The checkout page should display detail of the Feature issue that is to be purchased. This includes the issue title, description, requested by and price (£99.99). Manual testing confirms this. 
1. The checkout page should display fields to take payment details. The user should be able to enter their details into these fields and click on 'submit payment' to purchase the Feature issue request. Manual testing confirms this. 

### Profile Page

1. The profile page should display the users username and email address. Manual testing confirms this.

### Visual Checks

1. The app has been manually tested for various different screen sizes, including mobile displays. This has confirmed that the webiste is responsive to different screen sizes.

## Deployment

This app is hosted on Heroku. To be able to run the code on Heroku, a Procfile was added to tell Heroku it's a Python project (web: python app.py), as were the Config vars for IP (0.0.0.0) and PORT (5000).

## Credits

Jonathan Walters - This project was completed as part of Code Institute’s Diploma in Full Stack Web Development course in 2019.