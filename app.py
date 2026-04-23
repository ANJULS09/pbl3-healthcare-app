from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Healthcare Patient Portal</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f4f7f6; }
            .header { background: #007bff; color: white; padding: 20px; text-align: center; border-radius: 8px; }
            .card { background: white; padding: 20px; margin-top: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            table { width: 100%; border-collapse: collapse; margin-top: 15px; }
            th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
            th { background-color: #f2f2f2; }
            .status-tag { background: #28a745; color: white; padding: 4px 8px; border-radius: 4px; font-size: 0.8em; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Healthcare Patient Dashboard v2.0</h1>
            <p>SOA University Medical Center - Managed by Anjul Shukla</p>
        </div>

        <div class="card">
            <h2>System Information</h2>
            <p><strong>Deployment Environment:</strong> Kubernetes (Minikube)</p>
            <p><strong>CI/CD Tool:</strong> Jenkins Automation Server</p>
            <p><strong>Status:</strong> <span class="status-tag">ACTIVE</span></p>
        </div>

        <div class="card">
            <h2>Recent Patient Records</h2>
            <table>
                <tr><th>Patient ID</th><th>Name</th><th>Visit Reason</th><th>Status</th></tr>
                <tr><td>#9821</td><td>John Doe</td><td>General Checkup</td><td>Completed</td></tr>
                <tr><td>#9822</td><td>Jane Smith</td><td>Cardiology</td><td>Pending</td></tr>
                <tr><td>#9823</td><td>Robert Brown</td><td>Dermatology</td><td>In Progress</td></tr>
            </table>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>Healthcare Patient Dashboard v1.0</h1><p>Status: All Systems Secure.</p>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
