# montecarlo

These sort of build onto each other (in this order)

* MarketSim.py
  * simulates a market performance for a single object over a specified number of instances
    * Eg. Given high and low delta parameters, simulate a companies performance over a year
* MarketSimTrials.py
  * performs the entire MarketSim function a specified number of times
    * Eg. Given high and low delta parameters, simulate a companies performance over a year, 1000 times
* MktSimTrialsCSV.py
  * exports MarketSimTrials output to CSV so that it can be manipulated by spreadsheet software (namely Excel)
    * Eg. Export the output of MarketSimTrials.py to a CSV
  
