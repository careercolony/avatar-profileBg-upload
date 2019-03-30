from flask import Flask, request, jsonify
import shutil
import os
from db import database
import datetime

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

UPLOAD_FOLDER = 'media/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/avatar', methods=['POST'])
def avatar():
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
        res["msg"] = "Nude photo not allowed"
    else:
        #res["msg"] = "Valid_Image"
        shutil.copy(temp_file,filename)
        file = request.files['image']
        filename = request.form['memberID'] + ".jpg"
            
        avatar = '/media/images/av-' +filename
        res["msg"] = "Profile picture uploaded successfully"
        
        memberID = request.form['memberID']
        database['users'].update({'_id': memberID}, {"$set": {'avatar':avatar}})

    os.remove(temp_file)

    return jsonify({"data": res})

@app.route('/profile_bg', methods=['POST'])
def profile_bg():
    res = {}

    if 'image' in request.files and 'memberID' in request.form :
        file = request.files['image']
        filename = request.form['memberID'] + ".jpg"
        res["msg"] = "Profile picture uploaded successfully"
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
        res["msg"] = "Nude photo not allowed"
    else:
        #res["msg"] = "Valid_Image"
        shutil.copy(temp_file,filename)
        file = request.files['image']
        filename = request.form['memberID'] + ".jpg"
            
        profile_bg = '/media/images/pf-' +filename
        res["msg"] = "Profile picture uploaded successfully"
        
        memberID = request.form['memberID']
        database['users'].update({'_id': memberID}, {"$set": {'profile_bg':profile_bg}})

    os.remove(temp_file)

    return jsonify({"data": res})



if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001', debug=True)


