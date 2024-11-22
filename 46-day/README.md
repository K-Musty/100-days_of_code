# DAY 46 of 100 (Spotify Playlist Musical Time Machine)
-----
### The challenge

- Step 1: Scrape the Billboard Hot 100.
- Step 2: Authenticate with Spotify
- Step 3: Search Spotify for the Songs from Step 1
- Step 4: Create and Add to Spotify Playlist

### What I reviewed
- Scraping the Web with Beautiful Soup
- strip() method
- list comprehensions
- requests module

### Notes
- It was an amazing challenge that got me thinking alot, my approach to scraping was really with the use of 'find\_all' not 'select' which made me use alot of methods to get the 100 songs, i used list slicing and sorted through the list, the songs started at 6 and the list ended at 403 and i needed to skip just 4 times for the song title i.e [6:403:4]
- Authentication with spotify was very easy and straight forward with the resources provided
- Searching through the song wanted to cause me issues as i didn't see the spotify search class early in the documentation
- At the end it was all done
