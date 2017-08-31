from flask import Flask, session, redirect, url_for, request
app = Flask(__name__)
app.secret_key = 'hBBXdDqOzmtiBmDX9I3Rehdx4tOGpAQSDZUVxbn6'

from random import randint, choice

FLAG = 'FLAG{why_n0t_@ut0m@t3_1t}'

def gen_problem():
    n = 10
    op = ['+', '+', '*']
    nums = [str(randint(1,100)) for _ in range(n)]
    ops = [choice(op) for _ in range(n-1)]
    
    result = []
    result.append(nums[0])
    for i in range(n-1):
        result.append(ops[i])
        result.append(nums[i+1])
    return ''.join(result)

def bad():
    session['count'] = 0

def good():
    session['count'] += 1

html = ('<h1>You solved {} problems<h1><br>'
        'Solve this: {}'
        '<form action="/check" method=post>'
        '<input type=text name=solution>'
        '<input type=submit value=GO>'
        '</form>')

@app.route('/')
def index():
    if 'count' not in session:
        bad()
    prob = gen_problem()
    session['task'] = prob
    count = session.get('count', None)
    if count < 100:
        return html.format(count, prob)
    else:
        #bad()
        return html.format(count, FLAG)

@app.route('/check', methods = ['POST'])
def check():
    rval = redirect(url_for('index'))
    if not hasattr(request, 'form'):
        bad()
        return rval
    solution = request.form.get('solution', None)
    if not solution:
        bad()
        return rval
    try:
        solution = int(solution)
    except ValueError:
        bad()
        return rval
    prob = session.get('task', None)
    if not prob:
        bad()
        return rval
    my_sol = eval(prob)
    if my_sol == solution:
        good()
    else:
        bad()
    return rval
