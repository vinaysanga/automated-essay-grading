from grader import gradeMe
from flask import Flask, render_template, request

app = Flask(__name__)
# Views for pages
@app.route('/')
def essays():
    essayList = []
    with open("st.csv") as f:
        for line in f:
            essayList.append(line.strip().split('\t'))
    return render_template('essays.html', essayList = essayList)

@app.route('/<eid>')
def essayRoute(eid):
    filename = f'{eid}.html'
    return render_template('eid.html', eid = eid, filename = filename)


@app.route('/grade', methods = ['GET', 'POST'])
def grade():
    username = request.form['username']
    textArea = request.form['textArea']
    grade = gradeMe(textArea)
    print(f'The grade is {grade}')
    return render_template('grade.html', username=username, score=grade)

if __name__ == '__main__':
    app.run(debug=True)
