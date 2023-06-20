from flask import Flask, render_template, request, send_file, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

   return render_template('example1.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=9000)
  