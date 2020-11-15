![WishBot Logo](wishBotLogo.png)
# WishBot
> A Discord bot to select, track, and obtain information on possible gift items for your friends and family!
> Test server invite link: https://discord.gg/UQQCZ2RP5u 

Installation tested in a Ubuntu16 system. Python 3.6.9.

## Install dependencies
## OPTION A: INSTALL ALL DEPENDENCIES (EXPERIMENTAL)
```bash
pip3 install -r requirements.txt
```
## OPTION B: INSTALL DEPENDENCIES INDIVIDUALLY
#### 1. Change directory to /wishbot  
```bash
cd wishbot
```
#### 2. Install Discord.py
```bash
pip3 install -U discord.py
```
#### 3. Install Dotenv  
```bash
pip3 install -U python-dotenv
```
#### 4. Install BeautifulSoup  
```bash
pip3 install beautifulsoup4
```
#### 5. Install lxml requests  
```bash
pip3 install requests soupsieve lxml
```
## Update .env   
##### Used to customize and add WishBot to your own channels.  
> Edit env template.md with bot's token and guild name (steps detailed in the link below)
https://realpython.com/how-to-make-a-discord-bot-python/

## Run bot.py   
```bash
python3 bot.py
```
## Use bot.py
> Type the following into Discord in order to receive the respective result
#### 1. To ADD an item to a wishlist for a specified recipient
give <recipient's name> a(n) <item name>
#### 2. To REMOVE an item from a specified recipient's wishlist
remove <recipient's name>'s <item name>
#### 3a. To VIEW the links to _item searches_ in a specified recipient's wishlist (for large wishlists)
retrieve <recipient's name>
#### 3b. To VIEW the _suggested direct links_ to items in a specified recipient's wishlist (for small wishlists)
retrieve <recipient's name> link(s)
#### 4. To RECEIVE A SUGGESTION for a gift for a specified recipient within a certain price range
suggest for <recipient's name> under <cash amount either 20, 50, or 100>
#### 5. To SOLICIT ADVICE about whether or not you should get a present for a specified recipient
advice about <recipient's name>

## Source Code Walkthrough
Click below to watch!
[![Alt text](https://img.youtube.com/vi/LBh8Fwpyunk/0.jpg)](https://www.youtube.com/watch?v=LBh8Fwpyunk)

## References
https://realpython.com/how-to-make-a-discord-bot-python/

https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href

https://pythonspot.com/extract-links-from-webpage-beautifulsoup/

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

https://stackoverflow.com/questions/14885907/scraping-product-names-using-beautifulsoup

