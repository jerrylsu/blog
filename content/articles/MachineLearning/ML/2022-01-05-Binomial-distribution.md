date: 2022-01-05 10:17:17
author: Jerry Su
slug: Binomial-distribution
title: Binomial distribution
category: 
tags: Machine Learning, Statistics

n次伯努利实验，样本相互独立，单次成功概率为p，服从参数为n和p的二项分布:

$$P\{ x= m\} =C_{n}^{m}p^{m}\left( 1-p\right) ^{n-m}   \ \ (其中，0<p<1,  m=0,1,...,n)$$

累计概率分布函数：

$$F\left( m\right) =P\{ X \leq m\} =\sum ^{m}_{i=0}C_{n}^{i}p^{i}\left( 1-p\right) ^{n-i}$$

二项分布的两种逼近：泊松分布 和 标准正态分布(拉普拉斯中心极限定理)

- 当n很大，p较小（稀有事件，一般小于0.1），即np=$\lambda$较小，近似逼近泊松分布

- 当n很大，p较大，即np也很大，近似逼近标准正态分布   $Z=\dfrac{X-np}{\sqrt{np\left( 1-p\right) }}$ ，$X=\sum ^{n}_{i=0}x_{i}$ 对于二项分布，$x_{i}$为所有事件和，即成功次数。

```python3
abnormality = scipy.stats.binom(total / 100, p).cdf((total - loss) / 100)
abnormality = ((total - loss) - total * p) / math.sqrt(total * p * (1 - p))
```

在计算二项分布的分布函数$F_{m}$时，由于需要多次计算$C_{n}^{i}$，对cpu计算资源消耗过大，故采用拉普拉斯中心极限定理或泊分布近似计算。


```python
from scipy import stats
```


```python
stats.binom?
```


    [0;31mSignature:[0m       [0mstats[0m[0;34m.[0m[0mbinom[0m[0;34m([0m[0;34m*[0m[0margs[0m[0;34m,[0m [0;34m**[0m[0mkwds[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mType:[0m            binom_gen
    [0;31mString form:[0m     <scipy.stats._discrete_distns.binom_gen object at 0x7fc9b026c8b0>
    [0;31mFile:[0m            /opt/conda/envs/blog/lib/python3.8/site-packages/scipy/stats/_discrete_distns.py
    [0;31mDocstring:[0m      
    A binomial discrete random variable.
    
    As an instance of the `rv_discrete` class, `binom` object inherits from it
    a collection of generic methods (see below for the full list),
    and completes them with details specific for this particular distribution.
    
    Methods
    -------
    rvs(n, p, loc=0, size=1, random_state=None)
        Random variates.
    pmf(k, n, p, loc=0)
        Probability mass function.
    logpmf(k, n, p, loc=0)
        Log of the probability mass function.
    cdf(k, n, p, loc=0)
        Cumulative distribution function.
    logcdf(k, n, p, loc=0)
        Log of the cumulative distribution function.
    sf(k, n, p, loc=0)
        Survival function  (also defined as ``1 - cdf``, but `sf` is sometimes more accurate).
    logsf(k, n, p, loc=0)
        Log of the survival function.
    ppf(q, n, p, loc=0)
        Percent point function (inverse of ``cdf`` --- percentiles).
    isf(q, n, p, loc=0)
        Inverse survival function (inverse of ``sf``).
    stats(n, p, loc=0, moments='mv')
        Mean('m'), variance('v'), skew('s'), and/or kurtosis('k').
    entropy(n, p, loc=0)
        (Differential) entropy of the RV.
    expect(func, args=(n, p), loc=0, lb=None, ub=None, conditional=False)
        Expected value of a function (of one argument) with respect to the distribution.
    median(n, p, loc=0)
        Median of the distribution.
    mean(n, p, loc=0)
        Mean of the distribution.
    var(n, p, loc=0)
        Variance of the distribution.
    std(n, p, loc=0)
        Standard deviation of the distribution.
    interval(alpha, n, p, loc=0)
        Endpoints of the range that contains alpha percent of the distribution
    
    Notes
    -----
    The probability mass function for `binom` is:
    
    .. math::
    
       f(k) = \binom{n}{k} p^k (1-p)^{n-k}
    
    for ``k`` in ``{0, 1,..., n}``.
    
    `binom` takes ``n`` and ``p`` as shape parameters.
    
    The probability mass function above is defined in the "standardized" form.
    To shift distribution use the ``loc`` parameter.
    Specifically, ``binom.pmf(k, n, p, loc)`` is identically
    equivalent to ``binom.pmf(k - loc, n, p)``.
    
    Examples
    --------
    >>> from scipy.stats import binom
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots(1, 1)
    
    Calculate a few first moments:
    
    >>> n, p = 5, 0.4
    >>> mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
    
    Display the probability mass function (``pmf``):
    
    >>> x = np.arange(binom.ppf(0.01, n, p),
    ...               binom.ppf(0.99, n, p))
    >>> ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
    >>> ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
    
    Alternatively, the distribution object can be called (as a function)
    to fix the shape and location. This returns a "frozen" RV object holding
    the given parameters fixed.
    
    Freeze the distribution and display the frozen ``pmf``:
    
    >>> rv = binom(n, p)
    >>> ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
    ...         label='frozen pmf')
    >>> ax.legend(loc='best', frameon=False)
    >>> plt.show()
    
    Check accuracy of ``cdf`` and ``ppf``:
    
    >>> prob = binom.cdf(x, n, p)
    >>> np.allclose(x, binom.ppf(prob, n, p))
    True
    
    Generate random numbers:
    
    >>> r = binom.rvs(n, p, size=1000)
    [0;31mClass docstring:[0m
    A binomial discrete random variable.
    
    %(before_notes)s
    
    Notes
    -----
    The probability mass function for `binom` is:
    
    .. math::
    
       f(k) = \binom{n}{k} p^k (1-p)^{n-k}
    
    for ``k`` in ``{0, 1,..., n}``.
    
    `binom` takes ``n`` and ``p`` as shape parameters.
    
    %(after_notes)s
    
    %(example)s
    [0;31mCall docstring:[0m 
    Freeze the distribution for the given arguments.
    
    Parameters
    ----------
    arg1, arg2, arg3,... : array_like
        The shape parameter(s) for the distribution.  Should include all
        the non-optional arguments, may include ``loc`` and ``scale``.
    
    Returns
    -------
    rv_frozen : rv_frozen instance
        The frozen distribution.




```python
stats.binom.ppf?
```


    [0;31mSignature:[0m [0mstats[0m[0;34m.[0m[0mbinom[0m[0;34m.[0m[0mppf[0m[0;34m([0m[0mq[0m[0;34m,[0m [0;34m*[0m[0margs[0m[0;34m,[0m [0;34m**[0m[0mkwds[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Percent point function (inverse of `cdf`) at q of the given RV.
    
    Parameters
    ----------
    q : array_like
        Lower tail probability.
    arg1, arg2, arg3,... : array_like
        The shape parameter(s) for the distribution (see docstring of the
        instance object for more information).
    loc : array_like, optional
        Location parameter (default=0).
    
    Returns
    -------
    k : array_like
        Quantile corresponding to the lower tail probability, q.
    [0;31mFile:[0m      /opt/conda/envs/blog/lib/python3.8/site-packages/scipy/stats/_distn_infrastructure.py
    [0;31mType:[0m      method


