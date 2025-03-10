from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open("match_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"data": []}  # Fix: Access `data` instead of `matches`

    # Debugging: Print full JSON data
    print("DEBUG: Full JSON Data Loaded ->", data)

    # Extract match data correctly
    match_list = data.get("data", [])  # Correct key for match list

    # Filter only India's matches
    india_matches = [
        match for match in match_list
        if "India" in match.get("teams", [])
    ]

    # Debugging: Print filtered India matches
    print("DEBUG: India Matches Found ->", india_matches)

    # Get latest India match
    latest_match = india_matches[-1] if india_matches else None
    india_won = latest_match and "India won" in latest_match.get("status", "")

    return render_template("index.html", match=latest_match, india_won=india_won)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
