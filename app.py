# from flask import Flask, request, jsonify, render_template
# from pymongo import MongoClient
# from datetime import datetime
# from urllib.parse import quote_plus

# app = Flask(__name__)

# # --- MongoDB Setup ---
# username = "harshalkamble"
# raw_password = "Harshal@12"
# password = quote_plus(raw_password)

# uri = f"mongodb+srv://{username}:{password}@assesmentcluster.tktojdj.mongodb.net/?retryWrites=true&w=majority&appName=AssesmentCluster"
# client = MongoClient(uri)
# db = client.githubWebhooks

# # --- Routes ---

# @app.route('/webhook', methods=['POST'])
# def github_webhook():
#     event_type = request.headers.get('X-GitHub-Event')
#     payload = request.json

#     doc = {"event_type": event_type, "timestamp": datetime.utcnow()}

#     if event_type == "push":
#         doc.update({
#             "author": payload["pusher"]["name"],
#             "to_branch": payload["ref"].split("/")[-1]
#         })

#     elif event_type == "pull_request":
#         pr = payload["pull_request"]
#         doc.update({
#             "author": pr["user"]["login"],
#             "from_branch": pr["head"]["ref"],
#             "to_branch": pr["base"]["ref"]
#         })
#         if pr.get("merged"):
#             doc["event_type"] = "merge"

#     db.events.insert_one(doc)
#     return jsonify({"status": "received"}), 200


# @app.route('/events', methods=['GET'])
# def get_events():
#     events = list(db.events.find().sort("timestamp", -1).limit(10))
#     for e in events:
#         e["_id"] = str(e["_id"])
#     return jsonify(events)


# @app.route('/')
# def home():
#     return render_template("index.html")


# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
from urllib.parse import quote_plus

app = Flask(__name__)

# --- MongoDB Setup ---
username = "harshalkamble"
raw_password = "Harshal@12"  # Use your real password here
password = quote_plus(raw_password)

uri = f"mongodb+srv://{username}:{password}@assesmentcluster.tktojdj.mongodb.net/?retryWrites=true&w=majority&appName=AssesmentCluster"
client = MongoClient(uri)
db = client.githubWebhooks  # Database name
collection = db.events       # Collection name

# --- Routes ---

@app.route('/webhook', methods=['POST'])
def github_webhook():
    event_type = request.headers.get('X-GitHub-Event')
    payload = request.json

    doc = {
        "event_type": event_type,
        "timestamp": datetime.utcnow()
    }

    if event_type == "push":
        doc.update({
            "author": payload["pusher"]["name"],
            "to_branch": payload["ref"].split("/")[-1]
        })

    elif event_type == "pull_request":
        action = payload.get("action")
        pr = payload["pull_request"]

        doc.update({
            "author": pr["user"]["login"],
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"]
        })

        if action == "closed" and pr.get("merged"):
            doc["event_type"] = "merge"
        else:
            doc["event_type"] = "pull_request"

    # Save to MongoDB
    collection.insert_one(doc)
    return jsonify({"status": "received"}), 200


@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find().sort("timestamp", -1).limit(10))
    for event in events:
        event["_id"] = str(event["_id"])
    return jsonify(events)


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
