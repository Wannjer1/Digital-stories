# MODERN STORIES

Author: Ann Wanjeri

## Description

This is a flask application that allows users who have signed up to coment on the posted blogs. Users can also subscribe to receive emails every time a new blog is published. The application also enables writers to post blogs, edit and delete blogs.

## User Story

- A user can view the most recent blog
- A user can view and comment on the blogs
- A user receives an email alert when a new post is made by joining a subscription.
- A user sees random quotes on the blog
- A writer can create a blog, update or delete blogs they have created.

## Behaviour Driven Development

## Installation

1. Clone the repository
2. CD into the folder and install requirements
   > cd JymBlog
   > pip install -r requirements.txt
3. Export the configuration
   > export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
4. Run the application
   > python manage.py server
5. Test the application
   > python manage.py test

## Technologies Used

- Python3.9
- Flask
- Heroku

## Known Bugs

There are no known bugs currently but pull requests are allowed incase you spot a bug

# License
