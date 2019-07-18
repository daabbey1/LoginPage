from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/addcss')
def index():
    return 'Hello world'

@app.route('/whereami')
def whereami():
    return 'Ghana!'

@app.route('/FreeStyle')
def addMoreFunctions():
    return 'Let the coding Begin!'

@app.route('/')
def addcss():
    return render_template('myIndex.html')
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')