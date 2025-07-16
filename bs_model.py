import numpy as np
from scipy.stats import norm

def bs_call_price(S: float, K: float, T: float, r: float, σ: float) -> float:
    """
    European call price under Black–Scholes (q=0).
    S: stock price
    K: strike price
    T: time to expiry in years
    r: continuous annual risk-free rate
    σ: volatility (annual std. dev.)
    """
    #compute d1 and d2
    d1 = (np.log(S/K) + (r + 0.5 * σ**2) * T) / (σ * np.sqrt(T))
    d2 = d1 - σ * np.sqrt(T)

    #compute call price: S * N(d1) – K * e^(–rT) * N(d2)
    call = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call

def bs_put_price(S: float, K: float, T: float, r: float, σ: float) -> float:

    #European put price via put–call parity or direct formula.

    # put = call + K e^(–rT) – S
    call = bs_call_price(S, K, T, r, σ)
    put = call + K * np.exp(-r * T) - S
    return put
