
# Model View Template (MVT)
# Django follows the Model View Template (MVT) architecture, which is based on the Model View Controller (MVC) architecture.

# Model: It’s the backend where the database is defined. It helps handle the database by creating CRUD (Create, Read, Update, Delete) objects in the original database. It is used for storing and maintaining your data.(models.py)

# Object-relational mapping (ORM) is a programming technique that simplifies database interactions by enabling developers to work with relational databases using object-oriented programming languages.

# View: View is used to fetch data from the model. It executes business logic and carries data from the model to a template to render it properly. It also accepts HTTP requests and provides HTTP responses to client requests.(views.py)

# Template: It handles the user interface part and is hence called the presentation layer. Templates are files with HTML data used to display data. Content in these template files can be either static or dynamic.(directory templates)

# USER----------------DJANGO(Controller)
#                       |
#                       URL--------VIEW
#                                   |

#                                /     \
#                             MODEL   Template

# Django also provides a way to navigate around the different pages in a website.
# When a user requests a URL, Django decides which view it will send it to.
# This is done in a file called urls.py, using the path() function to associate a URL pattern with a view.

