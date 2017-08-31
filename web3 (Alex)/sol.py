from requests import session
from time import sleep

bot = session()

for _ in range(1000):
    n,prob = bot.get('http://127.0.0.1:5000/').text.split()[:2]
    print(n, prob)
    if n > 99:
        break
    sol = eval(prob)
    bot.post('http://127.0.0.1:5000/check', data=dict(solution=sol))
    sleep(0.2)
