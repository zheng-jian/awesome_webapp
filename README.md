# Python web blog application

This is a python web practice producted by Mr.Liao (https://www.liaoxuefeng.com/) 

  - MVC framework based on aiohttp
  - Orm, aiomysql Connection pool, mysql
  - Web middleware, restful api,


### Done:
    Model user, blog, comment
    orm, connection pool
    front page '/'and its handler
    api to get all user
    
### Didn't finish:
    sign in and log in
    authentication
    publish blog, comments

Functions(in file 'www'):
    app.py : contains init and middleware
    coroweb.py: decorates url handlers, registers url handlers in app
    handlers.py: url handlers
    orm: orm to mysql
    models: 3 models ,user, blog, comment

### Summary: 
    Good to learn about python web framework and process, orm
    Can help developpers focus on adding handlers
    But
    Python code without comment is very hard to review and read.
    Hard to maintain
    And can not find a job as python back-end in China :(

Move to a new project 'Community' with spring and bootstrap
