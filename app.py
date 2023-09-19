from flask import Flask , request , jsonify


app= Flask(__name__)

nums=[10,20,30]
@app.route('/')
def helo_world():
    return "Hello world"

@app.route("/evenodd<int:num>")
def evenodd(num):
    status=None
    if num%2==0:
        status='Even'
    else:
        status='Odd'
    
    return jsonify({'status':status})

@app.route("/addnum", methods=['POST'])
def addnum():
    request_data=request.get_json()
    print(request_data['num'])
    nums.append(request_data['num'])
@app.route("/showlist")
def show():
    return jsonify({'list':nums})

if __name__=="__main__":
    app.run(debug=True)


