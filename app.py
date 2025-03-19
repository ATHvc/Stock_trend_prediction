from flask import Flask, render_template, request
import numpy as np
from scipy.stats import norm

app = Flask(__name__)

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    return price

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        S = float(request.form['S'])
        K = float(request.form['K'])
        T = float(request.form['T'])
        r = float(request.form['r']) / 100
        sigma = float(request.form['sigma']) / 100
        option_type = request.form['option_type']
        price = black_scholes(S, K, T, r, sigma, option_type)
        return render_template('index.html', price=price)
    return render_template('index.html', price=None)

if __name__ == '__main__':
    app.run(debug=True)
    