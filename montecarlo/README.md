# montecarlo

## Description

Monte Carlo simulations are used to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of random variables. They can be used to understand the impact of risk and uncertainty in prediction and forecasting models.

## Table of Contents

These sort of build onto each other (in this order)

* <b>MarketSim.py</b>
  * simulates a market performance for a single variable over a specified number of instances
    * Eg. Given max and min avg daily delta parameters, simulate a companies performance over a year
* <b>MarketSimTrials.py</b>
  * performs the entire MarketSim function a specified number of times
    * Eg. Do MarketSim.py 1,000,000 times (START WITH A 10!!)
 * <b>MktSimTrialsCSV.py</b>
   * exports MarketSimTrials output to CSV so that it can be manipulated by spreadsheet software (namely Excel)
     * Eg. Export the output of MarketSimTrials.py to a CSV
  
