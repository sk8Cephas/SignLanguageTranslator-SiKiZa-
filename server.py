from flask import Flask,render_template 

sikiza = Flask(__name__)  # initialize sikiza


@sikiza.route('/')
def Intro_Page():
    return render_template('index.html')

@sikiza.route('/new_api')
def new_api():
    return render_template('api_request.html')



@sikiza.route('/home')
def Home_Page():
    return render_template('home.html')





if __name__ == '__main__':
    sikiza.run(debug=True)