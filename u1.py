from flask import Flask, request, redirect, render_template
import string
import random
app = Flask(__name__)

# In-memory storage for URLs
url_mapping = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    if short_url in url_mapping:
        return generate_short_url()
    return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_url = generate_short_url()
        url_mapping[short_url] = original_url
        # return render_template('index.html', short_url=short_url, host=request.host_url)
        return render_template('index.html', short_url=short_url, host=request.host_url)
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    original_url = url_mapping.get(short_url)
    if original_url:
        return redirect(original_url)
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
