from py_vollib.black_scholes import black_scholes as bs
from py_vollib.black_scholes.greeks.analytical import vega

def main():
    # Get the input from the user
    option_type, S, K, r, t, mkt_price = get_input()

    # Calculate implied volatility using the input parameters
    implied_volatility = calculate_implied_volatility(S, K, r, t, mkt_price, option_type)

    #Print the result
    print(f"Implied Volatility: {implied_volatility}%")

def calculate_implied_volatility(S, K, t, r, mkt_price, option_type, tol=0.00001):
    '''
    Implied volatility is the market's forecast of a likely movement in a security's price.
    It is a metric used by investors to estimate future fluctuations (volatility) of a security's price based on certain predictive factors.
    S = Current stock price
    K = Strike price
    t = Time to maturity (in years)
    r = Risk-free interest rate
    mkt_price = Market price of the option
    option_type = 'c' for call option, 'p' for put option
    tol = Tolerance level for convergence in the iterative process (default is 0.00001)
    '''
    # Set initial parameters for the iterative profess
    num_iter = 1000  # Max number of iterations
    vol_guess = 0.3  # Initial guess of implied volatility

    # Iteratively update implied volatility using the Black-Scholes formula and vega
    for i in range(num_iter):
        bs_price = bs(option_type, S, K, t, r, vol_guess)
        vega_calc = vega(option_type, S, K, t, r, vol_guess)*100 # Calculate vega, which represents the sensitivity of the option price to changes in implied volatility
        vol_new = vol_guess - (bs_price - mkt_price) / vega_calc
        new_bs_price = bs(option_type, S, K, t, r, vol_new)

        # Check for convergence based on tolerance
        if (abs(vol_guess - vol_new) < tol or abs(new_bs_price - mkt_price) < tol):
            break

        # Update the guess for the next iteration
        vol_guess = vol_new

    # Return the implied volatility in percentage form
    return vol_new * 100

def get_input():
    '''
    Gets the input from a user.
    '''
    while True:
        try:
            # Get option type (call or put), stock price, strike price, time to maturity, risk-free interest rate, and market price
            option_type = input("Option type - type 'c'  for call option or 'p' for put option: ").lower()
            if option_type not in ["c", "p"]:
                raise ValueError("Please input 'c' for call option or'p' for put option")

            S = float(input("Current stock price: ").replace(",", "."))
            K = float(input("Strike price: ").replace(",", "."))

            t = float(input("Time to maturity (in years): ").replace(",", "."))
            # If time to maturity is inputted as days to maturity, convert it to time to maturity in years
            if t > 1:
                t = t / 365

            r = input("Risk-free interest rate: ").replace(",", ".")
            # If input is in percentage, remove percentage sign and convert to float
            if "%" in r:
                r = r.replace("%", "")
                r = float(r) / 100
            else:
                r = float(r)

            mkt_price = float(input("Market price of the option: ").replace(",", "."))

            # Return the input values
            return option_type, S, K, t, r, mkt_price
        except ValueError as e:
            # Handle invalid input and prompt the user to try again
            print(str(e))

if __name__ == "__main__":
    main()
