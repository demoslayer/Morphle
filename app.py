from flask import Flask, render_template_string
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>HTOP Information</title>
    <style>
        body { font-family: monospace; padding: 20px; }
        pre { background: #f0f0f0; padding: 10px; }
    </style>
</head>
<body>
    <h2>System Information</h2>
    <p><strong>Name:</strong> {{name}}</p>
    <p><strong>Username:</strong> {{username}}</p>
    <p><strong>Server Time (IST):</strong> {{server_time}}</p>
    <h3>Top Output:</h3>
    <pre>{{top_output}}</pre>
</body>
</html>
"""

@app.route('/htop')
def htop():
    # Get username
    username = subprocess.getoutput('whoami')
    
    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Get top output
    top_output = subprocess.getoutput('top -b -n 1')
    
    return render_template_string(HTML_TEMPLATE,
        name="Byas Yadav",
        username=username,
        server_time=server_time,
        top_output=top_output
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)