#!/usr/bin/env python3
from functools import wraps
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt



def title(msg):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            n = len(msg)
            dash = '*' * n
            print(f"\n{dash}\n{msg}\n{dash}\n\n")
            ans = func(*args, **kwargs)
            if ans is None:
                return
            return ans
        return wrapper
    return decorate

# [1] Estimators of the main statistical measures
## [1.1] Mean
## [1.2] Variance
## [1.3] Standard deviation
## [1.4] Covariance
## [1.5] Correlation
## [1.6] Standard Error (SE)

# [2] Main Distributions
## [2.1] Normal Distribution

@title("Normal distribution")
def normal_distribution():
    mu = 0                      # mean
    variance = 2                # variance
    sigma = np.sqrt(variance)   # standard deviation
    x = np.linspace(mu-3*variance, mu+3*variance, 100)
    y = stats.norm.pdf(x, mu, sigma)
    plt.figure()
    plt.plot(x, y)
    plt.title("Normal distribution")
    
    
## [2.2] Chi-Square distribution
## [2.3] Fisher's F-distribution

@title("Fisher's F-distribution")
def fisher_distribution():
    fisher = stats.f
    
    fvalues = np.linspace(.1, 5, 100)
    plt.figure()
    # pdf(x, df1, df2): Probability densitiy function at x of F.
    plt.plot(fvalues, fisher.pdf(fvalues, 1, 30), 'b-', label='F(1, 30)')
    plt.plot(fvalues, fisher.pdf(fvalues, 5, 30), 'r-', label='F(5, 30)')
    plt.legend()
    plt.title("Fisher's F-distribution")
    
    # cdf(x, df1, df2): Cummulative distribution function of F
    proba_at_f_inf_3 = fisher.cdf(3, 1, 30)     # P(F(1, 30) < 30)
    
    # ppf(q, df1, df2): Percent point function (inverse of cdf) at q of F.
    f_at_proba_inf_95 = fisher.ppf(.95, 1, 30)  # q such P(F(1, 30) < .95)
    assert fisher.cdf(f_at_proba_inf_95, 1, 30) == .95
    
    # sf(x, df1, df2): Survival function (1 - cdf) at x of F
    proba_at_f_sup_3 = fisher.sf(3, 1, 30)      # P(F(1, 30) > 3)
    assert proba_at_f_inf_3 + proba_at_f_sup_3 == 1
    
    # p-value: P(F(1, 30)) < 0.05
    low_proba_fvalues = fvalues[fvalues > f_at_proba_inf_95]
    plt.fill_between(low_proba_fvalues, 0, fisher.pdf(low_proba_fvalues, 1, 30),
                     alpha=.8, label='P < 0.05')
    
    
# Hypothesis Testing
## One sample t-test
## - Model the data
## - Fit: estimate the model parameters
## - Test

TITLE = "Hypothesis Testing:\nExample of testing the mean height of population."
@title(TITLE+'\nOne sample t-test')
def one_sample_t_test():
    x = [1.83, 1.83, 1.73, 1.82, 1.83, 1.73, 1.99, 1.85, 1.68, 1.87]
    xbar = np.mean(x)           # sample mean
    mu0 = 1.75                  # hypothesized value
    s = np.std(x, ddof=1)       # sample standard deviation
    n = len(x)
    
    tobs = (xbar - mu0) / (s/np.sqrt(n))
    print(f"T-Statistics:\n\ttobs = {tobs}")
    
    
    _TITLE = "Hypothesis Testing:\nPlotting p-value on graph"

    @title(_TITLE)
    def plotting_pvalue_t_test():
        # n = len(x)
        # tobs = 2.39687663116        # assume the t-value (as computed above)
        tvalues = np.linspace(-10, 10, 100)
        plt.plot(tvalues, stats.t.pdf(tvalues, n-1), 'b-', label='T(n-1)')
        upper_tval_tvalues = tvalues[tvalues > tobs]
        plt.fill_between(upper_tval_tvalues, 0, stats.t.pdf(upper_tval_tvalues, n-1),
                         alpha=.8, label='p-value')
        plt.legend()
    plotting_pvalue_t_test()
    
    

# Testing pairwise associations
## Pearson correlation test: test association between two quantitative variables
## Two sample (Student) t-test: compare two means
## - Model the data
## - Fit: estimate the model parameters
## - T-Test
### Equal or unequal sample sizes, unequal variances (Welch's t-test)
## ANOVA F-test (quantitative ~ categorial (> 2 levels))
## - Model the data
## - Fit: estimate the model parameters
## - F-Test
## Chi-Square, X^2 (categorial ~ categorial)

# Non-parameteric test of pairwise associations
## Spearman rank-order correlation (quantitative ~ quantitative)
## Wilcoxon signed-rank test (quanititative ~ categorial)
## Mann-whitney U test (quantitative ~ categorial (2 level))

# Linear model
## Simple regression: test association between two quantitative variables
## - Model the data
## - Fit: estimate the model parameters
## - F-Test
## ** Goodness of fit
## ** Test
## Multiple regression

# Linear model with statmodels
## Multiple regression
## Multiple regression with categorical independent variables or factors:
## ... Analyis of covariance (ANCOVA)
## - One-way AN(C)OVA
## - Two-way AN(C)OVA
## - Comparing two nested models
## - Factor coding
## - Contrasts and post-hoc tests

# Multiple comparisons
## Bonferroni correction for multiple comparisons
## The False discovery rate (FDR) correction for multiple comparisons
## Brain volume study


def main():
    # Normal distribution
    # normal_distribution()
    
    # Fisher's F-distribution
    # fisher_distribution()
    
    # One sample t-test
    one_sample_t_test()
    plt.show()
    
    
if __name__ == "__main__":
    main()
    # Example One sample t-test
    # one_sample_t_test()
