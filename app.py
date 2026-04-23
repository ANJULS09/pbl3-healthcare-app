from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>SOA University Healthcare Portal</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #e9ecef; padding: 40px; }
            .container { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); max-width: 800px; margin: auto; border-top: 12px solid #0056b3; }
            h1 { color: #0056b3; border-bottom: 2px solid #eee; padding-bottom: 15px; }
            .info-bar { background: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 25px; color: #333; line-height: 1.6; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { border: 1px solid #dee2e6; padding: 12px; text-align: left; }
            th { background-color: #0056b3; color: white; }
            tr:nth-child(even) { background-color: #f2f2f2; }
            .badge { background: #28a745; color: white; padding: 5px 10px; border-radius: 50px; font-size: 0.85em; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Patient Records Management System</h1>
            <div class="info-bar">
                <strong>Project Lead:</strong> Anjul Shukla<br>
                <strong>Affiliation:</strong> Siksha ‘O’ Anusandhan (SOA) University<br>
                <strong>System Status:</strong> <span class="badge">K8S CLUSTER ONLINE</span>
            </div>
            <h3>Recent Appointments</h3>
            <table>
                <thead>
                    <tr><th>Patient ID</th><th>Name</th><th>Department</th><th>Status</th></tr>
                </thead>
                <tbody>
                    <tr><td>#SOA-001</td><td>Anjul Shukla</td><td>DevOps & Cloud</td><td>Confirmed</td></tr>
                    <tr><td>#SOA-002</td><td>Gaur Gopal Das</td><td>Counseling</td><td>Scheduled</td></tr>
                    <tr><td>#SOA-003</td><td>John Smith</td><td>Emergency</td><td>Under Review</td></tr>
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
