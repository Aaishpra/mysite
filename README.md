
# mysite
Just an App for Learning Django.Made from Django documentation.




![image](https://user-images.githubusercontent.com/66299533/94665750-2b021a80-032a-11eb-8af8-a785a0d31d59.png)
=======


This is just a project made for learning Django

![image](https://user-images.githubusercontent.com/66299533/95672357-c4002380-0bbd-11eb-873d-5894059215ff.png)

Polls
=====

Polls is a Django app to conduct Web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.

