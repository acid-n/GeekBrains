#!/usr/bin/env python
from flask import Flask, request
import os
# create app
# The app object is instantiated from the Flask class, by providing the name of the module (script) as a first parameter
app = Flask(__name__)

# Routes are defined using the route() decorator to tell Flask what URL should trigger our function. In our case, we have a unique route / which triggers the index() function, and this route accepts GET and POST requests:


@app.route('/', methods=['GET', 'POST'])
def index():
    # This index() function will have two blocks depending on the request type: GET or POST. If the request is of type GET, we simply show an html form which contains a text input named expression and a submit button
    if request.method == 'GET':
        # show html form
        return '''
            <h2>hostname: %s</h2>
            <form method="post">
                <input type="text" name="expression" />
                <input type="submit" value="Calculate" />
            </form>
        ''' % os.getenv('HOSTNAME')
#  If the function receive a POST which means that the form has been submitted, we retrieve the value filled inside the expression input using request.form object. After that, we evaluate the expression submitted using built-in eval() function and we print it in the browser:
    elif request.method == 'POST':
        # calculate result
        expression = request.form.get('expression')
        result = eval(expression)
        return '''
            <h2>hostname: %s</h2>
            <h3>result: %s</h3>
            <form method="post">
                <input type="text" name="expression" />
                <input type="submit" value="Calculate" />
            </form>
        ''' % (os.getenv('HOSTNAME'), result)


# If our script is executed and not being imported as a module in another script, we run our app. The debug parameter is set to True, to reload the server on code changes and provide us with helpful debugger messages
if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', 5000)
    app.run(debug=True, host=host, port=port)
