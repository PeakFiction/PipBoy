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

<br/>
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



# Assignment 3 README.md:

## What is the difference between POST form and GET form in Django?
POST Form:

HTTP Method: POST
Purpose: Used to submit data to the server for processing, typically used when the form is used to create or update resources on the server.
Data in Request: Form data is sent in the request body, not in the URL.
Security: More secure for sensitive data as it doesn't expose data in the URL.
Length Limitation: No strict length limitation on data, but server and browser may impose their own limits.
Idempotent: Not idempotent, meaning multiple identical POST requests may have different effects on the server.

GET Form:

HTTP Method: GET
Purpose: Used to request data from the server and include parameters in the URL, typically used for searching or filtering data on the server.
Data in Request: Form data is appended to the URL as query parameters.
Security: Less secure for sensitive data because data is visible in the URL.
Length Limitation: Limited by the maximum URL length, which varies depending on the browser and server.
Idempotent: Idempotent, meaning multiple identical GET requests should have the same effect on the server (no side effects).

## What are the main differences between XML, JSON, and HTML in the context of data delivery?

XML, JSON, and HTML are three distinct data formats employed for delivering data, each serving unique purposes with distinct characteristics.

XML, or Extensible Markup Language, is a versatile and adaptable format utilized for organizing and storing data. It offers high customizability, enabling users to define intricate document structures through user-defined tags. XML is commonly employed when structured data needs to be exchanged between different systems, making it suitable for scenarios requiring data to be both human-readable and machine-readable. However, XML can be verbose due to its tag-based syntax, potentially resulting in larger file sizes when compared to formats like JSON. Additionally, parsing XML can be computationally more demanding.

On the contrary, JSON, short for JavaScript Object Notation, is a lightweight and easily readable format for data delivery. It excels at representing data in a manner closely resembling data structures in many programming languages, making it popular for web APIs and data exchange between web clients and servers. JSON is concise, leading to smaller data payloads in comparison to XML. Moreover, it is simpler for both humans and machines to parse. Nevertheless, JSON is less versatile than XML when it comes to defining complex document structures, and it lacks some of the self-documentation features found in XML.

HTML, or Hypertext Markup Language, is primarily utilized for structuring and presenting content in web browsers. Although it is not a data interchange format like XML and JSON, it plays a crucial role in data delivery on the web. HTML is designed for crafting structured documents that encompass text, multimedia, hyperlinks, and more, presenting information to users in an aesthetically pleasing manner. HTML documents can also incorporate JSON or XML data within them, often as part of a web page's content. This allows for embedding structured data, such as configuration settings or dynamic content, directly into web pages for client-side processing.

In summary, XML is a highly customizable and extensible format suitable for structured data exchange, JSON is a lightweight and easy-to-parse format often used for web APIs, and HTML is primarily employed for structuring and presenting content on the web but can also include JSON or XML data within web pages. The choice of format depends on the specific requirements of data delivery and the intended use case.

##  Why is JSON often used in data exchange between modern web applications?

##  Explain how you implemented the checklist above step-by-step (not just following the tutorial).

### Create a form input to add a model object to the previous app.
Inside the main folder, I created a folder named forms.py, which imports my ModelForm, and Product. And added a ProductForm function, and in the fields section I added a few attributes that suit the types of items that I will be storing in the database. I then added some more imports in views.py in the main folder and a new function called create_product that takes requests as an argument, the usage of this function is to create a new ProductForm. I also modified the show_main function in views.py to show the table of added items. I also added more imports from the functions that I've created previously, like create_product. I also added the path list to the create_product in urls.py. So that there's something to look at, I added a new .html file that will be used to show the Add New Item Page for the User, not only that, but I changed the main.html so that it can accommodate new buttons that will lead to the new create_product.html

### Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats.
For this one, I added the necessary imports in views.py in the main folder, and added show_xml function, and a show_json function. These functions are used to show the XML and JSON of the data that's stored. Next I create a function that is similar to show_xml and show_json, the only difference being is showing the data by its ID. 

### Create URL routing for each of the views added in point 2
To do this I routed the proper paths in urls.py. Such that when you go to /xml or /json, it will show the XML or JSON of the data. In addition, if you do xml/[id] or json/[id], it will show the XML or JSON (depending on the link) of the specific data with that ID. Before that, I also imported the necessary functions that was made in the previous step in the urls.py file.



## Access the five URLs in point 2 using Postman, take screenshots of the results in Postman and add them to README.md.
<img src="/assets/viewAsHTML.png">
<img src="/assets/viewAsJSON.png">
<img src="/assets/viewAsXML.png">
<img src="/assets/viewAsJSONID.png">
<img src="/assets/viewAsXMLID.png">

