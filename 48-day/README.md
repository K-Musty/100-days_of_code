# DAY 48 of 100 - Selenium

### Challenges
- Go to the game website and familiarise yourself with how it works: http://orteil.dashnet.org/experiments/cookie/ (classic version)
- Create a bot using Selenium and Python to click on the cookie as fast as possible.
- Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive one. You'll need to check how much money (cookies) you have against the price of each upgrade.
- After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second".
- Once you've managed to get the bot to work, feel free to tweak the algorithm if you think there is a better way to play the game. 

#### Notes
- Using Service class to use the service argument in the webdriver object, 'executable_path' has been deprecated"
- Using two helper functions, get_current_money and get_cookies_per_secong
- The bot enters a while loop to continuously play the game until 15 seconds have passed (end_time). 
- for every 5 seconds (time_skip), the bot:
	. Checks how many cookies are available using get_current_money().
    	. Looks at the right-hand panel for available upgrades (#store div elements).
    	. Processes each upgrade:
        . Reads the price of the upgrade.
        . Compares it to the current cookie total.
        . If affordable, adds it to a list (prices_affordable)
- From the list of affordable upgrades, the bot would buy the highest affordable upgrade
- The bot stops for 5 seconds before attemping to buy an upgrade
- After a total of 5 minutes the bots stops and prints out the total cookie per second and driver quits


