# Z-Score calculation for single data point
def zscore(dp, mu, sd):
    """zscore returns the Z-Score of dp.

    Args:
        dp (float): Data Point.
        mu (float): Mean.
        sd (float): Standard Deviation.

    Returns:
        float: Z-Score of dp.
    """
    z = (dp - mu) / sd

    return z
