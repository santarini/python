# Python

This repo is an aggregation of Python programs and snippets. I ~~almost always~~ used to come here before I started writing a new Python script because I have so many useful snippets already written out. But over the years I've become impatient and just started pasting snippets all over the place with no description and now I have no idea what half of them do. So nowadays I just visit past projects that I remember had similar functionalites to the ones I'm trying to create. ~~And having all of these snippets in one place makes scripting largely *plug-and-play*.~~

## Contents

I started making a contents list when I first made this repo. How naive.

###### /RedditDaily/
* contains random programs written according to challenges in the subreddit <a href="https://www.reddit.com/r/dailyprogrammer/">r/DailyProgrammer</a>

###### /montecarlo/
* contains programs that perform monte carlo simulations

###### BithumbArb.py
* fetches crypto trade prices on bithumb and compares them the to the average coinmarketcap.com price

###### CryptoArb.py
* fetches crypto trade prices on exchanges? and compares them the to the average market price?
* this was my first attempt at pulling arb data directly from the HTML of websites

###### DefaultWebBrowser.py
* launches a window in your computer's default web browser, and navigates to a specific URL
   
###### InternetExplorer.py
* launches an Internet Explorer window and navigates to a specific URL.
  
###### PrintElapsedTime.py
* tells you how long it took your program to execute

###### README.md
* is what you're reading right now

###### edge_GitCommit.py
* Navigates to a mark down file on a GitHub repo, edits the file, and commits the edit.
* Requires Selenium and Edge/Edge drivers.

###### inputToArrray.py

###### random_num.py
* Prints a radom number within two parameters (float or int).

###### time.py
* Prints the time. Super intresting stuff.
* *The time is gone, the song is over, thought I'd something more to say...*

###### wordFreqCSV.py

###### wordFrequency.py
  
###### WritetoCSV.py
* Exports output to a CSV.
* NOTE: Taken almost verbatim from the DictWriter <a href="https://docs.python.org/2/library/csv.html#csv.DictWriter">usage example</a> on the Python Standard Library documentation on CSV

###### WritetoTXT.py
* Exports output to a TXT.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details


### Adding Create New Python File to Context Menu
https://stackoverflow.com/questions/19758455/how-do-i-add-a-new-python-script-option-to-the-context-menu/48096112#48096112

1. Open Regedit
2. Navigate to Computer\HKEY_CLASSES_ROOT.py
3. Right click on the .py key > New > Key
4. Name the new key "ShellNew"
5. Inside the ShellNew key, add a new string value
6. Name the string value "NullFile"
7. Change the NullFile's value to 1
8. That's it!
