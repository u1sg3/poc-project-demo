from flask import Flask, request, render_template_string

app = Flask(__name__)

# Dummy tasks
tasks = {
    "in_progress": [
    ],
    "completed": [
    ]
}

template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Task Assistant</title>
    <style>
        body {
            font-family: sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            height: 100vh;
        }
        .sidebar {
            width: 250px;
            background-color: #f4f4f4;
            padding: 20px;
            overflow-y: auto;
        }
        .main {
            flex: 1;
            padding: 40px;
            background-color: #fafafa;
        }
        .input-box {
            width: 100%;
            padding: 15px;
            font-size: 16px;
        }
        .submit-btn {
            padding: 10px 20px;
            font-size: 16px;
            margin-left: 10px;
        }
        .task-section {
            margin-bottom: 30px;
        }
        .quick-tasks {
            display: flex;
            gap: 20px;
            margin-top: 40px;
        }
        .task-card {
            border: 1px solid #ccc;
            padding: 20px;
            width: 200px;
            border-radius: 8px;
            background-color: #fff;
        }
    </style>
</head>
<body>
    <div class="main">
        <h2>How can I help?</h2>
        <form method="POST">
            <input name="command" class="input-box" placeholder="Type a command..." autofocus>
            <button type="submit" class="submit-btn">Send</button>
        </form>
        {% if command %}
            <p><strong>You typed:</strong> {{ command }}</p>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    command = ""
    if request.method == 'POST':
        command = request.form.get('command', '')
    return render_template_string(template, tasks=tasks, command=command)

if __name__ == '__main__':
    app.run(debug=True)