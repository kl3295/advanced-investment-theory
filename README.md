# advanced-investment-theory
This project aims 1) to build a factor-based model allocation namely a Long/Short Global Macro Strategy with a Target Beta and 2) to evaluate its sensitivity to variations of Beta and its sensitivity to the length of the estimators for covariance matrix and the expected returns under different market scenarios.

The performance and the risk profiles of such a strategy may be very sensitive to the target Beta and the market environment. A low Beta meaning a strategy that aims to be de-correlated to the global market represented by the S&P 500, while a high Beta meaning that, having a big appetite for risk, we are aiming to ride or scale up the market risk. In addition to that, such a strategy is likely to to be quite sensitive to the estimators used for the Risk Model and the Alpha Model (for example the length of the look-back period used for estimation risk and expected returns), so it is important to understand the impact of those estimators on the Portfolio’s characteristics: realized return, volatility, skewness, VaR/ CVaR and risk to performance ratios such as the Sharpe ratio.

The behavior of the optimal portfolio built from a specific combination of estimators for Covariance and Expected Return may change with the market environment and the target Beta (a particular strategy being defined by a specific combination, for example S90(0.5) - say using 60 days for estimation of 60 covariance, 90 days for estimation of Expected Returns and a target β = 0.5). The goal of this project is to understand, analyze and compare the behavior of strategies built using chosen combinations of return/risk estimators and Target Beta during several historical periods : before the subprime (2008) crisis, during that crisis and after the crisis. The factor model we will use, known as the French Fama 3-factor model has 3 factors, Momentum, Value and Size.

We will consider the following set of ETFs downloaded from Yahoo from March 1st, 2007 to November 29th, 2019.
1. CurrencyShares Euro Trust (FXE)
2. iShares MSCI Japan Index (EWJ)
3. SPDR GOLD Trust (GLD)
4. Powershares NASDAQ-100 Trust (QQQ) 5. SPDR S&P 500 (SPY)
6. iShares Lehman Short Treasury Bond (SHV) 7. PowerShares DB Agriculture Fund (DBA)
8. United States Oil Fund LP (USO)
9. SPDR S&P Biotech (XBI)
10. iShares S&P Latin America 40 Index (ILF)
11. iShares MSCI Pacific ex-Japan Index Fund (EPP) 12. SPDR DJ Euro Stoxx 50 (FEZ)
12. SPDR DJ Euro Stoxx 50 (FEZ)

The benchmark will be the Market Portfolio S&P 500 ( SPY ETF)
