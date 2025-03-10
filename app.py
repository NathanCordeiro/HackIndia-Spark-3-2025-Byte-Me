from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Define airports and flight times as a meTTa program
metta_program = """
    (:- (flight DEL BOM 130))
    (:- (flight DEL BLR 150))
    (:- (flight DEL HYD 135))
    (:- (flight BOM MAA 120))
    (:- (flight BOM BLR 90))
    (:- (flight BLR HYD 75))
    (:- (flight MAA CCU 140))
    (:- (flight CCU HYD 150))
    (:- (flight HYD PNQ 90))
    (:- (flight PNQ AMD 70))
    (:- (flight AMD COK 120))
    (:- (flight COK GOI 110))
    (:- (flight GOI JAI 140))
    (:- (flight JAI LKO 90))
    (:- (flight LKO BBI 130))
    (:- (flight BBI IXC 150))
    (:- (flight IXC TRV 160))
    (:- (flight TRV VGA 100))
    (:- (flight VGA IXB 140))
    (:- (flight IXB GWL 120))
    (:- (flight GWL IXR 90))
    (:- (flight IXR UDR 110))
    (:- (flight UDR DEL 130))

    (defrule (path X Y Time) (flight X Y Time))
    (defrule (path X Y Time) 
        (flight X Z T1) 
        (path Z Y T2) 
        (+ T1 T2 Time))

    (defrule (shortest_path X Y BestPath BestTime) 
        (collect Path Time (path X Y Time))
        (min Time BestTime)
        (find Path BestTime BestPath))
"""


def query_metta(source, destination):
    query = f"(shortest_path {source} {destination} ?path ?time)"
    try:
        result = subprocess.run(
            ["metta"],
            input=metta_program + "\n" + query,
            text=True,
            capture_output=True
        )
        output = result.stdout.strip()
        if "?path" in output or "?time" in output:
            return None
        return parse_metta_output(output)
    except Exception as e:
        return None

def parse_metta_output(output):
    lines = output.split("\n")
    path = []
    time = 0
    for line in lines:
        if line.startswith("("):
            parts = line.strip("()").split()
            if parts[0] == "shortest_path":
                path = parts[2:-1]
                time = int(parts[-1])
    return {"path": path, "travel_time": time}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/find_route", methods=["POST"])
def find_route():
    data = request.json
    source = data.get("source")
    destination = data.get("destination")
    
    result = query_metta(source, destination)
    if not result:
        return jsonify({"error": "No available route!"}), 404
    
    return jsonify(result) 

if __name__ == "__main__":
    app.run(debug=True)
