# WishBot
> A Discord bot to select, track, and obtain information on possible gift items for your friends and family!
> Test server invite link: https://discord.gg/UQQCZ2RP5u 

Installation tested in a Ubuntu16 system. Python 3.6.9.

## Install dependencies
> OPTION A: INSTALL ALL DEPENDENCIES
```bash
pip3 install -r requirements.txt
```
> OPTION B: INSTALL DEPENDENCIES INDIVIDUALLY
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
> Edit env template.md with bot's token and guild name (steps detailed below) 


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
#### 3. To VIEW the items in a specified recipient's wishlist
retrieve <recipient's name>
#### 4. To RECEIVE A SUGGESTION for a gift for a specified recipient within a certain price range
suggest for <recipient's name> under <cash amount either 20, 50, or 100>
#### 5. To SOLICIT ADVICE about whether or not you should get a present for a specified recipient
advice about <recipient's name>
