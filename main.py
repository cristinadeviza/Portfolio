
# from flask import Flask, render_template,request,redirect,url_for
# import json

# app = Flask(__name__)

# dictionary = {}

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route("/redirect/<destination>", methods=["GET", "POST"])
# def google_redirect(destination):    
#     destinations = {
#         "github": "https://github.com/cristinadeviza/Huddle",        
#         "demo": "https://cristina-huddles.netlify.app/"
#         }    
#     if destination in destinations:       
#         return redirect(destinations[destination])    
#     else:        
#         return "Invalid destination", 400
    

# @app.route("/projects")
# def projects():    
#     return redirect(url_for('index', _anchor="projects"))
# @app.route("/contacts")
# def contacts():    
#     return redirect(url_for('index', _anchor="contacts"))


# @app.route('/linkedin')
# def linkedin():
#     return redirect("https://www.linkedin.com/in/cristina-deviza-704375271/", code=302)

# @app.route('/github')
# def github():
#     return redirect("https://github.com/cristinadeviza", code=302)



# if __name__ == '__main__':
#     app.run(debug=True)
