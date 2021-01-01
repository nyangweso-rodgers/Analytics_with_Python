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