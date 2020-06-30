import os
from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = os.path.dirname(__file__)

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = 'to_be_tested.py'
        f.save(BASE_DIR + f'/uploads/{filename}')
        os.system(f'python {BASE_DIR}/uploads/testing.py')
        try:
            with open('test_result.txt', 'r') as fread:
                lines = [line.strip().split(':') for line in fread.readlines()]
                score = 0
                for test, result in lines:
                    if result == 'Pass':
                        score += 1
        except:
            score = 0
            lines = []
        return render_template('result.html', score = score, num_test = len(lines))

    else:
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='5000')