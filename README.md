
# WELCOME TO MY DIARY APP

[![Build Status](https://travis-ci.org/ekumamait/My-Diary.svg?branch=api_branch)](https://travis-ci.org/ekumamait/My-Diary)

[![Coverage Status](https://coveralls.io/repos/github/ekumamait/My-Diary/badge.svg)](https://coveralls.io/github/ekumamait/My-Diary)


# PROJECT SETUP


1. Clone the Repository
`https://github.com/ekumamait/My-Diary`

2. Navigate to the application directory
`cd My-Diary`

3. install all dependencies
`pip install -r requirements.txt`

4. Run the application
`python My-Diary`


# AVAILABLE ROUTES


EndPoint | Functionality    
--- | --- 
/api/v1/entries methods=['GET' | Fetches all entries created                        
/api/v1/entries/entry_id> methods=['GET' | Fetches a particular entry by id
/api/v1/entries', methods=['POST'] | add a new entry 
/api/v1/entries/int:entry_id', methods=['Delete'] | delete an entry
/api/v1/entries/int:entry_id', methods=['PUT'] | edit a single entry

[Here is a link to the application]
(https://dashboard.heroku.com/apps/ekumamait)
