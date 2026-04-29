from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (for demo)
jobs = [
    {"id": 1, "title": "Software Engineer", "status": "applied"},
    {"id": 2, "title": "DevOps Engineer", "status": "interview"}
]

@app.route('/')
def home():
    return "Version 2 🚀"

@app.route('/health', methods=['GET'])
def health():
    return "Webhook Working 🚀"

@app.route('/jobs', methods=['GET'])
def get_jobs():
    return jsonify({"jobs": jobs})

@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = next((j for j in jobs if j["id"] == job_id), None)
    if job:
        return jsonify(job)
    return jsonify({"error": "Job not found"}), 404

@app.route('/jobs', methods=['POST'])
def create_job():
    data = request.get_json()
    new_job = {
        "id": len(jobs) + 1,
        "title": data["title"],
        "status": data.get("status", "applied")
    }
    jobs.append(new_job)
    return jsonify(new_job), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
