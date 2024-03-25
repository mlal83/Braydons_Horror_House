# Braydon's Horror House PROJECT README

### Author Manjula Lal,

## Contents

- Brief
- External user’s goal:
- Site owner's goal
- Project Initial ERD and data base design
- Develop strategy and Wireframe
- Miro Board
- Balsamiq
- Lucid Chart
- Github project and Milestones
- Features
- Styling frontend development
- Fixed Bugs
- Unfixed Bugs
- Testing
- Future features and modifications
- Tools and Technology used
- Credits

## Brief -- Project 3: Braydon's Horror House

Welcome to the Braydon's Horror House platform. Our platform aims to promote an entertaining experience for horror enthusiasts who wish to share there stories and experiences and to build a community where people can engage with each other.

![iamresponsive](/static/images/iamresponsiveppp.png)

### External user’s goal:

"The user seeks engaging content that entertains and encourages return visits to the site. Additionally, they desire to be part of a community where they can interact with other users who share similar interests. Providing the option for users to contribute their own content personalizes their experience, fostering a sense of ownership and connection. Optional user details are available to enhance the personalization of the website, adding a key personal touch."

### Site owner's goal:

"My goal is to entertain users and encourage them to engage within a community centered around shared interests, particularly in spooky stories. I've noticed a significant market for people interested in this genre, and my aim is to differentiate my website by offering unique features not commonly found on modern platforms. I am committed to continuing the development of this site, recognizing its potential for growth.

I wanted to create a website that strikes a balance, appealing to a wide audience without overwhelming them. It's important to me that users don't feel stressed or overwhelmed when reading stories, so I've focused on creating an environment that stimulates the mind while fostering creativity."

### Project Initial ERD and data base design

I had created this ERD to design my database prior to creating the models, so I had a physical plan on how my database would be structured.
![Project ERD](/static/images/erd3.png)

## Develop strategy and Wireframe

## Miro Board

I initially used the Miroboard for the initial iteration. start until finished, placed all articles and pictures we will be using and the technology that will be used.

## Balsamiq

I utilized Balsamiq to design the initial concept of the 'Braydon's Horror House' website, encompassing all user features, navigation elements, and placeholders for images to be integrated into the website. Throughout the design process, I made minor adjustments to enhance user-friendliness and ensure responsiveness."

![Balsamiq Wireframe](/static/images/wireframe.png)

## Lucid Chart

I decided to create a visual map of the website so we could clearly conceptualise the project as a whole. As you can see there alot of work left to do for this website and alot of potential of scope.

![Lucid Chart](/static/images/lucidPP.png)

## Github project

I utilized the GitHub project feature to craft our User Stories based on user requirements, outlining the project scope and identifying tasks for future iterations. Additionally, I established milestones and created corresponding issues, all of which are accessible on GitHub for review.

## Features

- When users visit the website, they will encounter a list of stories displayed in rows of three. Clicking on a story will allow them to read it. Each story card features an automated picture, ensuring consistency across the website's design and providing a seamless user experience.

![stories](/static/images/stories.png)

- The 'Submit Story' option and dropdown form are located below the stories section. To write their story, users must be logged in. If they are not logged in and attempt to submit a story, they will be redirected to the login page before submission.

![submit story and dropdown](/static/images/story-dropdown.png)

- The registration page includes a disclaimer and functionality that enables users to successfully create their accounts."

![register Page](/static/images/sign-up-page.png)

- The navigation bar features options such as homepage, login, and register. Upon logging in, the navbar expands to include the option to view the user's profile. Additionally, if the user uploads a picture, it will be displayed in the navbar until the user signs out.

![navbar](/static/images/navbar.png)

- The profile feature offers users a more personalized connection to the website, enabling them to attract other users by sharing their social links, a bio, and uploading a picture. It's important to note that all of these elements are optional, as uploading stories and leaving comments only requires the user to be logged in. Additionally, at the bottom of the profile page, users can view the stories they have added to the website

![profile](/static/images/profile.png)

- When a user uploads a story, clicking on the story title redirects the user to a page where the full story is available for viewing. Under the story title, users will find details about the author of the story, including their bio and picture if available.

![inside card](/static/images/inside-card.png)

- The comments section allows users to write comments under the stories. Users have the option to edit and delete their comments. Additionally, the section displays the total number of comments the story has received.

![comments](/static/images/comments.png)

## Styling frontend development

