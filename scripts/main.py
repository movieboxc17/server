from flask import Flask, render_template_string

app = Flask(__name__)

# Define your HTML template as a string
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #2b2b2b;
            color: #ffffff;
            text-align: center;
            margin: 0;
            padding: 50px;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Flask App!</h1>
    <p>This is a basic web application using Flask.</p>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
