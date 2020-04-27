from timeit import default_timer
import requests

def load_data(delay):
    print(f'Starting {delay} second timer')
    text = requests.get(f'http://httpbin.org/delay/{delay}').text
    print(f'Completed {delay} second timer')

def run_demo():
    start_time = default_timer()

    two_data = load_data(2)
    three_data = load_data(3)

    elapsed_time = default_timer() - start_time
    print(f'The operation took {elapsed_time:.2} seconds')

def main():
    run_demo()

main()
