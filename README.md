![Title image](media/readme-images/title.png)

A long time ago in a galaxy far far away, the arma 3 community created the 501st unit. Along with their fellow GARC units, they created a proud community of star wars simulator fans. The Comlink is a place where the clones can converse with each other and share images/videos from their antics. 

<br>

![Screenshot of my website mockup](media/readme-images/Comlink-mockup.png)

Link to deployed site: [Comlink](https://the-comlink-896502f13dfc.herokuapp.com/)
---

## **Contents**
- [AI]
- [Basics](#Basic)
    - [Naming](#naming)
    - [User Stories](#user-stories)
    - [User Stories: Criteria](#user-stories-criteria)
    - [User Stories: Issues](#user-stories-isssues)
- [User Design](#user-design)
    - [Wireframes](#wireframes)
    - [ERD](#erd)
    - [Colour Scheme](#Colour-scheme)
    - [Typography](#Typography)
    - [Imagery](#Imagery)
- [Agile](#)
- [Page Features](#page-features)
    - [Main Content](#main-content)
    - [Footer](#footer)
- [Known Bugs](#known-bugs)
- [Responsivity](#responsivity)
    - [Mobile Layout](#mobile-layout)
    - [Tablet/PC Layout](#tablet-layout)
- [Future Features](#future-features)
    - [Future Changes](#future-changes)
- [Testing](#testing)
    - [Lighthouse Scores](#lighthouse) 
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
- [Deployment](#deployment)
    - [Github](#connecting-to-github)
    - [Django](#django-setup)
    - [Cloudinary](#cloudinary-api)
    - [Heroku](#heroku-deployment)
- [Credits](#credits)

---

## AI use
Please find the use of AI spoken throughout the README. I found I didn't use AI much so the times I did are included int he sections that it links to

## Basics

### Naming
To begin with, I was uncertain what to call this social media site as I wanted it to relate to Star wars and the community. While thinking about quotes from the films i realised that there could only be one name - Comlink. This is the device usedd across the galaxy to communicate to one another and so this fits perfectly with the idea and theme of the service.
### User Stories 
Since creating user stories is a weak point for me, I decided to have Microsoft Copilot help me out.
![User Stories](media/readme-images/user%20stories.png)
### User Stories: Criteria
The majority of the provided user stories fit very well and so I asked Copilot to create the criteria for each.
![User Stories and criteria](media/readme-images/criteria.png)
### User Stories: Isssues
From what Copilot provided me, I tweaked the wording of some of them and then added them to the issues section od GitHub. I created a user story template to do this much faster.
![Github Issues page](media/readme-images/Initital%20issues.png)
Once the issues were made, I added them to my project board and assigned them labels for their priority.

## User Design
Since this site is heavily influenced by Star Wars, I wanted to keep the styling similar to the main colours used for their graphics - this is where the black and yellow come from on the pallete.

### Wireframes
I drew up the wireframes using sketchbook - a drawing app that I use. The layout is simple so that the site can be easy to use. I only drew how the profile page will change on tablet and pc screens as the main feed page will just look the same only bigger.
![Wireframes screenshot](media/readme-images/wireframes.png)


### ERD 
Since I'm still not fully comfortable with the databases and relationships, I asked Copilot to help me with the ERD once i had finished the project:
![Copilot helping with ERD](media/readme-images/ERD-AI-Help.png)

From the information that Copilot gave me I was then able to use [Eraser.io](https://app.eraser.io/all) to create the visual diagram with all the connections - something that helped me understand what I'd build a little better:
![ERD image](media/readme-images/diagram-export-28-01-2025-09_52_48.png)

### Colour Scheme

Since this site is aimed for the 501st unit (which I am a part of) I wanted to include more colours that connect to the unit specifically. For those that know Star Wars, they will know that their colours are blue (on top of the clone trooper white). For those that don't - here is a photo of the 501st Commander, Rex, to show his colours:

![Commander Rex - Star Wars](media/readme-images/commander%20rex.jpg)

and here is a snippet from the offical Star Wars wiki page:
![Screenshot of the Wiki page taking about 501st colours](media/readme-images/color%20pallete%20influence.png)

Using this photo and some research the closest blue I could link was French blue (hex code: #0072BB) and so, combining all the colours together I created this pallete using Coolors.
![Colour Pallete from Coolors](media/readme-images/Comlink%20colour%20pallete.png)

While planning I wasn't 100% certain how many colours I would need and so, keeping on the Star wars theme, I went to get more colours - just in case. (From the future: these colours did come in handy)
![Lightsaber Colours](media/readme-images/lightsaber%20colors.png)

### Typography 
As much as I would have loved to use the Star Wars offical font - I opted to choose an easier to read and more relaxed looking set of fonts. I tried to keep with the galactic theme and so looked for quite robotic and sharp fonts. I settled on:
#### Header: Orbitron
![Orbitron text sample](media/readme-images/font%20choice%20-%20orbitron.png)

#### Body: Montserrat
![Montserrat text sample](media/readme-images/font%20choice%20-%20montserrat.png)

### Images
Since this site it so be used as a type of social media any images used in the main site will be provided by it's users, this inclludes the feed page and the profile page. The only images used on the site is the logo which was made using [Font Meme](https://fontmeme.com/star-wars-font/):

![Font Meme Logo](static/images/logo.webp)

The background image found on [Pintrest](https://uk.pinterest.com/pin/404057397815645775/):
![Background image](static/images/background.webp)

And the placeholder avatar image found [here](https://imgbin.com/png/CfnPwTL4/clone-trooper-star-wars-the-clone-wars-stormtrooper-anakin-skywalker-png)
![Placeholder avatar](static/images/clone-placeholder.webp)

I made sure to convert all the images to Webp [here](https://cloudconvert.com/):
![Webp convert](media/readme-images/webp-convert.png)

## Agile
I am very familiar with Agile development as I used this from an early age, for theis reason its almost second nature to me. For this reason I aimed to complete one page of the site at a time, creating each section as I went along and making sure each was style correctly and responsive so i didnt ahve to go along and do a massive overhaul. This also meant that (due to starting with the feed page) the site could be tested and used while I developed other pages allowing early deployment and use.

### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for Comlink, identifying and labelling my:

- **Must Haves**: the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project early, allowing me to develop the project further than originally planned.
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.
- **Won't Haves**: the features or components that either no longer fit the project's brief or are of very low priority for this release. 

### Kanban Board
Since my project was stored in github I decided to use Githubs project boards for the Kanban board. This is where my user stories and MoSCoW prioritization were used.
You can find the board [here](https://github.com/users/Darthspider360/projects/8)

I also utilized the ability to create issues and sub issues from already created issues meaning I could concentrate on getting the MVP completed when some of the functions in my already designated issues ended up being unneeded for a certain part to function.

## Page Features

### Main Content
The main content of the site will be provided by its users, this will be the feed page. This is how it could look once populated:
![Feed page](media/readme-images/feed-page.png)

A post is created by pressing the button at the top of the page - if you are logged it in will look like this:
![Signed in user's post button](media/readme-images/make-post.png)
And once pressed it will send you to this form view:
![Post form](media/readme-images/Post-form.png)

However, if you arent signed in, the button will appear like this - redirecting you to the sign in or sign up page:
![Signed out user's post button](media/readme-images/post-button-change.png)

#### Comments
As part of the MVP of the project, users need to be able to interact with the posts - creating comments, viewing them, editing and deleting them (CRUD). Comments are found in the "Post view" section of the site, which is when you click on a specific post to go to its page and the comments section will appear underneath the post - also displaying the number of comments:
![Post view](media/readme-images/post-view.png)
Using example comments this is how they are presented for a logged in user:
![Comment section](media/readme-images/comment-section.png)
![Comment icons](media/readme-images/comment-icons.png)
Notice on the comments that there is an "edit" icon and a "delete" icon, these only appear for the comment author and allows them to edit and delete their comment as they wish. 
On viewed comments that arent by the Signed in user, a flag icon will appear - this will be a future feature but for now it is linked to my custom 404 page:
![Custom 404 page](media/readme-images/custom-404.png)

If a user isnt logged in, no icons will appear and the option to leave a comment is locked behind a sign in section:
![Log in to leave a comment](media/readme-images/logged-out-comment-view.png)

#### Profile Page
Another part of the MVP of the project was the profile page, which admittedly took me a while to perfect. While at this stage there isnt an ability for the user to delete their own account(only admins can), users can create, edit and view their own profiles. Here is what that looks like:
![Profile page](media/readme-images/Profile-page.png)

When you press the green pencil (edit button) this will take you to the form to change your profile - this form is the exact same as the profile creation form apart from the fact that the fields are prepopulated with their already existing data:
![Profile create/edit page](media/readme-images/profile-edit.png)

### Signing in/out/up
Since I'm using allauth for my accounts I had to go in and add styling to their provided pages. As you can see, this is where the lightsaber colours came in handy as I could add glow to represent each section of signing in.out/up. This is how they look:
![Sign in page](media/readme-images/sign-in.png)
![Sign out page](media/readme-images/sign-out.png)
![Sign up page](media/readme-images/sign-up.png)

Due to using allauth I have to used Devtools to allow me to find the ID of certain area's of their forms to perfect the styling to match the rest of the site - changing the form field backgrounds from solid white. Amy helped me with learning how to do this.
![Devtools use](media/readme-images/devtools.png)
![Devtools styling use](media/readme-images/devtools-styling.png)
### Footer
While I do have a footer, it only provides minimal information so not to distract from the main page. This is a link to my github page and the copyright of the site.


## Known Bugs
Some knows bugs include:
- Report function not working and goes to 404 (done intentionally)
- Posts can be made that contain nothing - form fields need a check function
- the current avatar name isnt show when changing the avatar
- image posts displayed on profile arent corretcly responsive

## Responsivity 
To make sure that the site was responsive across all devices I built it mobile first as this is most likely where people in a crisis will access the site.

### Mobile Layout
![Mobile layout - feed page](media/readme-images/feed-page-phone.png)
![Mobile layout - profile page](media/readme-images/profile-page-phone.png)

### Tablet/PC Layout
![Tablet/PC layout - feed page](media/readme-images/feed-page-pc-tablet.png)
![Tablet/PC layout - profile page](media/readme-images/profile-page-pc-tablet.png)

## Future Features
Future feature of the site include:
- report comment funtion (currently the flag icon)
- edit, delete, report functions for the posts
- viewing other users accounts
- following users (which will update the numbers on the users profile page)
- ability to upload and view images

### Future Changes
Future changes will include:
- possible reshuffle of user profile page on table/PC 
- making auser only able to post if one of the fields are filled in


## Testing

- For all testing, please refer to the [TESTING.md](TESTING.md) file.


## Deployment

### Connecting to GitHub  

To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the purple CodeAnywhere (if this is your IDE of choice) button to generate a new workspace.

### Django setup
1. Install Django and supporting libraries: 
   
- ```pip3 install 'django<4' gunicorn```
- ```pip3 install dj_database_url psycopg2```
- ```pip3 install dj3-cloudinary-storage```  
  
2. Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the ```pip3 freeze --local > requirements.txt``` command in the terminal.  
3. Create a new Django project in the terminal ```django-admin startproject comlink .```
4. Create a new app eg. ```python3 mangage.py startapp feed```
5. Add this to list of **INSTALLED_APPS** in **settings.py** - 'feed',
6. Create a superuser for the project to allow Admin access and enter credentials: ```python3 manage.py createsuperuser```
7. Migrate the changes with commands: ```python3 manage.py migrate```
8. An **env.py** file must be created to store all protected data such as the **DATABASE_URL** and **SECRET_KEY**. These may be called upon in your project's **settings.py** file along with your Database configurations. The **env.py** file must be added to your **gitignore** file so that your important, protected information is not pushed to public viewing on GitHub. For adding to **env.py**:

- ```import os```
- ```os.environ["DATABASE_URL"]="<copiedURLfromCIemail>"```
- ```os.environ["SECRET_KEY"]="<asupersecretkey>"```
  
For adding to **settings.py**:

- ```import os```
- ```import dj_database_url```
- ```if os.path.exists("env.py"):```
- ```import env```
- ```SECRET_KEY = os.environ.get('SECRET_KEY')``` (actual key hidden within env.py)  

9. Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

10. Set up the templates directory in **settings.py**:
- Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
- Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in top level of project file in IDE workspace.

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: ```web: gunicorn comlink.wsgi```
12. Make the necessary migrations again.

### Cloudinary API 

Cloudinary provides a cloud hosting solution for media storage. All users uploaded images in the FreeFid project are hosted here.

Set up a new account at [Cloudinary](https://cloudinary.com/) and add your Cloudinary API environment variable to your **env.py** and Heroku Config Vars.
In your project workspace: 

- Add Cloudinary libraries to INSTALLED_APPS in settings.py 
- In the order: 
```
   'cloudinary_storage',  
   'django.contrib.staticfiles',  
   'cloudinary',
```
- Add to **env.py** and link up with **settings.py**: ```os.environ["CLOUDINARY_URL"]="cloudinary://...."``` 
- Set Cloudinary as storage for media and static files in settings.py:
- ```STATIC_URL = '/static/'```

### Heroku deployment

To start the deployment process , please follow the below steps:

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
3. Enter an app name and choose your region. Click '**Create App**'. 
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your: 
   
   - **CLOUDINARY_URL**: **cloudinary://....** 
   - **DATABASE_URL**:**postgres://...** 
   - **DISABLE_COLLECTSTATIC** of value '1' (N.B Remove this Config Var before deployment),
   -  **PORT**:**8000**
   -  **SECRET_KEY** and value  
  
5. Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> ```['herokuappname', ‘localhost’, ‘8000 port url’].```
6. Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9.  Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. **DISABLE_COLLECTSTATIC**  may be removed from the Config Vars once you have saved and pushed an image within your project, as can **PORT:8000**.



## Credits
Some credits are included inline with the code.
- Amy for the README Layout idea and certain sections
- Copilot for user stories and coding support
- Coding Coaches.
- [Dev.to](https://dev.to/earthcomfy/django-user-profile-3hik) for user profile help
- HTML & CSS Validator
- Devtools Lighthouse
- AutoPrifix
- Mugs of tea and bacon sandwiches for moral support
- Cans of Monster for energy (order: 66)