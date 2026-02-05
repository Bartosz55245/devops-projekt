from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
cache = Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    try:
        visits = cache.incr('counter')
    except Exception as e:
        return f"Aplikacja działa, ale brak połączenia z bazą Redis.<br>Błąd: {e}"
        
    return f"<h1>Witaj w moim projekcie DevOps!</h1>" \
           f"<p>To jest aplikacja w kontenerze.</p>" \
           f"<p>Liczba odwiedzin w bazie: <b>{visits}</b></p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)