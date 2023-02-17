from flask import Flask, render_template, redirect, request

app = Flask('__name__')
lst = []
l = [int(i) for i in range(len(lst))]
d = {}
for i in l:
    if i not in d:
        d[i] = lst[i]
        print(d)
'''
@app.route('/', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        task_content = request.form['task']
        # task_content = request.form.get('task')
        lst.append(task_content)
        return redirect('/')
    else:
        return render_template("demo.html", lst=lst)
'''


@app.post('/')
def add():
    task_content = request.form['task']
    # task_content = request.form.get('task')
    lst.append(task_content)
    return redirect('/')


@app.get('/')
def display():
    return render_template("demo.html", lst=lst)


@app.route('/delete/<string:content>')
def remove(content):
    lst.remove(content)
    return redirect('/')


if __name__ == '__main__':
    lst.clear()
    app.run(debug=True, port=5004)
