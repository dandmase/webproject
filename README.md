# webproject
Web Project - [*TopFestivals*][1]

[1]: https://github.com/dandmase/webproject

## Collaborators
* Dand Marbà
* Joel Romia
* Rubén González Molina
* Jose Ramon Noguero
* Ruben Querol

## Tecnologies

For the development of the bussines model of TopFestivals we use the following tecnologies:
- [X]  Use of **Framework Django** 





## How to RUN
### Requisites
- [X] This project uses [*python 3.9*][2] and pip.
- [X] Open requirements.txt and install all de requeriments.

[2]: https://www.python.org/downloads/release/python-394/ "Download Python 3.9"
  
### Running Project
First of all you *need to clone the repository* before the requeriments part:  
Check your python version 
```console
$ python3 -V
```
Finally:
```console
$ sudo apt install python3-django
$ python manage.py runserver
```

### Users
http://127.0.0.1:8000/admin/
  - *Admin* User
    * Username : *admin*
    * Password : *admin*

  - *Normal* User
    * Username : *provauser*
    * Password : *user1234*

### Design considerations
We wanted a webpage with a lot of festivals where people can add a comment about that festival. So in the main page we think that should appear all the registered festivals with a picture of it and some few details.
Then when you want to see the information of a festival or the comments that users had add, you have to click te name of he festival and the user would be redirectioned to another page with all the information about the festival,
the comments and all the artist that will play. When all the functionalities worked correctly, we had concentrated on the design of the page trying differnt kinds of disgn we finally choose this. 
And we do the same design when you want to see the information of an artist.
