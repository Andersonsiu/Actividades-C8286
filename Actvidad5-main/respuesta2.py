import time
from flask import Flask, jsonify
import logging

app = Flask(__name__)


logging.basicConfig(filename='circuit_breaker.log', level=logging.INFO)

def record_failure(self):
    self.failures += 1
    self.last_failure_time = time.time()
    if self.failures >= self.fail_threshold:
        self.state = "open"
        logging.info(f'Circuit opened at {self.last_failure_time}')

class CircuitBreaker:
    def __init__(self, fail_threshold=3, reset_timeout=10):
        self.fail_threshold = fail_threshold
        self.reset_timeout = reset_timeout
        self.failures = 0
        self.last_failure_time = None
        self.state = "closed"
    
    def call(self, func, *args, **kwargs):
        if self.state == "open":
            if time.time() - self.last_failure_time > self.reset_timeout:
                self.state = "half-open"
            else:
                raise Exception("Circuit is open. Calls are not allowed.")
        
        try:
            result = func(*args, **kwargs)
            self.reset()
            return result
        except Exception as e:
            self.record_failure()
            raise e

    def record_failure(self):
        self.failures += 1
        self.last_failure_time = time.time()
        if self.failures >= self.fail_threshold:
            self.state = "open"

    def reset(self):
        self.failures = 0
        self.state = "closed"

failure_count = 0

def unreliable_service():
    global failure_count
    failure_count += 1
    if failure_count > 5:  # Garantiza un éxito después de 5 fallos
        failure_count = 0
        return "Service response"
    raise Exception("Service failure.")


breaker = CircuitBreaker(fail_threshold=3, reset_timeout=30)  # Incrementa o disminuye el timeout

@app.route('/')
def index():
    try:
        # Make a call through the circuit breaker
        response = breaker.call(unreliable_service)
        return jsonify({'response': response, 'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'service unavailable'})

if __name__ == '__main__':
    app.run(port=5005)
