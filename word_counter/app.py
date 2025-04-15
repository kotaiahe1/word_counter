from flask import Flask, render_template, request

app = Flask(__name__)

def count_words(text):
    words = text.strip().split()
    return len(words)

@app.route('/', methods=['GET', 'POST'])
def index():
    word_count = None
    error = None

    if request.method == 'POST':
        user_input = request.form.get('text')

        if user_input.strip() == "":
            error = "Please enter some text."
        else:
            word_count = count_words(user_input)

    return render_template('index.html', word_count=word_count, error=error)

if __name__ == '__main__':
    app.run(debug=True)
