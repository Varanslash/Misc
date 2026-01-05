import sqlite3 as sql

oauth2 = False
manager = sql.connect("logins.db")
cursor = manager.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    content TEXT NOT NULL
);""")

def add_user(username, password):
    cursor.execute("INSERT INTO users VALUES (NULL, ?, ?)", (username, password))
    manager.commit()

def get_user(username, password):
    global oauth2
    cursor.execute("SELECT * FROM users WHERE username = (?) AND password = (?)", (username, password))
    oauth2 = True if cursor.fetchone() else False
    print(f"OAuth2: {oauth2}")

def make_post(username):
    global oauth2
    if oauth2:
        content = input("Enter your post: ")
        cursor.execute("INSERT INTO posts VALUES (NULL, ?, ?)", (username, content))
        manager.commit()
    else:
        print("You must be logged in to make a post.")

def delete_post(post_id, username):
    global oauth2
    if oauth2:
        cursor.execute("DELETE FROM posts WHERE id = ? AND username = ?", (post_id, username))
        manager.commit()
    else:
        print("You must be logged in to delete a post.")

def delete_user(username, password):
    global oauth2
    print("Are you sure you want to delete your account? This action is irreversible. (yes/no)")
    confirmation = input("> ").strip().lower()
    if oauth2 and confirmation == "yes":
        cursor.execute("DELETE FROM users WHERE username = ? AND password = ?", (username, password))
        manager.commit()
        oauth2 = False
    else:
        print("You must be logged in to delete your account.")

print("Welcome to Vasanistrus Labs!")
while True:
    action = input("Choose an action (register, login, post, exit): ").strip().lower()
    if action == "register":
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        add_user(uname, pwd)
        print("User registered successfully.")

    elif action == "login":
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        get_user(uname, pwd)
        print("Logged in successfully." if oauth2 else "Login failed.")

    elif action == "post":
        if oauth2:
            make_post(uname)
        else:
            print("You must log in first.")
    
    elif action == "list posts":
        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()
        for post in posts:
            print(f"Post ID: {post[0]},\n Username: {post[1]},\n Content: {post[2]}\n")

    elif action == "exit":
        break

    else:
        print("Invalid action. Please try again.")