# Tasty Tales

Tasty Tales is a full stack web application that gives user a platform to view and share their recipes. The intention of the website is to provide a simple, intuitive, visually appealing and user-friendly platform where users can find recipes shared by food-loving people from around the globe, share their recipes and interact with the community. The intended target audience is anyone with an interest in cooking and exploring world cuisines. The target audience will be mostly span across men and women from young adults to older generations.

- The interactive application implements user authorisation and full CRUD functionality allowing users to create, update, read and delete recipes stored in a relational database management system. Users can also search recipes, like recipes and interact with other users via comments.
- The Tasty Tales website also features a back-end admin dashborad that allows an administrator to review and approve user comments, as well as monitor and edit recipes.

- The website is built using HTML, CSS, JavaScript, Python and the Django framework as a Portfolio Project#4 for the Code Institute's Full Stack Software Development Course.

            Website Image goes here


## The live website link goes here

------

## Table of Contents

 - [Tasty Tales](#tasty-tales)
   - [Table of Contents](#table-of-contents)
 - [User Experience Design](#user-experience-design)
   - [The Strategy Plane](#the-strategy-plane)
    - [Site Goals](#site-goals)
    - [Agile planning](#agile-planning)
      - [Milestones](#milestones)
      - [User Stories](#user-stories)
   - [The Structure Plane](#the-structure-plane)
      - [Features](#features)
      - [Features Left to Implement](#features-left-to-implement)
   - [The Skeleton Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
      - [Desktop Wireframes](#desktop-wireframes)
      - [Mobile Wireframes](#mobile-wireframes)
    - [Database Design](#database-design)
   - [The Surface Plane](#the-surface-plane)
    - [Design](#design)
 - [Technologies](#technologies)
   - [Tools and Technologies](#tools-and-technologies)
   - [Imports](#imports)
    - [Python Packages](#internal-packages)
    - [External Packages](#external-packages)
 - [Testing](#testing)
  - [Responsiveness](#responsiveness)
  - [Accessibility](#accessibility)
  - [Lighthouse](#lighthouse)
  - [Validator Testing](#validator-testing)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
  - [Manual Testing](#manual-testing)
    - [Functional testing](#functional-testing)
    - [Links and Buttons](#links-and-buttons)
    - [Negative Testing](#neagtive-testing)
  - [Automated Testing](#automated-testing)
    - [Unit Tests](#unit-tests)
 - [Bugs](#bugs)
 - [Deployment](#deployment)
   - [Version Control](#version-control)
   - [Deployment Using Heroku](#deployment-using-heroku)
   - [Cloning the Repository](#cloning-the-repository)
   - [Forking](#forking)
 - [Credits](#credits)


# User Experience Design

## The Strategy Plane

### Site Goals

The website is aimed for everyone who loves cooking and exploring cuisines from all around the globe. The site also aims at people who are simply searching for an inspiration on days when they simply want to try something new and discover a diverse recipes. The application aims to provide a vibrant and engaging platform for food enthusiasts to explore, share and indulge in culinary delights. Through a user-friendly interface, users can discover a diverse range of recipes tailored to their tastes and love for a variety of cuisines. 
- The site allows users to share their favourite recipes, exchange cooking tips and connect with food-loving like-minded individuals. 
- With a visually appealing, clean and earthy design, the site inspires and delights users, whether they are browsing on a desktop or a mobile device.


### Agile Planning

I employed the Agile methodology and utilized a GitHub project board to organize and develop my user stories starting from the project planning stage and continuing until the final product was built. To enhance clarity and structure, a user story template is designed that precisely outlines each user story with an acceptance criteria to be fulfilled. Small features have been assigned to 7 milestones.

- All User Stories include:
   - Acceptance Criteria
   - Labels (MoSCoW Prioritization)
- Labels have been used to mark which features the project : 'must have', 'should have', 'could have' and 'nice to have'. The prioritization was done so that a MVP for the project is created in time I have and only focus on the 'should haves' or 'could haves' if the time allows.
- Each User story was checked for the acceptance criteria have been met and closed.

- The detailed Project Board with all user stories can be found here. [PROJECT BOARD-link](https://github.com/gayatrig19/tasty-tales-website-pp4/projects?query=is%3Aopen)


<details><summary>Issues Template</summary>


![issue template](documentation/docs_images/issue_template.png)

</details>


<details><summary>Issues List</summary>


![issues](documentation/docs_images/issues_list.png)

</details>


<details><summary>Project Board</summary>


![project board](documentation/docs_images/project_board.png)

</details>


#### Milestones

- **1 - Initial Project Setup:**
  The first task in starting the project was to setup it up. All the tasks from setting up github repository to installing django, setting up django app and related packages and libraries were included in this milestone. The acceptance criteria was refined for each of the setup to be completed for clarity and ease of understanding. 

- **2 - User Authentication:**
This milestone covers user authentication and authorization i.e. user sign-up, sign-in and logout so that user can explore complete features and functionality of the website.

- **3 - Recipe Post Functions:**
All the CRUD functionality and features related to recipes (comments, likes) is included here.

- **4 - User Interface Design (UX/UI):**
The website to be user-friendly and responsive on all devices, this milestone covers the styling aspects of the site, from website pagination to responsiveness and error pages so that user has smooth experience throughout the application.

- **5 - Admin Functionality:** 
Includes admin dashboard functionality so that admin can monitor the website for users, recipes and comments. This milestone was included to keep the admin and site user functionality separate for clarity. 

- **6 - Project Documentation:**
This milestone was needed so that I can document my project in-depth with all website features, testing, deployment information.
- **7 - Final Project Deployment:**
Included as it was absolutely necessary and important to have a live link of fully functional website with no errors so that everyone can have access to the application.


#### User Stories

Each Milestone covers the user stories for small features allowing me to prioritize the most important ones to least in project development.

- **Milestone 1 - Initial Project Setup:**
    - As a developer, I need to set up the recipe blog project with all the necessary components and configurations so that I can ensure a smooth development and deployment process.
       - Initialize and setup a GitHub repository with a README file using CI Gitpod template.
       - Install the latest version of Django.
       - Create a new Django project.
       - Add main app.
       - Verify that the project runs without errors using the Django development server.
       - Add a requirements.txt file listing all project dependencies.
       - Add env.py file to store sensitive information.
       - Add Procfile
       - Implement a proper media storage configuration for user-uploaded images.
            - image database: Cloudinary
       - Configure the project to use a ElephantSQL database.
       - Update the settings.py file to notify Django of the installed supporting libraries .
       - Deploy project to Heroku to test deployment is successful.

    - As a developer, I need to create a base.html file so that I can have a basic structure of the page for the project.
    - As a developer, I need to add static files and media so that I can build the website to be user friendly, interesting and responsive to all screen sizes.
    - As a developer, I need to create a navigation menu so that a website user can easily navigate through the site pages and content.
       - Home Page - for all users
       - Browse Recipes Page - for all users
       - Signup Page - for unauthorised user's registration
       - Login Page - for users already registered
       - Logout Page - for authorised users
       - User Drafts Recipe Page - for authorised users
       - Create new recipes Page - for authorised users
    - As a developer, I need to create a footer so that I can include social media links, contact links and relevant site information about the website.

- **Milestone 2 - User Authentication:**
    - As a developer, I need to setup allauth so that users can have an option to register and sign-in to the website for exploring more features.
      - Install allauth
      - Implement register, login and logout functionality
      - Verify that users can register/ login and logout of their account with an appropriate message displayed.
    - As a Site User I can register an account so that I can access publishing, commenting and like/unlike features.

- **Milestone 3 - Recipe Post Functions:**
   - As a logged-in User, I can create/publish recipes so that I can share recipes that I find delicious with others.
   - As a logged-in User, I can edit the recipes that I have shared so that I can correct and update the recipe details if necessary.
   - As a logged-in User, I can delete my recipes so that they are no longer published on the site.
   - As a Site User, I can view and read the detailed recipes shared/published by others so that I can get some inspiration.
   - As a Site User, I can view a paginated list of recipe posts so that I can select which recipes I want to view.
   - As a logged-in User, I can go to a page to view only my recipes so that I can easily access them if needed.
   - As a Site User, I can search recipes so that I can only view recipes I am interested in.
   - As a Site User, I can leave comments on recipes so that I can interact with others/share my opinion.
   - As a Site User, I can view comments on an individual recipe post so that I can read the conversation.
   - As a logged-in User, I can like/unlike others' recipes so that I can interact with the content.

- **Milestone 4 - User Interface Design (UX/UI):**
    - As a developer, I need to create a home page so that the user can quickly understand what the recipe blog offers and navigate easily to find interesting recipes.
    - As a User, I can navigate between pages easily, so that I can explore the website content without any chaos.
    - As a developer, I want to style the allauth authentication pages(signup, login and logout pages) so that they are visually consistent with the rest of the website and provide a seamless user experience.
    - As a Site User, I can get corresponding feedback after taking an action so that I know whether my actions were successfully run or not.
    - As a User, I want to be directed to a 403 error page when attempting to access content or functionality that I am not authorized to view, so that I am aware of my access limitations and can take appropriate action.
    - As a User, I want to be directed to a custom 404 page when I navigate to a broken link or URL that does not exist, so that I am informed that the page I am looking for is not available and can be directed to other relevant sections of the website.
    - As a user, I am notified in case of an internal error so that I can understand what went wrong and how to proceed.

- **Milestone 5 - Admin Functionality:** 
   - As a developer, I need to create a superuser so that I can manage the website efficiently and ensure the quality and organization of content on the website.
   - As a Site Admin I can create, read, update and delete recipe posts so that I can manage my recipe blog content.
   - As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.

- **Milestone 6 - Project Documentation:**
   - As a developer, I need to create readme.md file so that the project is documented in detail.

- **Milestone 7 - Final Project Deployment:**
   - As a developer, I need to make sure the project is deployed to heroku so that everything works and looks as expected.


## The Structure Plane

### Features

### Existing Features

#### Navigation Menu

- As a developer, I need to create a navigation menu so that a website user can easily navigate through the site pages and content. **(User Story#4) (must have)**
- As a User, I can navigate between pages easily, so that I can explore the website content without any chaos. **(User Story#22) (should have)**

##### Navigation bar for all users (desktop/mobile)
![navigation-bar-view-desktop](documentation/docs_images/nav-bar-unauthorised-desktop.png)

![navigation-bar-view-mobile](documentation/docs_images/nav-bar-unauthorised-mobile.png)

##### Navigation bar for only authorised users (desktop/mobile)
![navigation-bar-view-authorised-desktop](documentation/docs_images/nav-bar-authorised-desktop.png)

![navigation-bar-view-authorised-mobile](documentation/docs_images/nav-bar-authorised-mobile.png)

- The navigation bar is shown on all pages based on the users logged-in(authentication) status and is responsive to all screen sizes. For smaller screen sizes the navigation bar appears as a hamburger menu and can be easily accessed. A success message is displayed when user is logged-in/ registered.
- The design is kept clean and simple so that user can navigate between the pages easily without any confusion. The links are visible clearly both on large screen and smaller screen sizes. 
- The active link is marked for ease of accessibility so that the user knows the current page been visited.
- The navigation menu includes:
    - Home Page - for all users
    - Recipes Page - for all users
    - Search Recipes Page - for all users
    - Sign up Page - for unauthorised user's registration
    - Sign in Page - for users already registered
    - Logout Page - for authorised users
    - Add Recipe Page - for authorised users
    - My Drafts Page - for authorised users
  

#### Home Page

- As a developer, I need to create a home page so that the user can quickly understand what the recipe blog offers and navigate easily to find interesting recipes. **(User Story#21) (must have)**

##### Home Page for all users
![home-page-view-unauthorised-users](documentation/docs_images/home-page-view-unauthorised.png)

##### Home Page for authorised users
![home-page-view-authorised-users](documentation/docs_images/home-page-view-authorised.png)

- The home page is designed such that it is inviting and conveys the user a clear message about the website and what the user can expect throughout the site journey. The background image showcases the essence of the recipe website. User is encouraged to sign up and explore through a quick, simple introduction about the recipe application.


#### Footer

- As a developer, I need to create a footer so that I can include social media links, contact links and relevant site information about the website. **(User Story#5) (must have)**

![footer-section-view](documentation/docs_images/footer-page-view.png)

- The footer section includes the information about the website: the developer of the website, the purpose (for educational purpose only), year developed and the developer's GitHub and LinkedIn links.
- Similar to the navigation bar, the footer is displayed on every page of the website. It displays icon links to GitHub and LinkedIn accounts. These icon links can enable user to see more about my work through GitHub and learn more about me through LinkedIn. Both the links opens in new page.


#### Sign-Up / Sign-In / Logout Pages

- As a developer, I need to setup allauth so that users can have an option to register and sign-in to the website for exploring more features. **(User Story#6) (must have)**

- As a Site User I can register an account so that I can access publishing, commenting and like/unlike features. **(User Story#7) (must have)**

- As a developer, I want to style the allauth authentication pages(signup, login and logout pages) so that they are visually consistent with the rest of the website and provide a seamless user experience. **(User Story#23) (should have)**

![sign-up-page-view](documentation/docs_images/sign-up-page-view.png)

![sign-in-page-view](documentation/docs_images/sign-in-page-view.png)

![sign-out-page-view](documentation/docs_images/sign-out-page-view.png)

- All the pages are accessible from navigation bar for large and small screen sizes.
- User can easily access the sign-up / sign-in options to explore the website features completely.
- A clear message is displayed on the pages for user to know whether he needs to sign-in or sign-up to explore the recipe website and to like, comment and post the recipes.
- A success message is displayed to user based on his actions for sign-in, sign-up and sign-out.


#### Add Recipe Page

- As a logged-in User, I can create/publish recipes so that I can share recipes that I find delicious with others. **(User Story#8) (must have)**

![add-recipe-page-view](documentation/docs_images/add-recipe-page-view.png)

- CRUD Functionality - The Add Recipe page link is only visible and accessible to logged-in users. On clicking the Add Recipe link, authorised users are directed to the create recipe form. The form field marked as * are mandatory to be filled. If user tries to submit the form without entering all required field, messages are displayed below relevant fields that are left empty.
- A default image is incorporated so that if the user is unable to provide any recipe image, the default image will act as one.
- All the fields in the form except the Recipe Image field are required. The form is not deemed to be valid in case any of the fields are left empty. User can either publish or save recipe as draft. 
- Users can share their recipes with others using the add recipe form. On submitting the recipe, user is displayed with a success message and directed to the Recipes page.

#### Edit Recipe
- As a logged-in User, I can edit the recipes that I have shared so that I can correct and update the recipe details if necessary. **(User Story#9) (must have)**

![edit-recipe-button](documentation/docs_images/edit-button-view.png)

![edit-recipe-page-view](documentation/docs_images/edit-recipe-page-view.png)

- CRUD Functionality - the feature of edit in recipe details page is only visible and accessible to the logged-in users and only if the user is the author of the recipe.
- On clicking the edit button user is directed to the Edit recipe form/page where user can update / edit recipe for any changes and can either save as draft or publish it. On successful update of the recipe, user is displayed with success message and directed to Recipes Page.
- If anauthorised user accesses the link the 403 error page will be displayed.


#### Delete Recipe

- As a logged-in User, I can delete my recipes so that they are no longer published on the site. **(User Story#10) (must have)**

![delete-button-view](documentation/docs_images/delete-button-view.png)

![delete-recipe-page-view](documentation/docs_images/delete-recipe-page-view.png)


- CRUD Functionality - the feature of delete in recipe details page is only visible and accessible to the logged-in users and only if the user is the author of the recipe.
- User is directed to confirm delete page where user can either delete the recipe or cancel. 
- The recipe is permanently deleted if delete is confirmed and a success message is diplayed to user else user will be taken back to recipe details page if cancelled.
- If anauthorised user accesses the link the 403 error page will be displayed.


#### Recipe Details
- As a Site User, I can view and read the detailed recipes shared/published by others so that I can get some inspiration. **(User Story#11) (must have)**

##### Recipe Details View for Unauthorised Users
![recipe-details-page-view](documentation/docs_images/recipe-details-view.png)

##### Recipe Details View for Logged-in Users
![recipe-details-page-view-authorised-users](documentation/docs_images/recipe-details-recipe-author.png)

##### Recipe Details View for Logged-in User and author of the recipe
![recipe-details-page-view-recipe-author](documentation/docs_images/recipe-details-view-user.png)

- User can view a detailed recipe on this page along with number of comments, number of likes and the all recipe information.
- The edit and delete buttons are visible and accessible only to the logged-in user as author of the recipe.
- Logged-in users can explore the recipe details page completely for like / unlike and comments feature.
- If user is not logged-in, information is displayed below recipe for sign-in along with the comments from other users in the comment section.


#### Recipe Pagination (Recipes Page)

- As a Site User, I can view a paginated list of recipe posts so that I can select which recipes I want to view. **(User Story#12) (should have)**

![recipe-page-list-view](documentation/docs_images/recipe-page-lists-view.png)

![recipe-page-next-button](documentation/docs_images/recipe-pagination-next-page.png)

![recipe-page-prev-button](documentation/docs_images/recipation-pagination-prev-page.png)

- This feature allows recipes to be paginated by 6 recipes per page, given more than 2 pages the next and prev buttons appear adjacent to each other.
- The recipe list page is kept simple so that it is not overcrowded and user can find it easy to navigate between the pages.
- On clicking the View Recipe button user is taken to recipe details page to view complete recipe information.


#### My Drafts Page

- As a logged-in User, I can go to a page to view only my recipes so that I can easily access them if needed.
**(User Story#13) (should have)**

- **Note:** The user story is partially complete. User can only view the recipes saved as draft in my drafts page for now. User can update the draft recipe from my drafts page to either publish or save it for later. 
- This page is only accessible and visible to logged-in users.
- The paginated list of recipe drafts is displayed with 6 recipes per page (if present). With this feature user can create recipe and save for later as draft for changes or to publish later.
- User can also make his published recipes draft for any changes. This feature allows a flexibility for user to share recipes and manage them.

![my-drafts-recipe-view](documentation/docs_images/my-drafts-page-view.png)


#### Search Recipes Page

- As a Site User, I can search recipes so that I can only view recipes I am interested in. **(User Story#14) (could have)**

![search-recipes-page-view](documentation/docs_images/search-recipes-page-view.png)

![search-results-page-view](documentation/docs_images/search-results-page-view.png)

![search-not-found-page-view](documentation/docs_images/search-not-found-page-view.png)

- The search recipes page allows users to search recipes by title, keyword and cuisines. This page is accessible throughout the website and to all users.
- If the user search results are not found, a message for refining search is provided. Also user is encouraged to share own recipes or view all recipes.
- If search query is not provided by user, the page is loaded with message to search bu recipe title, keyword and cuisines.


#### Comment Section

- As a Site User, I can leave comments on recipes so that I can interact with others/share my opinion. **(User Story#15) (should have)**

- As a Site User, I can view comments on an individual recipe post so that I can read the conversation. **(User Story#16) (should have)**

##### Comments Section for unauthorised Users
![comment-view-unauthorised-user](documentation/docs_images/comments-section-unauthorised.png)

##### Comments Section for unauthorised Users
![comment-view-authorised-user](documentation/docs_images/comments-section-authorised.png)

![total-number-of-comments-view](documentation/docs_images/total-comments-view.png)

- This feature allows user to comment on recipes posted by others.
- If the user is not logged-in, user will only be displayed with the comments made by others on the recipes and a message to login to comment and like the recipe with sign-in link. When user is logged-in with the link, he is taken back to same recipe to add comment. 
- Authorised users are displayed with the comment box to comment on the recipe, upon comment submission a success message is displayed with a comment awaiting approval information.
- The comments from other users on the recipe and total number of comments on the recipe is visible to all users regardless of their login status.
- If recipe has no comments, then a short messsage 'No comments yet' will be displayed.


#### Like / Unlike Recipes

- As a logged-in User, I can like/unlike others' recipes so that I can interact with the content. **(User Story#17) (should have)**

![liked-recipe-view](documentation/docs_images/liked-recipe-view.png)
![unliked-recipe-view](documentation/docs_images/unliked-recipe-view.png)

- The like / unlike feature allows logged-in user to like or unlike the recipes.
- If unauthorised user clicks the hollow heart icon, no action / effect will be seen on the icon. A simple message is diplayed for user below the recipe details to know that they needs to be logged-in to comment or like the recipe.
- Authorised user - likes the recipes (if didn't previously liked the recipe), hollow heart icon will be displayed - if clicked the icon will change to solid red color and the number of likes will increase by one.
- Authorised user - unlikes the recipe (if previously liked the recipe) , the solid red heart icon will be shown - if clicked the icon will chnage to hollow ones and the number of likes will be decreased by one.


#### Admin Functionality

- As a developer, I need to create a superuser so that I can manage the website efficiently and ensure the quality and organization of content on the website. **(User Story#24) (must have)**
- As a Site Admin I can create, read, update and delete recipe posts so that I can manage my recipe blog content. **(User Story#25) (must have)**
- As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments. **(User Story#26) (must have)**

![admin-functionality-view](documentation/docs_images/admin-functions-view.png)

- The most important task for website to function was to create a superuser, to manage the recipe post functionality and the website entirely.
- The admin can ensure the quality and organization of the content on the webite.
- When the comment is made by any user on the recipe, the comment awaiting approval message is displayed to user. The comment is only displayed if it approved by admin.
- The admin panel helps the administrator to have control over the website to function seamlessely and keep the website content meaningful and organized.


#### Feedback on user actions

- As a Site User, I can get corresponding feedback after taking an action so that I know whether my actions were successfully run or not. **(User Story#18) (must have)**

![user-signin-success-message](documentation/docs_images/user-signin-message.png)

![user-signout-success-message](documentation/docs_images/user-signout-message.png)

- This feature informs the user if the action taken has been successful so that user can know the outcome of every action throughout while navigating the website.
- Message will be displayed when :
    - User Sign In / Sign Up / Logout
    - User posted a recipe
    - User edited the recipe
    - User deleted the recipe
    - User comments on a recipe


#### Initial Project Setup / Project Documentation / Final Project Deployment
All the user stories are completed for project setup, project documentation and final project deployment

- As a developer, I need to set up the recipe blog project with all the necessary components and 
  configurations so that I can ensure a smooth development and deployment process. **(User Story#1) (must have)**
    - Initialize and setup a GitHub repository with a README file using CI Gitpod template.
    - Install the latest version of Django.
    - Create a new Django project.
    - Add main app.
    - Verify that the project runs without errors using the Django development server.
    - Add a requirements.txt file listing all project dependencies.
    - Add env.py file to store sensitive information.
    - Add Procfile
    - Implement a proper media storage configuration for user-uploaded images.
            - image database: Cloudinary
    - Configure the project to use a ElephantSQL database.
    - Update the settings.py file to notify Django of the installed supporting libraries .
    - Deploy project to Heroku to test deployment is successful.

- As a developer, I need to create a base.html file so that I can have a basic structure of the page for the project. **(User Story#2) (must have)**
- As a developer, I need to add static files and media so that I can build the website to be user friendly, interesting and responsive to all screen sizes. **(User Story#3) (must have)**
- As a developer, I need to create readme.md file so that the project is documented in detail. **(User Story#19) (must have)**
- As a developer, I need to make sure the project is deployed to heroku so that everything works and looks as expected. **(User Story#20) (must have)**


    








### Features left to implement




## The Skeleton Plane

### Wireframes

#### Desktop Wireframes
Wireframes for Large Screen Sizes 

Update: The Search Recipes Button is changed later in design, it is included along with the other navbar menus and is accessible to all users. It is just kept as a nav link instead of button for both desktop and mobile devices.

#### Home Page (authorised / unauthorised users)
     
![home-page-authorised-users-desktop-wireframe](documentation/docs_images/home-page-authorised-users-wireframe-desktop.png)

![home-page-unauthorised-users-desktop-wireframe](documentation/docs_images/home-page-unauthorised-users-wireframe-desktop.png)


#### Recipes Page
The recipes page is accessible to all users.

![recipe-page-wireframe-desktop](documentation/docs_images/recipe-page-wireframe-desktop.png)


#### Recipe Details Page (authorised / unauthorised users)

![recipe-details-page-authorised-wireframe-desktop](documentation/docs_images/recipe-details-authorised-wireframe-desktop.png)

![recipe-details-page-unauthorised-wireframe-desktop](documentation/docs_images/recipe-details-unauthorised-wireframe-desktop.png)


#### My Drafts Page (for authorised users only)

![my-drafts-page-wireframe-desktop](documentation/docs_images/draft-recipes-page-wireframe-desktop.png)


#### Search Recipes Page 
Search Recipes page is accessible to all users.

![search-recipes-page-wireframe-desktop](documentation/docs_images/search-recipe-wireframe-desktop.png)


#### Add Recipe Page (for authorised users only)

![add-recipe-page-wireframe-desktop](documentation/docs_images/add-recipe-wireframe-desktop.png)


#### Edit Recipe Page (for authorised users only)

![update-recipe-page-wireframe-desktop](documentation/docs_images/update-recipe-wireframe-desktop.png)


#### Delete Recipe Page (for authorised users only)

![delete-recipe-page-wireframe-desktop](documentation/docs_images/delete-recipe-confirm-wireframe-desktop.png)


#### Sign Up and Sign In Page (for unauthorised users only)

![sign-up-page-wireframe-desktop](documentation/docs_images/sign-up-wireframe-desktop.png)

![sign-in-page-wireframe-desktop](documentation/docs_images/sign-in-wireframe-desktop.png)


#### Log Out Page (for authorised users only)

![log-out-page-wireframe-desktop](documentation/docs_images/log-out-wireframe-desktop.png)


#### Mobile Wireframes
Wireframes for Small Screen Sizes

#### Home Page (authorised / unauthorised users)
     
![home-page-authorised-users-mobile-wireframe](documentation/docs_images/home-page-authorised-wireframe-mobile.png)

![home-page-unauthorised-users-mobile-wireframe](documentation/docs_images/home-page-unauthorised-wireframe-mobile.png)


#### Recipes Page
The recipes page is accessible to all users.

![recipe-page-wireframe-mobile](documentation/docs_images/recipe-page-wireframe-mobile.png)


#### Recipe Details Page (authorised / unauthorised users)

![recipe-details-page-authorised-wireframe-mobile](documentation/docs_images/recipe-detail-authorised-page-wireframe-mobile.png)

![recipe-details-page-unauthorised-wireframe-mobile](documentation/docs_images/recipe-detail-unauthorised-page-wireframe-mobile.png)


#### My Drafts Page (for authorised users only)

![my-drafts-page-wireframe-mobile](documentation/docs_images/draft-recipe-page-wireframe-mobile.png)


#### Search Recipes Page 
Search Recipes page is accessible to all users.

![search-recipes-page-wireframe-mobile](documentation/docs_images/search-page-wireframe-mobile.png)


#### Add Recipe Page (for authorised users only)

![add-recipe-page-wireframe-mobile](documentation/docs_images/add-recipe-page-wireframe-mobile.png)


#### Sign Up and Sign In Page (for unauthorised users only)

![sign-up-page-wireframe-mobile](documentation/docs_images/sign-up-page-wireframe-mobile.png)

![sign-in-page-wireframe-mobile](documentation/docs_images/sign-in-page-wireframe-mobile.png)


#### Log Out Page (for authorised users only)

![log-out-page-wireframe-mobile](documentation/docs_images/logout-page-wireframe-mobile.png)


### Database Design

![Entity-Relationship-Diagram](documentation/docs_images/entity-relationship-diagram.png)


- The database ER diagram was designed using [SmartDraw](https://www.smartdraw.com/entity-relationship-diagram/). The main Recipe model contains all the fields needed for the recipe to be complete. Additional fields (like category, nutritional value, meals type., etc) can be added to further enhance the website, but the values are not vital for the site to work and can be added later.
- The diagram shows relationaships between the Recipe model, Comments Model and django's allauth User model as follows:
   1. User to Recipe: One-to-Many (1:M)
       - Each user can create multiple recipes.
       - Each recipe is created by one user.
   2. Recipe to Comment: One-to-Many (1:M)
       - Each recipe can have multiple comments.
       - Each comment is associated with one recipe.
   3. User to Comment: One-to-Many (1:M)
       - Each user can make multiple comments.
       - Each comment is made by one user.

- In summary, User can create multiple recipes, and each recipe is associated with one user. Recipe can have multiple comments, and each comment is associated with one recipe. User can make multiple comments, and each comment is made by one user.
- These relationships was implemented using ForeignKey fields in the models. The Recipe model have a ForeignKey field referencing the User model to represent the creator of the recipe, and the Comment model have ForeignKey fields referencing both the Recipe model and the User model to represent the recipe being commented on and the user making the comment, respectively.


## The Surface Plane

### Design

The website uses clean, simple design with earthy colours and images that showcases the primary goal of the website. The aim here was to keep the site clutter-free so that user can have a smooth straight-forward navigation experience throughout without any chaos and confusion.

#### Typography

- [Oswald](https://fonts.google.com/specimen/Oswald?query=oswald) was chosen for logo and headings as it can be combined easily with other fonts. It is attractive and amenable for the heading content on site. Because it is slightly elongated, it brings contrast to a typography combination. With website consideration it was best suited as it gives both modern and a serious touch to the content throughout on pages.

- [Lato](https://fonts.google.com/specimen/Lato?query=Lato) was chosen for body text as it is light and easy to read.


#### Images

- The images in this project are sourced from [Pexels](https://www.pexels.com/), [Unsplash](https://unsplash.com/) and [Pixabay](https://pixabay.com/). They were specifically selected to correlate with the main purpose of the website and to give user a imagery representation for the recipe content to increase impact of the design.


## Technologies

### Tools and Technologies



### Imports

#### Python Packages



#### External Packages


## Testing 

### Responsiveness

- The site is designed to be flexible, fluid and responsive on all screen sizes. Website has been checked for responsiveness through Chrome Development tools. In order to do this, the following steps have been taken:
  1. Open the browser.
  2. Navigate to the Tasty Tales website <https://tasty-tales-4b4d80fd4040.herokuapp.com/>
  3. Right click anywhere on the page and got to "Inspect" to open Development Tools.
  4. Click on drop down menu: "Dimensions: Responsive" and choose "Responsive".
  5. Drag the side of the screen and change screen size, making sure the website looks good from 320px and up. Here, ensure there is consistency in design of the website on every screen size from small(mobile devices) to larger(desktop devices) and no scorll bar is showing for layout of site.

- Expected Result: Each page is responsive and user friendly when viewing the website on small and large screens.The pages have no design or accessibility issue in any of the screen sizes from 320px and up.
- Actual Result: Website is responsive with no scroll bar showing, the content is accessible to user to read and the images are not appearing stretched. Website is user friendly on small to large screen sizes.

- The following devices are used to check responsiveness:
     - Iphone 12 Pro
     - Samsung Galaxy S20 Ultra
     - iPad Mini
     - Surface Pro 7
- The website was also tested further by sharing the live link with friends and family. The site was tested on following devices:
     - Samsung S20 FE 5G
     - Iphone 12 
     - iPad Air
     - Samsung S24 Ultra
     - Microsoft Surface
     - Asus X5 50
     - Lenovo Pad Pro 12.7

- The following browsers have been used to check responsiveness. Testing for different browsers was carried on using [BrowserStack](https://www.browserstack.com/) and manually on some of the browsers.
     - Chrome
     - Safari
     - Microsoft Edge
     - Firefox
     - Internet Explorer


### Accessibility


### Lighthouse



## Validator Testing

### HTML Validation

All pages have been run through the [W3C VALIDATOR](https://validator.w3.org/).

In order to check HTML code in dynamic website:

- go to the live page
- click right and select 'Inspect' then click right and select 'View page source'
- code will open in new tab - copy the code
- paste the code in the validator as 'direct input'

#### Home Page
![home-page-html-validation](documentation/docs_images/home-page-html-validation.png)

#### Recipes Page
![recipes-page-html-validation](documentation/docs_images/recipes-page-html-validation.png)

#### Recipe Details Page
![recipes-details-page-html-validation](documentation/docs_images/recipe-detail-page-html-validation.png)

#### Search Recipes Page
![search-recipes-page-html-validation](documentation/docs_images/search-recipe-page-html-validation.png)

#### My Drafts Page
![my-drafts-page-html-validation](documentation/docs_images/my-drafts-page-html-validation.png)

#### Sign In Page
![sign-in-page-html-validation](documentation/docs_images/sign-in-page-html-validation.png)


#### Logout Page
![logout-page-html-validation](documentation/docs_images/logout-page-html-validation.png)

#### Error Pages (403, 500, 404)
![error-page-html-validation](documentation/docs_images/error-pages-html-validation.png)

#### Delete Recipe Page
![delete-recipe-page-html-validation](documentation/docs_images/delete-recipe-page-html-validation.png)

#### Add Recipe Page | Update Recipe Page
All errors listed by W3Validator are related to Summernote, and not any code written by me. Errors are the same for both "Add Recipe" page and "Update Recipe" page. Research conducted within the Code Institute community indicates that this is a common occurrence, and therefore it should be noted. However, no action needs to be taken in response.

<details>

  <summary>Click here to see the errors.</summary>
    
![add-recipe-html-validation-error](documentation/docs_images/add-recipe-page-error-html-validation.png)

  </details>

#### Sign Up Page
 The Sign Up page HTML code is part of the Django authentication form, and I could find no way to change it. 
 The html errors are coming from Django forms interpretation of allauths helper text, and not any code written by me. So, no action is taken in response.

 <details>

  <summary>Click here to see the errors.</summary>
    
![signup-html-validation-error](documentation/docs_images/sign-up-form-error-html-validation.png)

  </details>


### CSS Validation
No errors were found when passing through the official Jigsaw W3 Validator

![css-validation-check](documentation/docs_images/css-page-validation.png)


### JavaScript Validation
No errors were found when passing through the [jshint validator](https://jshint.com/)

![javascript-validation-check](documentation/docs_images/javascript-code-jshint-validation.png)


### Python Validation
No errors were found when passing each file through [CI Python Linter](https://pep8ci.herokuapp.com/)

![python-validation-check](documentation/docs_images/python-ci-linter-validation.png)

Couple of warnings when running settings.py file. Too long lines of code. Modifying the file for resolving the warnings rendered errors during deployment. I have left the mentioned lines in settings.py file unchanged for warnings. All other python files have passed the validation with no errors.

![settings-python-validate-warnings](documentation/docs_images/settings-python-validation-warnings.png)


## Manual Testing






## Automated Testing

### Unit Testing

No unit testing performed at this stage.