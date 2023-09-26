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
JSON (JavaScript Object Notation) is often used in data exchange between modern web applications for several key reasons:

1. Human-Readable Format: JSON is a human-readable format, making it easy for developers to work with and debug. Its structure resembles JavaScript objects, which are widely used in web development, making it familiar to many developers.

2. Lightweight: JSON is a lightweight data interchange format. It doesn't include a lot of unnecessary characters, which means it reduces the data transfer overhead, making it efficient for transmitting data over networks, especially in situations where bandwidth is limited or costly.

3. Language Agnostic: JSON is not tied to any particular programming language. It can be used with virtually any modern programming language because parsers and libraries for JSON are readily available for most programming languages. This language-agnostic nature makes it a popular choice for web services that need to communicate with different technologies.

4. Wide Support: JSON is supported by a wide range of programming languages, databases, and tools. Most modern web development frameworks and libraries include built-in support for working with JSON, simplifying the process of encoding and decoding data.

5. Easy to Convert: JSON can be easily converted to and from native data structures in most programming languages. This makes it straightforward to serialize data on the server, transmit it to a client, and deserialize it for use in the client-side code.

6. JavaScript Integration: Since JSON's syntax is based on JavaScript object notation, it can be directly consumed by JavaScript on the client-side, making it a natural choice for AJAX requests and data manipulation in web applications.

7. Standardized: JSON is an open standard specified by RFC 8259, which means there are clear guidelines for its structure and usage. This standardization ensures that JSON data can be reliably exchanged between different systems.

8. Security: JSON is considered safer than other data interchange formats like XML, which can carry security vulnerabilities such as entity expansion attacks. JSON does not support entities or complex structures like XML, reducing the risk of security issues.

9. Web APIs: Many web services and APIs use JSON as their preferred format for exchanging data due to its efficiency and compatibility with web technologies. This makes it easy for developers to integrate data from different sources into their web applications.

In summary, JSON's simplicity, efficiency, wide support, and human-readability make it a popular choice for data exchange between modern web applications, enabling seamless communication between various components of web-based systems.


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

# Assignment 4 README.md:

## What is UserCreationForm in Django? Explain its advantages and disadvantages.
UserCreationForm is a built-in user authentication system that comes with Django. It’s designed to handle user registration i.e. usernames, passwords, etc. In a way, it simplifies the process of creating user accounts in web applications

The advantages of UserCreationForm are:
Ease of Use — it instantly provides a ready-made form class with the necessary fields to create a user account, which saves time for the developers

Integration with Authentication System — The form integrates easily with Django’s authentication system, which means password hashing, user account creation, and other security-related aspects is being automatically done.

Customisable — Even though Django provides default values and fields that makes it easier for beginners, you can easily customise it to include much more fields by creating a custom form class

Validation — Password validation is included into the form to make sure users submit secure passwords and that the password and password confirmation boxes are same.

The disadvantages of UserCreationForm are:

Limited to User Model — UserCreationForm is suitable for simple user registration, however it was created exclusively for the User model that comes with Django. You might need to design a unique registration form that adheres to the fields and specifications of your custom user model if you're using one.

Lack of Email Verification — Email verification is not included by default in UserCreationForm. You must implement this independently if your application requires email confirmation as a requirement for registration.

Minimal User Data — 	UserCreationForm only offers a minimal set of fields (often only a username and password) and excludes any user profile data. You will need to either extend the form or add a separate profile creation phase if your application wants to collect more user information during registration.

Limited Styling — The form has the required functionality, but it doesn't have a lot of styling or front-end elements. In order to modify the form's appearance to match the style of your application, you'll need to create templates and add CSS styles.

## What is the difference between authentication and authorization in the Django application? Why are both important?
Authentication refers to the process of verifying the identity of a user, ensuring that they are who they claim to be. In a Django application, this typically involves user registration, login, and password management. Django provides a built-in authentication system that handles user authentication seamlessly, allowing users to create accounts, log in, and maintain their sessions securely.

Authorization, on the other hand, deals with determining what actions a user is allowed to perform once they are authenticated. It defines the permissions and access control rules that dictate which parts of the application a user can access and what operations they can perform. Django's authorization system revolves around defining user roles, assigning permissions to these roles, and then checking these permissions before allowing a user to carry out specific actions or access certain views.

