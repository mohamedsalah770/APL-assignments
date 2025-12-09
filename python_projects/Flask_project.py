#!/usr/bin/env python3

from flask import Flask, render_template_string, request, redirect, url_for, session
import sqlite3
app = Flask(__name__)
app.secret_key = "change_me_to_something_complex_please"

auth_layout = """
<!doctype html>
<html>
  <head>
    <title>{{ page_title }}</title>
    <style>
        body { font-family: sans-serif; max-width: 400px; margin: 50px auto; text-align: center; background-color: #f4f4f4; }
        form { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input { width: 90%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 4px; }
        button { padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .error { color: red; }
    </style>
  </head>
  <body>
    <h2>{{ page_title }}</h2>
    <form method="POST">
      <input type="text" name="u_name" placeholder="Enter your Name" required /><br />
      <input type="password" name="p_word" placeholder="Enter your Password" required /><br />
      <button type="submit">
        {% if page_mode == 'signin' %}Sign In{% else %}Register Now{% endif %}
      </button>
    </form>
    <p>
      {% if page_mode == 'signin' %}
        New here? <a href="/register">Join us</a>
      {% else %}
        Member already? <a href="/signin">Go to Login</a>
      {% endif %}
    </p>
  </body>
</html>
"""

dashboard_layout = """
<!doctype html>
<html>
  <head>
    <title>Member Area</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; }
        h1 { color: #2c3e50; }
        a { color: red; text-decoration: none; font-weight: bold; }
    </style>
  </head>
  <body>
    <h1>Hello, {{ member_name }}!</h1>
    <p>You are now inside the secure area.</p>
    <a href="/signout">Exit (Logout)</a>
  </body>
</html>
"""

def setup_database():
    db_link = sqlite3.connect("app_data.db")
    cursor = db_link.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS members(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            handle TEXT UNIQUE,
            secret TEXT
        );
        """
    )
    db_link.commit()
    db_link.close()

@app.route("/")
def dashboard():
    if "active_member" in session:
        return render_template_string(dashboard_layout, member_name=session["active_member"])
    return redirect(url_for("signin"))
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        input_user = request.form.get("u_name")
        input_pass = request.form.get("p_word")

        db_link = sqlite3.connect("app_data.db")
        cursor = db_link.cursor()

        try:
            cursor.execute(
                "INSERT INTO members (handle, secret) VALUES (?, ?)",
                (input_user, input_pass),
            )
            db_link.commit()
            db_link.close()
            return redirect(url_for("signin"))
        except sqlite3.IntegrityError:
            db_link.close()
            return """
            <h3 style='color:red'>Name unavailable!</h3>
            <p><a href="/register">Try a different name</a></p>
            """
    return render_template_string(auth_layout, page_mode="signup", page_title="Create New Account")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        target_user = request.form.get("u_name")
        target_pass = request.form.get("p_word")

        db_link = sqlite3.connect("app_data.db")
        cursor = db_link.cursor()
        
        cursor.execute(
            "SELECT * FROM members WHERE handle=? AND secret=?", (target_user, target_pass)
        )
        member = cursor.fetchone()
        db_link.close()

        if member:
            session["active_member"] = target_user
            return redirect(url_for("dashboard"))

        return """
        <h3 style='color:red'>Wrong credentials! Try again.</h3>
        <p><a href="/signin">Back</a></p>
        """
    return render_template_string(auth_layout, page_mode="signin", page_title="Member Login")

@app.route("/signout")
def signout():
    session.pop("active_member", None)
    return redirect(url_for("signin"))


if __name__ == "__main__":
    setup_database()
    app.run(debug=True)