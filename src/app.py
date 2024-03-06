from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            return "Failed to retrieve public IP"
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/get_public_ip')
def get_public_ip_route():
    public_ip = get_public_ip()
    return jsonify({'ip': public_ip})

@app.route('/reversed_public_ip')
def reversed_public_ip_route():
    public_ip = get_public_ip()
    reverse_public_ip = '.'.join(public_ip.split('.')[::-1]) # Corrected variable name
    return jsonify({'rIPv4': reverse_public_ip})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)