Authentication and authorization are crucial in web applications because they collectively ensure the security, privacy, and compliance of user data while allowing for customizable access control tailored to different user roles.

## What are cookies in a website? How does Django use cookies to manage user session data?
Cookies are little data files that a website stores on a user's computer. They frequently serve as storage for data related to a user's session or preferences. By saving a session ID in a cookie, Django manages user session data. Django establishes a session for each user when they log in, assigns a special session ID, and keeps this ID in a cookie on the user's device. By doing so, Django is able to recognise the user on subsequent requests and obtain their session data from the server, enabling the maintenance of user sessions across many web pages.

## Are cookies secure to use? Is there a potential risk to be aware of?
For storing non-sensitive data like session IDs or user preferences, cookies are often secure. However, there could be problems connected to cookies. If not handled appropriately, they may be susceptible to attacks like cross-site scripting (XSS). Additionally, if cookies are sent via unencrypted connections (HTTP instead of HTTPS), they may be stolen. The use of HTTPS and making sure that cookies holding sensitive data are securely encrypted and guarded against unauthorised access are only two examples of secure procedures that developers must put into practice.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).

### Implement registration, login, and logout functions to allow users to access the previous application.
To implement registration, login, and logout functionality, I followed a structured approach. First, I designed a registration form and associated function. Within the views.py file, I introduced the register function, alongside essential imports such as UserCreationForm. This function dynamically generates a registration form, and upon submission, creates a new user account. 

To complement this, I crafted a dedicated HTML page named register.html. This page serves as the entry point for individuals looking to create a new user account. I also integrated this page into the application's URL routing by specifying the corresponding path in urlpatterns within the urls.py file and importing the relevant function from views.py.

For the login functionality, I employed a similar approach. I imported the necessary functions into views.py, establishing a login_user function responsible for authenticating user credentials received through a request. A corresponding HTML page, `ogin.html, was designed to facilitate user login. Once again, I ensured that the URL routing and function imports were appropriately configured in urls.py.

The logout functionality was implemented in a comparable fashion. The logout_user function was created, and a 'Log Out' button was integrated directly into the main page instead of introducing a new HTML file. To complete this, I included the required imports and URL paths in urls.py.

Furthermore, to enhance security, I implemented a prerequisite for users to log in before accessing the main page. This was achieved by applying a decorator atop the show_main function in views.py, utilizing the login_required decorator from Django's decorator library. This measure ensures that users must authenticate themselves before gaining access to the main page, enhancing the overall security of the application.

### Connect Item model with User.
To establish a connection between each item model and its respective user creator, I implemented a straightforward process. Initially, in the models.py file, I imported the 'user' module from the Django library and incorporated a 'user' attribute within the 'Product' class. This attribute was configured as a ForeignKey, ensuring that each item became associated with the user responsible for its creation.

Subsequently, I proceeded to enhance the 'create_product' function. This modification ensured that every item generated through this function was automatically linked to the currently authenticated user. Additionally, I made adjustments to the 'show_main' function, enabling it to display information about the presently logged-in User, providing a seamless user experience by establishing these essential connections between users and their created items.

### Create two user accounts with three dummy data entries for each account using the model previously created in the application.
<img src="/assets/peakfictionuser.png">
<img src="/assets/xlntuser.png">

### Display the information of the logged-in user, such as their username, and applying cookies, such as last login, on the main application page.

To achieve this functionality, I made several improvements within the codebase. In the views.py file, I introduced the necessary imports, including datetime, reverse, and HttpResponseRedirect. Within the login_user function, I enhanced it to record the user's most recent login timestamp. Additionally, in the show_main function, I expanded the context by introducing a new item called 'last_login.' This item retrieves the user's last login time from the stored cookies.

To ensure that this information remains accurate, I also made corresponding adjustments within the logout_user function. Here, I implemented logic to remove the last login cookie when a user logs out.

To present this valuable data to the user, I refined the main.html template, incorporating a section to display the 'Last Login' session time for the currently authenticated user. Finally, I conducted necessary migrations to ensure that all changes in the models were seamlessly integrated into the application, resulting in a fully functional and user-friendly solution.






