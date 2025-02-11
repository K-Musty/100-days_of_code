# DAY 53 OF 100 - CAPSTONE PROJECT: Data Entry Job Automation

### Challenges:
1- Go to https://docs.google.com/forms/ and create your own form
2- Add 3 questions to the form, make all questions "short-answer"
3- Click send and copy the link address of the form. You will need to use this in your program.
4- Go to this web address on Zillow and see how the website is structured, this is where you'll be scraping the data from
5- Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address (Step 4 above).
6- Create a list of links for all the listings you scraped. 
7- Create a list of prices for all the listings you scraped
8- Create a list of addresses for all the listings you scraped
9- Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its price/address/link added to the form. You will need to fill in a new form for each new listing

#### Notes
- Instead of using a long direct XPath for locating elements, you can use a more concise and robust XPath like //input[@class='whsOnd zHQkBf' and @aria-labelledby='i11 i14'] to target the input field directly based on its attributes. This approach makes the locator easier to read and maintain since it focuses on unique and stable attributes like class and aria-labelledby. For example, in your Selenium code, you can replace the long XPath (/html/body/...) with driver.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf' and @aria-labelledby='i11 i14']"). This method ensures your code is more flexible and less prone to breaking if the page structure changes but the attributes remain consistent.
