# In this video we will learn about how to add forms and validations for the same.

1. In order to integrate Forms and validations we can use a flask libary called 'flask_wtf'
    pip3 install flask_wtf

2. To make the registration and login form we need to make use 'FlaskForm' this will be inherited by child classes.
    from flask_wtf import FlaskForm

3. To apply the Validations 
    from wtforms.validators import 
        - DataRequired
        - Email
        - Length
        - EqualTo


4. To use different input field
    - StringField('LabelName', validators=[DataRequired(), Length(min=2, max=20), Email(), EqualTo('Email')])
    - PasswordField()
    - SubmitField()
    - BooleanField('Remember Password')

5. Secret Key will help protect against modifying cookies and CSRF(Cross-Site-Request-Forgery) attacks.

6. We can generate a secret using secrets module
    import secrets
    secrets.token_hex(16)

7. Using a bootstrap form for Registraton.

8.  This is being used for preventing CSRF attacks
    {{ form.hidden_tag() }}

9. To make it available flash messages in our HTML file
    {% with messages=get_flashed_messages(with_categories=true) %}
        {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{category}}">
            {{ message }}
            </div>
        {% endfor %}
        {% endif %}
    {% endwith %}

10. if we fill the registration form and click on sign up it give us below error.

        ```
            Method Not Allowed
            The method is not allowed for the requested URL.
        ```

    Because we haven't specified that URL to be post request so we can solve this issue by mentioning it as POST request.