from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/v1.0/<tenant_id>/activity/feed/subscriptions/start", methods=["POST"])
def start_subscription(tenant_id):
    return "", 200  # Fake success

@app.route("/api/v1.0/<tenant_id>/activity/feed/subscriptions/content", methods=["GET"])
def get_content(tenant_id):
    # Simulate FAZ polling for content
    content = [
        {
            "contentUri": f"https://mockserver.local/content/{tenant_id}/log1.json",
            "contentType": "Audit.Exchange",
            "contentId": "12345"
        }
    ]
    return jsonify(content)

@app.route("/content/<tenant_id>/log1.json", methods=["GET"])
def get_log(tenant_id):
    # Simulated log content (can be randomized or static)
    log_data = [
        {
            "CreationTime": "2025-06-09T15:04:00",
            "Operation": "UserLoggedIn",
            "OrganizationId": tenant_id,
            "RecordType": 1,
            "UserType": 0,
            "Workload": "Exchange",
            "UserId": "testuser@yourdomain.com",
            "ClientIP": "123.123.123.123"
        }
    ]
    return jsonify(log_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context="adhoc")
