from flask import Flask, redirect

app = Flask(__name__)
domain = "theantechs.com"
# Define role-based access control based on path
@app.route('/it')
def page_it():
    # Redirect to a different URL, e.g., http://127.0.0.1:5600
    return redirect(f"http://corp.{domain}:8080/it", code=302)

@app.route('/hr')
def page_hr():
    # Redirect to a different URL for HR, e.g., another service or page
    return redirect(f"http://corp.{domain}:8880/hr", code=302)

@app.route('/')
def index():
    return """
        <h1>Welcome to your company page!</h1>
        <p><a href="/it">/IT admin</a> space </p>
        <p><a href="/hr">/HR</a> space</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)