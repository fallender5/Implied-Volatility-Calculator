
# Project Title

Implied Volatility Calculator


## Description

This Python program calculates implied volatility of an option using the Newton-Raphson method. Implied volatility is the market's forecast of a likely movement in a security's price and is a metric used by investors to estimate future fluctuations based on certain predictive factors. Implied volatility cannot be directly calculated from the Black-Scholes formula; instead, it needs to be solved for using numerical methods like Newton-Raphson.

Since the Black-Scholes formula is used to calculate theoretical option prices, finding the implied volatility involves solving for it given the observed market price.

The calculate_implied_volatility function starts with an initial guess for the implied volatility (vol_guess), often set to a reasonable value.
It then iteratively refines this guess using the Newton-Raphson method until a convergence criteria is met.

The convergence criteria involve checking whether the difference between the current guess and the next guess for implied volatility is below a certain tolerance level (tol), or if the difference between the Black-Scholes price with the new volatility and the market price is below the tolerance. The iteration continues until one of these criteria is satisfied or the maximum number of iterations (num_iter) is reached.

 


## Prerequisites

- Python 3.x
- Required Python packages: `py_vollib`
## Usage

To use the implied volatility calculator, run the main() function in the provided Python script. The program will prompt you to input the option type, current stock price, strike price, time to maturity, risk-free interest rate, and market price of the option. Follow the on-screen instructions to input the required information.

To run "imp_vol_calculator.py" execute the following command in terminal: 
python imp_vol_calculator.py

## Inputs
option_type = Call or Put Option\
S - Current(spot) price of an underlying asset\
K - Strike Price\
r - Risk-Free Interest Rate\
t - Time to Maturity\
mkt_price - The current market price of the option
## Output
The program will display the calculated implied volatility as a percentage.


## Newton-Raphson Method
The calculation of implied volatility in the provided code is based on the Newton-Raphson method, an iterative numerical technique. The Newton-Raphson method is an iterative root-finding algorithm used for finding successively better approximations to the roots (or zeros) of a real-valued function.

In the context of the provided code, the function being targeted is the difference between the Black-Scholes option price and the market price of the option. The goal is to find the implied volatility that makes this difference close to zero.

The reason for using an iterative approach is that the relationship between option price and implied volatility is nonlinear, and a direct formula for solving for implied volatility does not exist. Newton-Raphson is a widely used method for solving nonlinear equations and is effective for finding roots of functions.

Feel free to use, modify, and distribute this code as needed. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

