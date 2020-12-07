from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route("/")          # The "@" decorator associates this route with the function immediately following
def hello_world():
    print ("You are on the main page")
    return 'Hello World!!'  # Return the string 'Hello World!' as a response

@app.route("/dojo")
def hello_dojo():
    print ("you are on the dojo route")
    return "Dojo!"

# import statements, maybe some other routes
    
@app.route("/<name>")
def hello(name):
    print("The name route is where you are now!")
    return f"Sup, {name}"

@app.route("/repeat/<number>/<words>")
def repeat(number, words):
    print("You're in the repeat route")
    return f"Hello, {words*int(number)}"   #WOO FINALLY WORKS


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
