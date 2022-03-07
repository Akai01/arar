The ARAR Algorithm:
===================

Memory Shortening
-----------------

The ARAR algorithm applies a memory-shortening transformation if the
underlying process of a given time series
:math:`{Y_{t}, t = 1, 2, ..., n}` is “long-memory” then it fits an
autoregressive model.

The algorithm follows five steps to classify :math:`{Y_{t}}` and take
one of the following three actions:

-  L: declare :math:`{Y_{t}}` as long memory and form :math:`{Y_{t}}` by
   :math:`{\tilde{Y}_{t} = Y_{t} - \hat{\phi}Y_{t - \hat{\tau}}}`
-  M: declare :math:`{Y_{t}}` as moderately long memory and form
   :math:`{Y_{t}}` by
   :math:`{\tilde{Y}_{t} = Y_{t} - \hat{\phi}_{1}Y_{t -1} - \hat{\phi}_{2}Y_{t -2}}`
-  S: declare :math:`{Y_{t}}` as short memory.

.. raw:: latex

   \par

If :math:`{Y_{t}}` declared to be :math:`L` or :math:`M` then the series
:math:`{Y_{t}}` is transformed again until. The transformation process
continuous until the transformed series is classified as short memory.
However, the maximum number of transformation process is three, it is
very rare a time series require more than 2.

The Algorithm:
--------------

-  

   1. For each :math:`\tau = 1, 2, ..., 15`, we find the value
      $:raw-latex:`\hat{\phi(\tau)}` $ of :math:`\hat{\phi}` that
      minimizes
      :math:`ERR(\phi, \tau) = \frac{\sum_{t=\tau +1 }^{n} [Y_{t} - \phi Y_{t-\tau}]^2 }{\sum_{t=\tau +1 }^{n} Y_{t}^{2}}`
      then define :math:`Err(\tau) = ERR(\hat{\phi(\tau), \tau})` and
      choose the lag :math:`\hat{\tau}` to be the value of :math:`\tau`
      that minimizes :math:`Err(\tau)`.

-  

   2. If :math:`Err(\hat{\tau}) \leq 8/n`, :math:`{Y_{t}}` is a
      long-memory series.

-  

   3. If :math:`\hat{\phi}( \hat{\tau} ) \geq 0.93` and
      :math:`\hat{\tau} > 2`, :math:`{Y_{t}}` is a long-memory series.

-  

   4. If :math:`\hat{\phi}( \hat{\tau} ) \geq 0.93` and
      :math:`\hat{\tau} = 1` or :math:`2`, :math:`{Y_{t}}` is a
      long-memory series.

-  

   5. If :math:`\hat{\phi}( \hat{\tau} ) < 0.93`, :math:`{Y_{t}}` is a
      short-memory series.

Subset Autoregressive Model:
----------------------------

In the following we will describe how ARAR algorithm fits an
autoregressive process to the mean-corrected series
:math:`X_{t} = S_{t}- {\bar{S}}`, :math:`t = k+1, ..., n` where
:math:`{S_{t}, t = k + 1, ..., n}` is the memory-shortened version of
:math:`{Y_{t}}` which derived from the five steps we described above and
:math:`\bar{S}` is the sample mean of :math:`S_{k+1}, ..., S_{n}`.

The fitted model has the following form:

:math:`X_{t} = \phi_{1}X{t-1} + \phi_{1}X_{t-l_{1}} + \phi_{1}X_{t- l_{1}} + \phi_{1}X_{t-l_{1}} + Z`

