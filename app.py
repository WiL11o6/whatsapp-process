from flask import Flask, render_template, request, redirect, url_for
from text_processing import process_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        text_data = file.read().decode('utf-8')
        processed_data = process_text(text_data)
        return render_template('results.html', table_data=processed_data.to_html(classes='table table-striped'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
