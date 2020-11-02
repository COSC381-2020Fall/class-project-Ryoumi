from flask import Flask, render_template, request, jsonify
import query_on_whoosh

app = Flask(__name__)
app.config.update(dict(JSONIFY_PRETTYPRINT_REGULAR=True))

@app.route("/")
def handle_slash():
    requested_name = request.args.get("name")
    return render_template("index.html",user_name=requested_name)

@app.route("/query", strict_slashes=False)
def handle_query():
    query_term = request.args.get("q")
    return jsonify({"query_term": query_term, "search_results": query_on_whoosh.query(query_term)})