# In this article we will learn about 'templates' directory

1. 'templates' directory allow us to render complex HTML snipet.

2. We should import 'render_template' function in our flask app to redirect to specified html file.

    render_template('<html_file_name.html>')

3. Let us assume that we have received a data from the DB and then we have decided to pass that data
    to html file and access and render them on page. We can do this using templating engine called Jinja2
    flask uses Jinja2 template to render the data inside html file.

    Syntax:
        render_template('<html_file_name.html>', variable_name=data_to_be_passed)

    e.g.
        render_template('home.html', posts=posts)

    - For loop
        {% for post in posts %}
            <h1> {{ post.title }}</h1>
        {% endfor %}

    - If else condition
        {% if title %}
            <h1> Flask Blog - {{ title }} </h1>
        {% else %}
            <h1> Flask Blog </h1>
        {% endif %}

4. Mistakes that should be aware while writing loop or condition
    {% if title %}
    <h1> Flask Blog - {{ title } } </h1>

    In above snippet while printing in h1 titile } bracket is placed without attaching that might create error.

5. Pass the title from the render_template() function to render it on the browser based on if condition.

6. If we look at both the html files other than content present in body tag other thing is same in both the files.
    So we violating the basic rule of programming DRY - Do not Repeat Yourself

    To solve this issue, we will use something called Template Inheritance where we will have a single layout html
    file which has the duplicate code present in both the files and then this fill will be inherited by child files
    using {% block %} section.

    Parent Template - layout.html
    Child Template - home.html, about.html

    layout.html
    {% block content %}
    {% endblock %}

    If home/about.html wants to extend the parent template

    {% extends "layout.html" %}

7. Integrating Bootstrap with our application 
    For starter template follow the link - https://getbootstrap.com/docs/4.4/getting-started/introduction/
    Latest version - https://getbootstrap.com/docs/5.3/getting-started/introduction/

8. We have improved our UI by adding nice navigation bar and also we have added main.css
    This snippets were taken from Corey Github https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/snippets 
    
    To integrate with our flask application we have imported 'url_for("css_directory_name", filename='<css_file_name>')

    e.g. <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='main.css')}}">
