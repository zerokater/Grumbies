import discord

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') # Last I checked this was necessary.
options.add_argument("--start-maximized")
options.add_argument("window-size=1920,1080")
driver = webdriver.Chrome(chrome_options=options)

def token_lookup(token):
  driver.get('https://battle.grumbies.io/lookup')
  driver.maximize_window()

  search_input = driver.find_element(By.CSS_SELECTOR, "input")
  search_input.send_keys(token + Keys.TAB + Keys.RETURN)

  time.sleep(5)


  grumbietoken = driver.find_element(By.CLASS_NAME, "token-box")

  scrrenshot = grumbietoken.screenshot_as_png
  with open('canvas.jpg', 'wb') as f:
     f.write(scrrenshot)

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
 


@client.event
async def on_message(message):
    nachricht = message.content
    if message.author == client.user:
        return
 
    if message.content.startswith('$token'):
        nachricht = nachricht.replace("$token ","")
        token_lookup(nachricht)
        await message.channel.send(file=discord.File('canvas.jpg'))
 
client.run('MTA5MTI1OTM2NTcxMDg5MzA1OA.Gh5lHB.4AzQtnTP-tvZAEOIYXg9L_gGQcJZPCS54S8cWI')
