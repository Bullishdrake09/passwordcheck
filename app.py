from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

# Serve the index.html file
@app.route('/')
def serve_index():
    return render_template('index.html')

# Serve rockyou.txt (ensures it's accessible by fetch requests)
@app.route('/rockyou.txt')
def serve_rockyou():
    return send_from_directory('.', 'rockyou.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
