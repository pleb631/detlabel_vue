from flask import Flask, request,jsonify
from flask_cors import CORS
import glob
import os
import base64


app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome backend!'

@app.route('/api/getFiles/<path:base_path>', methods=['GET'])
def getFiles(base_path):  # put application's code here
    if not os.path.exists(base_path):
        return jsonify({"code":200,"paths":[],'lenght':0,"base_path":base_path})
    elif os.path.isfile(base_path):
        if os.path.splitext(base_path)[1] in ['.jpg','.png']:
            return jsonify({"code":200,"paths":[base_path],'lenght':1,"base_path":os.path.dirname(base_path)})
        else:
            return jsonify({"code":200,"paths":[],'lenght':0})
        
    elif os.path.isdir(base_path):

        img_list = glob.glob(os.path.join(base_path,"**/*.jpg"),recursive=True)+glob.glob(os.path.join(base_path,"**/*.png"),recursive=True)
        img_list = [os.path.relpath(i,base_path) for i in img_list]
        img_list = sorted(img_list)
        return jsonify({"code":200,"paths":img_list,'lenght':len(img_list),"base_path":base_path})
    else:
        return jsonify({"code":200,"paths":[],'lenght':0})
    

def encode_base64(file):
    with open(file,'rb') as f:
        base64_data = base64.b64encode(f.read()).decode("utf-8")

        # 如果想要在浏览器上访问base64格式图片，需要在前面加上：data:image/jpeg;base64,
        base64_str = "data:image/jpeg;base64,"+str(base64_data)

        return base64_str

@app.route('/api/getImg/<path:img_path>', methods=['GET'])
def getImg(img_path):
    if os.path.exists(img_path):
        try:
            base64_data = encode_base64(img_path)
            return jsonify({"code": 200, "base64_data": base64_data})
        except Exception as e:
            return jsonify({"code": 500, "message": str(e)})
    else:
        return jsonify({"code": 404, "base64_data": None, "message": "Image not found"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)