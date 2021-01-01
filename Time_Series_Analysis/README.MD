# Time Series Analysis

## Patterns iin Time Series
Any time series may be split into the following components: __Base Level + Trend + Seasonality + Error__

* A __trend__ is observed when there is an increasing or decreasing slope observed in the time series. 
* __seasonality__ is observed when there is a distinct repeated pattern observed between regular intervals due to seasonal factors. It could be because of the month of the year, the day of the month, weekdays or even time of the day.

However, It is not mandatory that all time series must have a trend and/or seasonality. A time series may not have a distinct trend but have a seasonality. The opposite can also be true. So, a time series may be imagined as a combination of the trend, seasonality and the error terms.

* Another aspect to consider is the __cyclic__ behaviour. - It happens when the rise and fall pattern in the series does not happen in fixed calendar-based intervals. Care should be taken to not confuse ‘cyclic’ effect with ‘seasonal’ effect.

* So, How to diffentiate between a ‘__cyclic__’ vs ‘__seasonal__’ pattern? _If the patterns are not of fixed calendar based frequencies, then it is cyclic. Because, unlike the seasonality, cyclic effects are typically influenced by the business and other socio-economic factors._