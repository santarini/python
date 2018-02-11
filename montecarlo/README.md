## Description

Monte Carlo simulations are used to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of random variables. They can be used to understand the impact of risk and uncertainty in prediction and forecasting models.


## Table of Contents


### Coin Flips

* <b>CoinFlip.py</b>
  * uses a binary to simulate a coin flip over a specified number of instances
    * Eg. Given 100 coin flips, what percentage of the time will I get heads or tails

* <b>CoinFlipTrials.py</b>
  * performs the entire CoinFlip function a specified number of times
    * Eg. Do CoinFlip.py 1,000,000 times (START WITH A 10!!)
    
### Market Sims

These sort of build onto each other (in this order)

* <b>MarketSim.py</b>
  * simulates a market performance for a single variable over a specified number of instances
    * Eg. Given max and min avg daily delta parameters, simulate a company's performance over a year
    
* <b>MarketSimTrials.py</b>
  * performs the entire MarketSim function a specified number of times
    * Eg. Do MarketSim.py 1,000,000 times (START WITH A 10!!)
    
 * <b>MktSimTrialsCSV.py</b>
   * exports MarketSimTrials output to CSV so that it can be manipulated by spreadsheet software (namely Excel)
     * Eg. Export the output of MarketSimTrials.py to a CSV
  
### Dice Rolls

* <b>RollDie.py</b>
  * simulates a die roll over a specified number of instances
    * Eg. Given 100 die rolls, what percentage of the time will I get 1, 2, 3, 4, 5, 6
    
* <b>RollDice.py</b>
  * simulates the roll of two die (or dice) over a specified number of instances
    * Eg. Given 100 dice rolls, what percentage of the time will I get 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
 
* <b>RollDiceTrials.py</b>
  * performs the entire RollDice function a specified number of times
    * Eg. Do RollDice.py 1,000,000 times (START WITH A 10!!)
