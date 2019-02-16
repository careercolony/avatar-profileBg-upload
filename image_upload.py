from flask import Flask, request, jsonify
import shutil
import os

#import nude
#from nude import Nude
from nudity import Nudity

def is_nude(fileName):

    nudity = Nudity();
    nude_ret = nudity.has(fileName)
    # gives you True or False

    #print(nudity.score(fileName))

    return nude_ret
    # gives you nudity score 0 - 1

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def upload_file():
    res = {}

    if 'image' in request.files and 'memberID' in request.form :
        file = request.files['image']
        filename = request.form['memberID'] + ".jpg"
    else:
        if not 'image' in request.files :res["error"] = "No Image"
        if not 'memberID' in request.form :res["error"] = "No user ID provided"
        return jsonify({"data": res})

    filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)


    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    temp_file = os.path.join(app.config['UPLOAD_FOLDER'], "temp.jpg")
    file.save(temp_file)

    # check nudity validation
    if is_nude(temp_file):
        res["msg"] = "Nude_Image"
    else:
        res["msg"] = "Valid_Image"
        shutil.copy(temp_file,filename)

    os.remove(temp_file)

    return jsonify({"data": res})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001', debug=True)