from flask import Flask,jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def get_details():
    return jsonify({
        "hostname": socket.gethostname(),
        "current_time": datetime.datetime.utcnow().isoformat() + "Z"
    })

@app.route('/api/v1/healthz')
def get_health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == '__main__':  
    app.run(host='0.0.0.0')