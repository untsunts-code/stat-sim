import numpy as np
from scripy.stats import ttest_ind
import random

def simulate_t_tests(num_sims=100, sample_size=100, alpha=0.05, xmean=0, xsd=1, fseed=1):
  """
  Run multiple independent t-tests between samples from the same distribution.

    Parameters:
    -----------
    num_sims : int
        Number of simulations (i.e., how many t-tests to run).
    sample_size : int
        Size of each group in the t-test (equal-sized groups).
    alpha : float
        Significance level threshold (default is 0.05).

    Returns:
    --------
    np.ndarray
        Array of p-values resulting from each t-test.
  """
  random.seed(fseed)
  p_values=[]
  for i in range(num_sims):
    group1 = np.random.normal(xmean, xsd, sample_size)
    group2 = np.random.normal(xmean, xsd, sample_size)
    _, p = ttest_ind(group1, group2)
    p_values[i]= p

  return np.array(p_values)

