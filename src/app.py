from flask import Flask, jsonify, render_template
import requests
import time

app = Flask(__name__)
public_ip_buffer = None

def get_public_ip():
    global public_ip_buffer
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            public_ip_buffer = response.text
            return public_ip_buffer
        else:
            return "Failed to retrieve public IP"
    except Exception as e:
        return "An error occurred: {e}"

@app.route('/get_public_ip')
def get_public_ip_route():
    public_ip = get_public_ip()
    return jsonify({'ip': public_ip})

@app.route('/reversed_public_ip')
def reversed_public_ip_route():
    global public_ip_buffer
    if public_ip_buffer is None:
        get_public_ip()  # Fetch public IP if buffer is empty
    time.sleep(2)
    reverse_public_ip = public_ip_buffer[::-1]
    return jsonify({'rIPv4': reverse_public_ip})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)
