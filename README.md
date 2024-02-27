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
     - [Desktop and Mobile](#desktop-and-mobile)
    - [Database Design](#database-design)
   - [The Surface Plane](#the-surface-plane)
    - [Design/ Colour-Scheme/ Font/ Images](#design-colour-scheme-font-images)
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

- **3 - User Interface Design (UX/UI):**
The website to be user-friendly and responsive on all devices, this milestone covers the styling aspects of the site, from website pagination to responsiveness and error pages so that user has smooth experience throughout the application.

- **4 - Admin Functionality:** 
Includes admin dashboard functionality so that admin can monitor the website for users, recipes and comments. This milestone was included to keep the admin and site user functionality separate for clarity. 
- **5 - Recipe Post Functions:**
All the CRUD functionality and features related to recipes (comments, likes) is included here.
- **6 - Project Documentation:**
This milestone was needed so that I can document my project in-depth with all website features, testing, deployment information.
- **7 - Final Project Deployment:**
Included as it was absolutely necessary and important to have a live link of fully functional website with no errors so that everyone can have access to the application.



#### User Stories













