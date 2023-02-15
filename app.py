from flask import Flask, render_template
import instaloader

   
def get_info(profile):

    followers = []
    for record in profile.get_followers():
        followers.append(record.username)
    
    followed = []
    xtra=[]
    for record in profile.get_followees():
        followed.append(record.username)
        if record.username not in followers:
            xtra.append(record.username)

    return followed, followers, xtra

app = Flask(__name__)

@app.route("/")
def index():
    load = instaloader.Instaloader()

    username = "yourusername"
    load.login(username,"yourpassword")

    profile = instaloader.Profile.from_username(load.context, username)
    followed, followers, xtra = get_info(profile)

    return render_template("menu.html", followed=followed, followers=followers, xtra=xtra)

if __name__ == "__main__":
     app.run(debug=False)
