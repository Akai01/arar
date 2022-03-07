================
Arar forecasting
================


.. image:: https://img.shields.io/pypi/v/arar.svg
        :target: https://pypi.python.org/pypi/arar

.. image:: https://img.shields.io/travis/akai01/arar.svg
        :target: https://travis-ci.com/akai01/arar

.. image:: https://readthedocs.org/projects/arar/badge/?version=latest
        :target: https://arar.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




The ARAR Algorithm:
===================

Memory Shortening
-----------------

The ARAR algorithm applies a memory-shortening transformation if the
underlying process of a given time series
*Y*\ \ *t*\ , *t* = 1, 2, …, *n* is “long-memory” then it fits an
autoregressive model.

The algorithm follows five steps to classify *Y*\ \ *t*\  and take one
of the following three actions:

-  L: declare *Y*\ \ *t*\  as long memory and form *Y*\ \ *t*\  by
   *Ỹ*\ \ *t*\  = *Y*\ \ *t*\  − *ϕ̂**Y\ **\ t\ * − *\ τ̂\*
-  M: declare *Y*\ \ *t*\  as moderately long memory and form
   *Y*\ \ *t*\  by
   *Ỹ*\ \ *t*\  = *Y*\ \ *t*\  − *ϕ̂*\ 1\ *Y*\ \ *t* − 1 − *ϕ̂*\ 2\ *Y*\ \ *t* − 2
-  S: declare *Y*\ \ *t*\  as short memory.

If *Y*\ \ *t*\  declared to be *L* or *M* then the series *Y*\ \ *t*\ 
is transformed again until. The transformation process continuous until
the transformed series is classified as short memory. However, the
maximum number of transformation process is three, it is very rare a
time series require more than 2.

The Algorithm:
--------------

-  

   1. For each *τ* = 1, 2, …, 15, we find the value $ $ of *ϕ̂* that
      minimizes
      :math:`ERR(\\phi, \\tau) = \\frac{\\sum\_{t=\\tau +1 }^{n} \[Y\_{t} - \\phi Y\_{t-\\tau}\]^2 }{\\sum\_{t=\\tau +1 }^{n} Y\_{t}^{2}}`
      then define :math:`Err(\\tau) = ERR(\\hat{\\phi(\\tau), \\tau})`
      and choose the lag *τ̂* to be the value of *τ* that minimizes
      *E\ *\ **r**\ *\ r*\ (*τ*).

-  

   1. If *E\ *\ **r**\ *\ r*\ (*τ̂*) ≤ 8/*n*, *Y*\ \ *t*\  is a
      long-memory series.

-  

   1. If *ϕ̂*\ (*τ̂*) ≥ 0.93 and *τ̂* > 2, *Y*\ \ *t*\  is a long-memory
      series.

-  

   1. If *ϕ̂*\ (*τ̂*) ≥ 0.93 and *τ̂* = 1 or 2, *Y*\ \ *t*\  is a
      long-memory series.

-  

   1. If *ϕ̂*\ (*τ̂*) < 0.93, *Y*\ \ *t*\  is a short-memory series.

Subset Autoregressive Model:
----------------------------

In the following we will describe how ARAR algorithm fits an
autoregressive process to the mean-corrected series
*X*\ \ *t*\  = *S*\ \ *t*\  − *S̄*, *t* = *k* + 1, …, *n* where
*S*\ \ *t*\ , *t* = *k* + 1, …, *n* is the memory-shortened version of
*Y*\ \ *t*\  which derived from the five steps we described above and
*S̄* is the sample mean of *S*\ \ *k* + 1, …, *S*\ \ *n*\ .

The fitted model has the following form:

*X*\ \ *t*\  = *ϕ*\ 1\*X**t\ * − 1 + *\ ϕ\ *1*\ X\ **\ t\ * − *\ l\ *1 + *\ ϕ\ *1*\ X\ **\ t\ * − *\ l\ *1 + *\ ϕ\ *1*\ X\ **\ t\ * − *\ l\ *1 + *\ Z\*

where *Z* ∼ *W**N\ *(0,*\ σ\ *2). The coefficients*\ ϕ\ **\ j\ * and
white noise variance*\ σ\ *2 can be derived from the Yule-Walker
equations for given lags*\ l\ *1, *\ l\ *2, and*\ l\*3 :

= and
*σ*\ 2 = *γ̂*\ (0)[1−\ *ϕ*\ 1\ *ρ̂*\ (1)] − *ϕ*\ \ *l*\ 1\ *ρ̂*\ (*l*\ 1)] − *ϕ*\ \ *l*\ 2\ *ρ̂*\ (*l*\ 2)] − *ϕ*\ \ *l*\ 3\ *ρ̂*\ (*l*\ 3)],
where *γ̂*\ (*j*) and *ρ̂*\ (*j*), *j* = 0, 1, 2, …, are the sample
autocovariances and autocorelations of the series *X*\ \ *t*\ .

The algorithm computes the coefficients of *ϕ*\ (*j*) for each set of
lags where 1 < *l*\ 1 < *l*\ 2 < *l*\ 3 ≤ *m* where m chosen to be 13 or
26. The algorithm selects the model that the Yule-Walker estimate of
*σ*\ 2 is minimal.

Forecasting
-----------

If short-memory filter found in first step it has coefficients
*Ψ*\ 0, *Ψ*\ 1, …, *Ψ*\ \ *k*\ (*k*\ ≥0) where *Ψ*\ 0 = 1. In this case
the transforemed series can be expressed as where
*Ψ*\ (*B*) = 1 + *Ψ*\ 1\ *B* + … + *Ψ*\ \ *k*\ \ *B*\ \ *k*\  is
polynomial in the back-shift operator.

If the coefficients of the subset autoregression found in the second
step it has coefficients *ϕ*\ 1, *ϕ*\ \ *l*\ 1, *ϕ*\ \ *l*\ 2 and
*ϕ*\ \ *l*\ 3 then the subset AR model for
*X*\ \ *t*\  = *S*\ \ *t*\  − *S̄* is

where *Z*\ \ *t*\  is a white-noise series with zero mean and constant
variance and
*ϕ*\ (*B*) = 1 − *ϕ*\ 1\ *B* − *ϕ*\ \ *l*\ 1\ *B*\ \ *l*\ 1 − *ϕ*\ \ *l*\ 2\ *B*\ \ *l*\ 2 − *ϕ*\ \ *l*\ 3\ *B*\ \ *l*\ 3.
From equation (1) and (2) one can obtain

where *ξ*\ (*B*) = *Ψ*\ (*B*)\ *ϕ*\ (*B*).

Assuming the fitted model in equation (3) is an appropriate model, and
*Z*\ \ *t*\  is uncorrelated with *Y*\ \ *j*\ , *j* < *t* ∀\ *t* ∈ *T*,
one can determine minimum mean squared error linear predictors
*P*\ \ *n*\ \ *Y*\ \ *n* + *h*\  of *Y*\ \ *n* + *h*\  in terms of
1, *Y*\ 1, …, *Y*\ \ *n*\  for *n* > *k* + *l*\ 3, from recursions

with the initial conditions
*P*\ \ *n*\ \ *Y*\ \ *n* + *h*\  = *Y*\ \ *n* + *h*\ , for *h* ≤ 0.




* Free software: MIT license
* Documentation: https://arar.readthedocs.io.


Features
--------

* TODO

Credits
-------
* TODO