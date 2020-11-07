from flask import Flask, render_template, request, jsonify
import query_on_whoosh
import smtplib
import config
import math 

app = Flask(__name__)
app.config.update(dict(JSONIFY_PRETTYPRINT_REGULAR=True))

@app.route("/")
def handle_slash():
    requested_name = request.args.get("name")
    return render_template("index.html",user_name=requested_name)

@app.route("/query", strict_slashes=False)
def handle_query():
    query_term = request.args.get("q")
    query_page = int(request.args.get("p"))
    return jsonify({"query_term": query_term, "search_results": query_on_whoosh.query(query_term, 10, query_page)})

@app.route("/query_view", strict_slashes=False)
def handle_query_view():
    query_term = request.args.get("q")
    if not query_term:
        query_term = ""

    page_index_arg = request.args.get("p")
    if not page_index_arg:
        page_index_arg = '1'

    query_page = int(page_index_arg)
    query_results = query_on_whoosh.query(query_term, current_page=query_page)
    search_results = query_results[0] # returns a page of the search results
    results_cnt = int(query_results[1]) # returns a total number of the search results
    page_cnt = math.ceil( results_cnt / 10 )
    return render_template("query.html", 
                            results = search_results, 
                            page_cnt = page_cnt,
                            query_term = query_term)

@app.route("/about", strict_slashes=False)
def handle_about():
    return render_template("about.html")

@app.route("/success", strict_slashes=False)
def handle_request():
    new_data = request.args.get("new_data")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("ddaloisi@emich.edu", config.gmail_password)
    message = 'Subject: {}\n\n{}'.format("Request to add new data", "request to add: " + topic)
    server.sendmail("ddaloisi@emich.edu", "ddaloisi@emich.edu", + message)
    return render_template("success.html", new_data=new_data)