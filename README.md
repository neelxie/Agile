## Agile
Agile Group Project
This is a commandline app where users can create account by signing up. Users can also create comments when logged into their accounts.

## Getting started
*  Clone [this](https://github.com/neelxie/Agile) git repo to local directory.
``` cd agile ```
*  Create a virtual environment:
``` virtualenv venv ```
*  Activate virtual environment:
``` venv\Scripts\activate ```
*  Install dependencies:
``` pip install -r requirements.txt ```
*  Do not forget to run this in the develop branch:
``` git checkout develop ```

## Feature
| User Role | Create Comment | Edit Comment | Delete Comment
|-----------|----------------|--------------|---------------
| Normal User |  True | Own Comment | own comment
| Moderator |  True | Own comment | Any comment
| Admin |  True | Any comment | Any comment

## Project Management Board
This is the [link](https://www.pivotaltracker.com/n/projects/2239687) to our pivotal tracker board.

## Contributors
| Name | Role | Contribution
|------|------|-------------------
| Derrick Sekidde | Product Owner | Created Pivotal Tracker Stories, tools intergration and Readme file
| Edna Nakajugo | Scrum Master | Implemented the fundamental users' model.
| Kisekka David | Senior Developer | Implemented the commandline interface for the app.
| Alex Sanya | Senior Developer | Implemented the comments model and functionality.
| Joseph Senabulya | Senior Developer | Implemented the Admin class model and related functionality

