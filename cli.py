from bs_model import bs_call_price, bs_put_price

def prompt_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

def main():
    print("Black–Scholes European Option Pricer")
    S = prompt_float("Stock price (S): ")
    K = prompt_float("Strike price (K): ")
    T = prompt_float("Time to maturity (years): ")
    r = prompt_float("Risk-free Interest rate (decimal): ")
    σ = prompt_float("Volatility (σ, decimal): ")

    call = bs_call_price(S, K, T, r, σ)
    put  = bs_put_price(S, K, T, r, σ)

    print(f"\nCall price: ${call:.2f}")
    print(f"Put price:  ${put:.2f}")

if __name__ == "__main__":
    main()
