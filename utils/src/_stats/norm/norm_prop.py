from scipy.stats import norm
from utils.src._stats.zscore import zscore


def norm_prop(dp, mu, sd, area='below'):
    """norm_prop returns the proportion of a specific area based on dp.

    Args:
        dp (float or array like): Data Point. float for area = 'below' or area = 'high'; array like (2 float) for area = 'between'.
        mu (float): Mean.
        sd (float): Standard Deviation.
        area (str, optional): The specific area ('below', 'above', or 'between') of the normal distribution based on dp. Defaults to 'below'.

    Raises:
        ValueError: area must be one of 'below', 'above', or 'between'.
        ValueError: dp must be 2 for calculating proportion between two data points.

    Returns:
        float: The proportion of a specific area based on dp.
    """
    if area not in ['below', 'above', 'between']:
        raise ValueError("area must be one of 'below', 'above', or 'between'!")
    # Proportion below dp
    if area == 'below':
        p = norm.cdf(zscore(dp, mu, sd))
    # Proportion above dp
    elif area == 'above':
        p = 1 - norm.cdf(zscore(dp, mu, sd))
    # Proportion between dp_low and dp_high
    else:
        if isinstance(dp, (int, float, dict, str)):
            raise TypeError("dp must be an array like type!")
        if len(dp) != 2:
            raise ValueError("dp must contains two data points!")
        dp_low, dp_high = min(dp), max(dp)
        p = norm.cdf(zscore(dp_high, mu, sd)) - norm.cdf(zscore(dp_low, mu, sd))

    return p
