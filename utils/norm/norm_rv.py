import numpy as np
from .norm_prop import norm_prop


def norm_rv(dp, mus, sds, method, area):
    """norm_rv calculates the combination of random variables then calling function norm_prop to return the proportion of a specific area based on dp.

    Args:
        dp (float or array like): Data Point. float for area = 'below' or area = 'high'; array like (2 float) for area = 'between'.
        mus (array like): Collection of means.
        sds (array like): Collention of standard deviations.
        method (str): One of 'T'(Total) or 'D'(Difference).
        area (str, optional): The specific area ('below', 'above', or 'between') of the normal distribution based on dp. Defaults to 'below'.

    Raises:
        ValueError: method must be one of 'T' or 'D'

    Returns:
        float: The proportion of a specific area based on dp.
    """
    if method not in ['T', 'D']:
        raise ValueError("method must be one of 'T' or 'D'!")
    mus = np.array(mus)
    sds = np.array(sds)
    if method == 'T':
        mu = np.sum(mus)
    else:
        mu = mus[0] - np.sum(mus[1:])
    sd = np.sum(sds**2)**0.5

    p = norm_prop(dp, mu, sd, area)

    return p
