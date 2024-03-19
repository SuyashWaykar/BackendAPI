from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def sayHello():
    return(f'Hello User')

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=80)




