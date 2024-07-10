# CC-task-3

This task at first was tricky to understand. First I installed docker desktop and pull the postgres image then, i ran the image with name postgres_0 and exposed the ports by -p 5432:5432 and by -v flag following the absolute path of init.sql, created a volume to get it read by postgres.


Then for creating api, i used django rest framework(drf). First created a project and app by startproject and startapp cmd then, in setting.py made some alterations in intalled_apps adding rest_framework and name of the app created and databases changing the engine to postgres form default sqlite and giving the credentials.
Then added api/ in the urlpattern of urls.py of the main app and created a urls.py file in the task_3 app for the 3 methods of adding retriving and deleting a file and created models in models.py of task_3 app to avoid using string queries because of injection attacks. Lastly, in the views.py file i defined 3 methods of the adding retriving and deleting the file in the database.
then made migrations and ran server and checked the working of api using postman.


U can ignore the main config.py files
