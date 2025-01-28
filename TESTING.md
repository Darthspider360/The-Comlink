# Testing

This is the TESTING file for [Comlink](#) website.

Return back to the [README.md](README.md) file.
---

## **Contents**

- [Testing](#testing)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
---

## Validation

### HTML Validation

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

I have had to follow a different approach for validating my HTML for this project as the majority of my pages are developed using Jinja syntax such as '{% extends "base.html" %}' and '{{ form|crispy }}' and most require user authentication. The HTML validator will throw errors if I were to use my website's URL so I have had to follow the below approach for every page:

- Via the deployed Heroku app link, I have navigated to each individual page.
- Right clicking on the screen/CTRL+U/⌘+U on Mac, allows a menu to appear, giving me the option to 'View page source'.
- The complete HTML code for the deployed page will appear, allowing you to select the entire code using CTRL+A/⌘+A on Mac.
- Paste the copied code into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, revalidate by following the above steps and record the results.

| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- | 
| Home/Feed | 0 | 0 |
| Sign In | 0 | 0 |
| Sign Up | 4 | 0 |
| Sign out | 0 | 0 |
| Profile Page | 0 | 0 |
| Edit Profile | 0 | 0 |
| Add Post | 0 | 0 |
| View Post | 0 | 0 |
| Error 404 | 0 | 0 |

The 4 errors in the Sign up section are due to the AllAuth forms that I cant edit

### Python Validation
I used [CI python](https://pep8ci.herokuapp.com/#) for my python validation - checking the files i wrote and changed.

| App Name | admin.py | forms.py | models.py | urls.py | views.py |
|----|----|----|----|----|----|
| Comlink(main project)| na | na | na | [no errors](media/readme-images/comlink-app-python.png) | na |
| Feed | [no errors](media/readme-images/feed-admin-python.png) | [no errors](media/readme-images/feed-forms-python.png) | [no errors](media/readme-images/feed-models-python.png) | [no errors](media/readme-images/feed-urls-python.png) | [no errors](media/readme-images/feed-views-python.png) |
| Profile Page | [no errors](media/readme-images/profile-admin-python.png) | [no errors](media/readme-images/profile-forms-python.png) | [no errors](media/readme-images/profile-models-python.png) | [no errors](media/readme-images/profile-urls-python.png) | [no errors](media/readme-images/profile-views-python.png) |

### CSS Validation