# Learning Flask

1. Creating a virtual env
    python3 -m venv my_env

2. Activating the environment
    source my_env/bin/activate

3. Deactivating the environment
    deactivate

4. Installing flask module
    pip install flask

5. To list down the installed/present libraries in a created env
    pip list

6. To set the environment variable
    Linux/Mac - export FLASK_APP=flaskblog.py
    Windows   - set FLASK_APP=flaskblog.py

7. To list down the enviroment variables
    env

8. What is decorator here in flask @app.route?
    Way to add additional functionality to existing functions

9. Now we are done with setting the env varible we can run the flask app using below command:
    flask run

10. Access the flask app on 
    http://127.0.0.1:5000

11. If you are changing the code and that should be hot reloaded then we should set
    export FLASK_DEBUG=1
    i.e True

    In this way if we make any changes inside the code we don't need to rerun the code.
    Instead it will pick the changes and run itself

12. To run the script directly add below code snippet
    if __name__ == "__main__":
        app.run(Debug=True)

    python3 flaskblog.py

13. 404 Status code - URL not found