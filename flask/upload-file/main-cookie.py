from flask import Flask, request, redirect, make_response, render_template_string


app = Flask(__name__)


@app.route("/")
def index():

    cookies_filename = request.cookies.get('filename', '')
    
    return render_template_string('''
Previous filename: {{ filename }}
<hr>
<form action="getfile" method="POST" enctype="multipart/form-data">
    Project file path: <input type="file" name="config_file"><br>
    <input type="submit" value="Submit">
</form>
''', filename=cookies_filename)


@app.route('/getfile', methods=['GET','POST'])
def getfile():
    #print('args:', request.args)
    #print('form:', request.form)
    #print('files:', request.files)

    response = make_response(redirect('/'))
    
    result = request.files.get('config_file')
    
    if result:
        result.save(result.filename) # TODO: save with unique name which couldn't overwrite file with passwords 
        response.set_cookie('filename', result.filename)

    return response

    
app.run()    