I decided to use a gradient for the navbar, footer, and background to create an eerie yet welcoming atmosphere. For the navbar and footer, I opted for the 'moons spot' gradient, while I chose a purple gradient for the rest of the website. Additionally, I incorporated pictures created by AI to give the website a more original and personalized appearance, distinguishing it from others in the same entertainment niche. Overall, the combination of gradients and AI-generated images successfully achieves the desired eerie yet welcoming ambiance for the website.

## Fixed Bugs

- The problem I was having was that even though my CSRF_TRUSTED_ORIGINS were correct, the screen on my development environment kept throwing errors. It was noticed then that the numbers at the end of the URL kept iterating by one. So, after changing the number at the end of my URL, I was able to see my webpage.

![Iteration issues](/static/images/iteration-issue.png)

- I was encountering integrity errors, and in order to fix them, I had to create a new function to rectify the issue.

![Integrity error](/static/images/integrity-error.png)

- The issue arose because the URL /stories/set_avatar/ was being matched by the stories_detail pattern instead of the set_avatar pattern. This occurred because the set_avatar pattern was defined after the stories_detail pattern in the urlpatterns list.

Django processes URL patterns sequentially, stopping as soon as it finds a match. Because the stories_detail pattern was defined before the set_avatar pattern, Django matched /stories/set_avatar/ to the stories_detail pattern, resulting in the post_detail view being called instead of the set_avatar view.

To resolve this issue, rearranged the urlpatterns list so that the set_avatar pattern is defined before the stories_detail pattern. This ensures that requests to /stories/set_avatar/ are correctly routed to the set_avatar view.

![Issue with URL](/static/images/url3.png)

- Before adding the slug field, there were duplicated field declarations within the Story model. This duplication caused confusion and could lead to errors. The corrected version removed the duplicated fields, ensuring clarity and consistency in the model definition.

![Slugify](/static/images/slugify.png)

## Unfixed Bug

Though the profile page can be updated as many times as the user wants, the edit button will not work. This functionality is something that will be improved for the next iteration.

The comments and users storys are submitting successfuly to the database and I am able to submit them to the website successfully, however the modal message that it has 'successfully submitted' will not show. My code broke a few times and in the midst of fixing it, I must have triggered something. Its an improvment I must improve upon in my next iteration.

## Testing

- All top level links works as expected.

- User Account Creation works as expected.

- User login and logout works as expected.

- User comments and reviews have full CRUD functionality.

## Future features and modifications

Eventually, this website will allow users the option to pick an avatar instead of uploading a picture. The decoration of the website is still a work in progress, with plans to provide users the ability to listen to the content as well as reading it. Additionally, an online shop will be implemented where users can buy and sell their horror merchandise, alongside Braydon's merchandise which will consist of books. Braydon will act as an intermediary for payments, receiving a share of the price the users' items are sold at. The implementation of the Avatar option will be deferred to the next iteration due to time constraints.

## Tools and Technology used

- HTML used for the main site content.

- CSS used for design website.

- JavaScript used for user interaction.

- Python used for back-end programming.

- Git for version control.

- Bootstrap used alongside CSS to help build faster and help enhance user experience and responsiveness.

- Django used for Python framework.

- ElephantSQL for Postgres database.

- Heroku was used to deploy the back-end.

- Cloudinary used for online static file storage.

## Credits

I would like to extend a huge thanks to my facilitator, David Calikes, and my coding coaches, Kevin and Martin, at the Code Institute for their exceptional guidance and support. Additionally, I would like to give a special thanks to my mentor, Daisy, who has supported me throughout my journey. project

chat gpt was used to enhance my knowledge, help with identifying bugs, assist with indenting issues and help with my function in the view which was my submit_comment.

Other notable links
How-to-create-a-drop-down-list-in-a-Django-form.php
Stackoverflow.com
https://gencraft.com/generate
https://docs.djangoproject.com/en/5.0/ref/models/fields/
https://lucid.app/users/login#/login?folder_id=recent
https://app.diagrams.net/
https://www.eggradients.com/gradient/moon-spot
https://blog.logrocket.com/css-header-styles-cross-browser-compatibility/
https://dyatmika.org/students/my-favourite-short-scary-stories/
https://reintech.io/blog/implementing-profiles-in-django-tutorial
https://app.diagrams.net/
https://docs.djangoproject.com/en/5.0/ref/models/fields/
