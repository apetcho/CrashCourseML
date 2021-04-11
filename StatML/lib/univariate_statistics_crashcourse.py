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
    plt.plot(x, y)
    
    
## [2.2] Chi-Square distribution
## [2.3] Fisher's F-distribution

# Hypothesis Testing
## One sample t-test
## - Model the data
## - Fit: estimate the model parameters
## - Test

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
    normal_distribution()
    
    plt.show()
    
    
if __name__ == "__main__":
    main()