where :math:`Z \sim WN(0, \sigma^{2})`. The coefficients
:math:`\phi_{j}` and white noise variance :math:`\sigma^2` can be
derived from the Yule-Walker equations for given lags :math:`l_1, l_2,`
and :math:`l_3` : :raw-latex:`\begin{equation}
 \begin{bmatrix}
1 & \hat{\rho}(l_1 - 1) & \hat{\rho}(l_2 - 1) & \hat{\rho}(l_3 - 1)\\
\hat{\rho}(l_1 - 1) &1 & \hat{\rho}(l_2 - l_1) & \hat{\rho}(l_3 - l_1)\\
\hat{\rho}(l_2 - 1) & \hat{\rho}(l_2 - l_1) & 1 & \hat{\rho}(l_2 - l_2)\\
\hat{\rho}(l_3 - 1) & \hat{\rho}(l_3 - l_1) & \hat{\rho}(l_3 - l_1) & 1
\end{bmatrix}*\begin{bmatrix}
\phi_{1} \\
\phi_{l_1} \\
\phi_{l_2}\\
\phi_{l_3}
\end{bmatrix} = \begin{bmatrix} \hat{\rho}(1) \\ \hat{\rho}(l_1) \\ \hat{\rho}(l_2)\\ \hat{\rho}(l_3) \end{bmatrix}
\end{equation}`

and
:math:`\sigma^2 = \hat{\gamma}(0) [1-\phi_1\hat{\rho}(1)] - \phi_{l_1}\hat{\rho}(l_1)] - \phi_{l_2}\hat{\rho}(l_2)] - \phi_{l_3}\hat{\rho}(l_3)]`,
where :math:`\hat{\gamma}(j)` and
:math:`\hat{\rho}(j), j = 0, 1, 2, ...,` are the sample autocovariances
and autocorelations of the series :math:`X_{t}`.

The algorithm computes the coefficients of :math:`\phi(j)` for each set
of lags where :math:`1<l_1<l_2<l_3 \leq m` where m chosen to be 13 or
26. The algorithm selects the model that the Yule-Walker estimate of
:math:`\sigma^2` is minimal.

Forecasting
-----------

If short-memory filter found in first step it has coefficients
:math:`\Psi_0, \Psi_1, ..., \Psi_k (k \geq0)` where :math:`\Psi_0 = 1`.
In this case the transforemed series can be expressed as
:raw-latex:`\begin{equation}
    S_t = \Psi(B)Y_t = Y_t + \Psi_1 Y_{t-1} + ...+ \Psi_k Y_{t-k},
\end{equation}` where :math:`\Psi(B) = 1 + \Psi_1B + ...+ \Psi_k B^k` is
polynomial in the back-shift operator.

If the coefficients of the subset autoregression found in the second
step it has coefficients :math:`\phi_1, \phi_{l_1}, \phi_{l_2}` and
:math:`\phi_{l_3}` then the subset AR model for
:math:`X_t = S_t - \bar{S}` is :raw-latex:`\begin{equation}
    \phi(B)X_t = Z_t,
\end{equation}`

where :math:`Z_t` is a white-noise series with zero mean and constant
variance and
:math:`\phi(B) = 1 - \phi_1B - \phi_{l_1}B^{l_1} - \phi_{l_2}B^{l_2} - \phi_{l_3}B^{l_3}`.
From equation (1) and (2) one can obtain

:raw-latex:`\begin{equation}
    \xi(B)Y_t = \phi(1)\bar{S} + Z_t,
\end{equation}` where :math:`\xi (B) = \Psi(B)\phi(B)`.

Assuming the fitted model in equation (3) is an appropriate model, and
:math:`Z_t` is uncorrelated with :math:`Y_j, j <t`
:math:`\forall t \in T`, one can determine minimum mean squared error
linear predictors :math:`P_n Y_{n + h}` of :math:`Y_{n+h}` in terms of
:math:`{1, Y_1, ..., Y_n}` for :math:`n > k + l_3`, from recursions

:raw-latex:`\begin{equation}
    P_n Y_{n+h} = - \sum_{j = 1}^{k + l_3} \xi P_nY_{n+h-j} + \phi(1)\bar{S},  h\geq 1,
\end{equation}` with the initial conditions
:math:`P_n Y_{n+h} = Y_{n + h}`, for :math:`h\leq0`.
