from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Return HTML with a blue background
    return """
    <html>
        <head>
            <style>
                body {
                    background-color: lightblue;  /* lightBlue background */
                    color: white;             /* White text for contrast */
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                }
            </style>
        </head>
        <body>
            <h1>Hello from Docker!</h1>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0')
