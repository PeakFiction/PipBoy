# My Deployed App:
https://pipboy.adaptable.app/main


# Detailed Step-By-Step
I would like to preface that most of the things that I have done to finish this assignment is with the help of the tutorial.

## Creating a new Django Project
First, I setup the directory with the name of my desired project, where I would navigate to it using Terminal and create and activate the virtual environment using python3 -m venv env, and source env/bin/activate.

After that I made set up the dependencies by creating a requirements.txt filled with its dependencies, and install it from terminal using pip install -r requirements.txt. Finally I used django-admin startproject pipboy to start the project.

## Create an app with the name main on the project
I then create an app with the name main by typing "python manage.py startapp main", in which then I register it in settings.py, in the Installed Apps section

## Create a URL routing configuration to access the main map
I then create a urls.py inside the main application directory, which functions as some sort of road/route to the url for the views function that will be made later on.

## Create a model on the main app with the name Item, and these mandatory attributes...
I then create a models.py file in the main application directory, using the template from the tutorial, I changed some of the things to match this assignment, as well as adding some more stuff to my liking, i.e. making the site better, more "canon", etc.

## Create a function in views.py that returns the HTML template containing your application name, your name, and your class
I then open the views.py that's located in the main directory, imported render from django.shortcuts, and add a show_main function that shows the text in accordence to models.py.

## Create a routing in urls.py to map the function in views.py to an URL
I then go back to the urls.py in the main directory to configure the URL such that the website will display the page properly by entering the appropriate code. After, I go to the other urls.py in the pipboy directory to include its path as an import and in the urlpatterns section. 

## Deploy the App through Adaptable so it can be seen thru the internet
Once I'm done, I checked for some other mistakes I might have missed by using the "python manage.py runserver" command and opening the local server using "http://localhost:8000/main/". If all is good, then I upload the local repository to my github repository by using the 4 mantras of git. Connected my Github account to adaptable.io, and deployed the app. And as per the tutorial, we'll be using Python's App Template, PostGreSQL, and have some custom Start Commands as well.

## Diagram
<img src="/assets/DiagramPBD.jpg">

<br />
## What is the Purpose of a Virtual Environment?
You may work on Python projects with separated dependencies by using a virtual environment, which is a self-contained directory that includes a Python interpreter and a selection of libraries. A virtual environment's main function is to manage and isolate project-specific dependencies and configurations, guaranteeing that several projects may each have their own distinct Python environment free from conflict. Here are some major arguments in favour of virtual environments:

Isolation: Project dependencies are kept apart in virtual environments, preventing conflicts between several projects that may depend on various versions of libraries or packages.

Dependency management makes it simpler to replicate the environment on several machines by allowing you to easily manage and control the versions of libraries and packages your project requires.

Version Compatibility: Working on projects that need several Python versions in virtual environments enables you to make sure that your project uses the right interpreter during runtime.

Cleaner Development: By avoiding the chaos of global Python packages, virtual environments assist maintain a tidy and organised development environment.

Security: By isolating dependencies, you may update libraries just as needed and reduce the chance of disrupting other projects, helping to prevent possible security issues.

It is possible to create a Django web app without using virtual environments, but it is recommended for the reasons mentioned above.

## What is MVC, MVT, and MVVM? Explain the differences between the three.
Architectural patterns like MVC, MVT, and MVVM are used in software development to organise and structure the code and divide concerns inside an application. These design patterns are often used in a variety of software kinds, including online and desktop programmes, and each one approaches the separation of concerns in a somewhat different manner. Here is a summary of each pattern and how they differ from one another:

### Model-View-Controller (MVC)

Model: Depicts the data and business logic of the application. It is in charge of overseeing and modifying the data and informing the View if something changes.

View: Represents the application's presentation layer, which is in charge of showing the user's data. Updates are brought to the user's attention after being received from the Model.

Acts as a bridge between the Model and the View, the controller. It manages user input, handles requests, updates the Model in response to Model changes, and refreshes the View.

Differences:

The Controller in MVC is in charge of processing user input and overseeing the data flow between the Model and the View.
In conventional online applications, where the Controller receives and handles HTTP requests, MVC is frequently employed.

### Model-View-Template (MVT):

Model: The Model represents the data and business logic of the application, just like the MVC pattern does.

Similar to the View in MVC, the View represents the presentation layer and is in charge of showing the data to the user.

Template: MVT introduces the idea of templates, as contrast to MVC. Templates specify the presentation of data but do not include application logic. They are in charge of producing the final result that is seen to the user.

Differences:

MVT is a design pattern that is frequently connected to web frameworks like Django. In MVT, the Template is in charge of producing HTML dynamically, while Django's framework components frequently handle the Controller logic.

### Model-View-ViewModel (MVVM)

Similar to MVT and MVC, the model represents the data and business logic of the application.

View: This component, which represents the display layer, is typically more passive in MVVM than in MVC or MVT. It keeps track of the ViewModel and binds to it.

Acts as a bridge between the model and the view, or viewmodel. It makes information and commands available for the View to bind to and display. It frequently includes presentation logic, allowing the View to be lighter and more presentation-focused.

Differences:

Modern client-side apps frequently employ MVVM, particularly those developed using frameworks like Angular, Vue.js, or Knockout.js.
To accomplish a separation of concerns and produce more tested and manageable code, MVVM's ViewModel is in charge of making data and commands available to the View.
