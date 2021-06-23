# Time Series Analysis

## Patterns iin Time Series
Any time series may be split into the following components: __Base Level + Trend + Seasonality + Error__

* A __trend__ is observed when there is an increasing or decreasing slope observed in the time series. This is the type of tendency which continues to persist for a very long period. Prices and export and import data, _for example_, reflect obviously increasing tendencies.

* __Seasonality__: These are short term movements occurring in data due to _seasonal factors_. The short term is generally considered as a period in which changes occur in a time series with variations in weather or festivities.

Seasonality is observed when there is a distinct repeated pattern observed between regular intervals due to seasonal factors. It could be because of the month of the year, the day of the month, weekdays or even time of the day.

However, It is not mandatory that all time series must have a trend and/or seasonality. A time series may not have a distinct trend but have a seasonality. The opposite can also be true. So, a time series may be imagined as a combination of the trend, seasonality and the error terms.

* __Cyclic__:  These are long term oscillations occurring in a time series. These oscillations are mostly observed in economic data and the periods of such oscillations are generally extended from five to twelve years or more. These oscillations are associated with well-known business cycles. _It happens when the rise and fall pattern in the series does not happen in fixed calendar-based intervals. Care should be taken to not confuse ‘cyclic’ effect with ‘seasonal’ effect._

So, How to diffentiate between a ‘__cyclic__’ vs ‘__seasonal__’ pattern? _If the patterns are not of fixed calendar based frequencies, then it is cyclic. Because, unlike the seasonality, cyclic effects are typically influenced by the business and other socio-economic factors._

* __Irregularity__: These are sudden changes occurring in a time series which are unlikely to be repeated. They are components of a time series that cannot be explained by _trends_, _seasonal_ or _cyclic_ movements. These variations are sometimes called __residual__ or __random components__.

# Stationary and Non-Stationary Time Series
A __stationary__ series is one where the values of the series is not a function of time. i.e., the statistical properties of the series like _mean_, _variance_ and _autocorrelation_ are constant over time. __Autocorrelation__ of the series is nothing but the correlation of the series with its previous values.

## Why make a non-stationary series stationary before forecasting?
Forecasting a stationary series is relatively easy and the forecasts are more reliable. An important reason is, __autoregressive forecasting__ models are essentially linear regression models that utilize the lag(s) of the series itself as predictors.

We know that linear regression works best if the predictors (X variables) are not correlated against each other. So, stationarizing the series solves this problem since it removes any persistent autocorrelation, thereby making the predictors(lags of the series) in the forecasting models nearly independent.
## How to make a time series stationary?
You can make series stationary by:
1. Differencing the Series (once or more)
2. Take the log of the series
3. Take the nth root of the series
4. Combination of the above

The most common and convenient method to stationarize the series is by __differencing__ the series at least once until it becomes approximately stationary.



## Additive and Multiplicative Time Series
Depending on the nature of the __trend__ and __seasonality__, a time series can be modeled as an __additive__ or __multiplicative__, wherein, each observation in the series can be expressed as either a _sum_ or a _product_ of the components:

### Additive time series:
__Value = Base Level + Trend + Seasonality + Error__
### Multiplicative Time Series:
__Value = Base Level x Trend x Seasonality x Error__

## How to decompose a time series into its components?
You can do a classical decomposition of a time series by considering the series as an __additive__ or __multiplicative__ combination of the _base level_, _trend_, _seasonal index_ and the _residual_. 

The __seasonal_decompose__ in _statsmodels_ implements this conveniently. Setting extrapolate_trend='freq' takes care of any missing values in the trend and residuals at the beginning of the series.

If you look at the _residuals_ of the additive decomposition closely, it has some pattern left over. The multiplicative decomposition, however, looks quite random which is good. So ideally, multiplicative decomposition should be preferred for this particular series.

# ARIMA Model
__ARIMA__ stands for __Auto Regressive Integrated Moving Average__.  There are __seasonal__ and __Non-seasonal__ ARIMA models that can be used for forecasting. An __ARIMA__ model is characterized by 3 terms: p, d, q where:
* p is the order of the AR term, 
* q is the order of the MA term and 
* d is the number of differences required to make the time series stationary. 

If a time series, has __seasonal__ patterns, then you need to add seasonal terms and it becomes SARIMA, short for ‘__Seasonal ARIMA__’. 

# Prophet model
__Prophet__ is an open source __Time Series Forecasting Algorithm__ from __Facebook__ and it designed for ease of use without expert knowledge on Time Series Forecasting or Statistics. 

Time Series Forecasting builds model by finding a best smooth line which can be represented as sum of the following component:
* Overal Growth Trend
* early Seasonality
* Weekly Seasonality
* Holiday Affects

# The benefit of Prophet Approach:
1. Uneven time interval between data is not a problem
2. Day with NA is not a problem
3. Seasonality with multiple periods (Week & Year) is handled by default
4. Works well by default setting, parameters are easily interpretable

__Prophet__ requires the variable names in the time series to be:
1. y — Target
2. ds — Datetime