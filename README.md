# CSSNN Technology News Site

## Introduction
For my fourth milestone project, I chose to build a reddit style news site, as recommended by the portfolio preparation module and using the "I think therefore I blog" module as a basic skeleton. 

A live website can be found [here]().


# Table of Contents

-   [1. UX](#ux)
    -   [1.1. Strategy](#strategy)
        -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [Trends of Modern Websites](#trends-of-modern-websites)
            -   [Strategy Table](#strategy-table)
    -   [1.2. Structure](#structure)
    -   [1.3. Skeleton](#skeleton)
-   [2. Features](#features)
-   [3. Technologies Used](#technologies-used)
-   [4. Testing](#testing)
-   [5. Deployment](#deployment)
-   [7. Bugs](#bugs)
-   [8. Credits](#credits)

<a name="ux"></a>

# 1. UX

[Go to the top](#table-of-contents)
As a somewhat frequent user of forum style webpages i felt the need to try and explore this kind of webpage and how to build one.
<a name="strategy"></a>

## 1.1. Strategy

### Project Goals

The goal of this website is for users to be able to create posts and upload them which in turn makes a forum for users to discuss certain topics and collaborate with each other.

### User Stories:
#### All Site Users: 
- As a site user, I want to be able to view an ordered list of existing posts. 
- As a site user, I want to be able to click on a specific post to read that post in its entirety. 
- As a site user, I want to be able to view existing comments so I can view the conversation about a speficic post. 
- As an unregistered user, I want to be able to register an account with the site. 
- As a site user, I can filter posts through categories.
#### Registered User:
- As a registered user who isn't signed in, I want to be able to sign in. 
- As a registered user who is signed in, I want to be able to sign out.
- As a registered user, I can view the number of likes on each post so that I can see which is the most popular 
- As a registered user, I want to be able to create my own news post and upload it to the site. 
- As a registered user, I want to be able to add a comment and submit it to contribute to the discussion of a particular post.
#### Frequent User
- As a frequent user, I want to be able to see a newly updated and ordered post list.  

### User Expectations:
The user should be able to navigate the site efficiently, without any bugs or styling choices that present visual confusion or inconvenience.  The site should also be completely responsive across all standard device sizes. 

### Project Management
I used GitHub projects and specifically the projects board to manage existing issues and user stories. When I was ready to work on a user story, I would move it to the in progress section from the todo section. When complete, I would move it to the done section. 


## Scope
Following agile principles, this deployed initial version offers all core of the base functionality the site can provide, and some additional pieces.  However, there are several features, some covered above, which could possibly be added to the site in the future to improve functionality. These are discussed later in the features section. Below is a short description of the current site functionality. 

### Current Functionality
- Display Welcome Page
- View Existing Post List and Comments
- Register an Account
- Create a New Post
- Add a New Comment to a Post
- Delete Existing Post (as author)
- Edit Existing Post (as author)
- Responsivity
- Admin control

<a name="structure"></a>

## 1.2. Structure

[Go to the top](#table-of-contents)

<a name="skeleton"></a>

## 1.3. Skeleton

[Go to the top](#table-of-contents)


# 2. Features

[Go to the top](#table-of-contents)

-   A simple navigation bar for users to navigate easily

-   A row of blog posts made by users

-   A sign up form to be able to sign in and post

-   A comment section to either read or comment on posts

-   Social media links in the footer



## Features to be added

-   Change password, profile picture, bio

-   Approve posts before publishing 

-   Edit posts

-   Delete posts

## 3. Technologies Used

[Go to the top](#table-of-contents)

-   [HTML5](https://en.wikipedia.org/wiki/HTML)
    -   The project used HyperText Markup Language.
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
    -   The project used Cascading Style Sheets.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    -   The project used JavaScript.
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    -   The project used Python.
-   [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    -   The project used Bootstrap 5.
-   [PostgreSQL](https://www.postgresql.org/)
    -   The project used PostgreSQL as a database.
-   [Gitpod](https://www.gitpod.io/)
    -   The project used Gitpod and Gitpod projects.
-   [Chrome](https://www.google.com/intl/en_uk/chrome/)
    -   The project used Chrome to debug and test.
-   [Balsamiq](https://balsamiq.com/)
    -   The project used Balsamiq was used to create the wireframes.
-   [GitHub](https://github.com/)
    -   The project pushed all code through GitHub.
-   [Heroku](https://dashboard.heroku.com/)
    - Heroku was used to deploy the final product.
-   [Cloudinary](https://cloudinary.com/)
    - Cloudinary was used to store image assets for the project.

<a name="testing"></a>

# 4. Testing

[Go to the top](#table-of-contents)

Due to lack of time and brutal vomiting near the end product i was not able to test it properly.

## Manual Testing
I have tested my site on Safari and google chrome, which are the mediums available to me at this time. 


### Navigation Bar


# 5. Deployment

[Go to the top](#table-of-contents)

I used the terminal to deploy my project locally. To do this I had to:
1. Create a repository on GitHub
2. Open the bash terminal within GitPod
3. Enter "python3 manage.py runserver" into the terminal
4. Open the local host port on my web browser

For the final deployment to Heroku, I had to:
1. Set debug = False in my settings.py file.
2. Commit and push all files to GitHub
3. In the deploy tab, go to the manual deploy sections and click deploy branch.


<a name="bugs"></a>

# 7. Bugs

[Go to the top](#table-of-contents)

Due to lack of testing i found no bugs

<a name="credits"></a>

# 8. Credits

[Go to the top](#table-of-contents)

I used the "I Think Therefore I Blog" module as an effective skeleton for my site.  As such, several base pieces still resemble the code covered in that video.  

-   settings.py, admin.py, apps.py, models.py, views.py, manage.py, env.py, urls.py, base.html, post_detail.html, post_list.html, and requirements.txt skeleton and boilerplate django code from https://learn.codeinstitute.net/
-   Instances of pagination code taken from https://learn.codeinstitute.net/
-   Inspiration for a form based approach to making new posts and editing existing posts taken from samagosti7 on github
-   README skeleton copied from a samagosti7 on github.

