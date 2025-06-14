from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML UI
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Personal LLM Assistant</title>
</head>
<body>
    <h2>🧠 Personal LLM Assistant</h2>
    <form method="POST">
        <input type="text" name="prompt" placeholder="What do you want help with?" style="width:400px;" required>
        <button type="submit">Ask</button>
    </form>
    {% if response %}
        <div style="margin-top:20px;">
            <strong>📬 Assistant Response:</strong>
            <p>{{ response.replace('\\n', '<br>')|safe }}</p>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        prompt = request.form.get("prompt", "").lower()

        if "summarize my emails" in prompt:
            response = (
                "📬 Here's a summary of your emails from June 3:\n"
                "1. Prof. Chen confirmed your research meeting (Friday 2 PM). ✅ No reply needed.\n"
                "2. Lockheed Martin followed up about your internship — deadline Thursday. ⏰ Reply recommended.\n"
                "3. Penn State University Library sent an overdue notice (due May 31st). ⚠️ Consider renewing.\n"
                "4. Mom sent a grocery list for the weekend — she wants you to pick up almond milk, eggs, and avocados. 🛒 Optional.\n"
                "5. Amazon confirmed your textbook delivery — arriving by Wednesday. 📦 No action needed.\n\n"
                "✅ You have 1 urgent email to respond to (Lockheed Martin)."
            )
        else:
            response = f"Simulated response to: '{prompt}'"

    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)
