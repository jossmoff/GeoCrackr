#! /usr/bin/env python3


#GeoCracker: Is a Python Google Chrome wrapper that reveals
#your location in the popular online game GeoGuessr.


from time import sleep
import re
from selenium import webdriver

__version__ = "0.1.0"

BANNER = r"""
                                                          .-'';'-.
                                                        ,'   <_,-.`.
     _____             _____                _          /)   ,--,_>\_\
    / ____|           / ____|              | |        |'   (      \_ |  
   | |  __  ___  ___ | |     _ __ __ _  ___| | ___ __ |_    `-.    / |
   | | |_ |/ _ \/ _ \| |    | '__/ _` |/ __| |/ / '__| \`-.   ;  _(`/
   | |__| |  __/ (_) | |____| | | (_| | (__|   <| |     `.(    \/ ,' 
    \_____|\___|\___/ \_____|_|  \__,_|\___|_|\_\_|       `-....-'"""[1:]


class Game(webdriver.Chrome):

  def __init__(self, path, chrome_options):
    super().__init__(path, options = chrome_options)
    self._current_lat_lng = ""
    self._current_round_num = 1
    self._finished = False

  def get_round_number(self):
    game_info_elements = self.find_elements_by_class_name("game-info__value")

    # Couldn't find the elements so return current value
    if len(game_info_elements) == 0:
      return self._current_round_num
    else:
      game_info_element = game_info_elements[0].get_attribute('innerHTML')
      round_num = re.sub("(<!--.*?-->)", "",
                         game_info_element, flags=re.DOTALL)[0]
      self._current_round_num = int(round_num)

      return int(round_num)

  def get_link(self):
    while 1:
      page_data = self.page_source

      # Find the location of the position you are dropped at
      try:
        link_part = page_data.split('href="https://maps.google.com/maps/@')[1]
      except IndexError:
        sleep(2)
      else:
        break    
    # Effectively splits at the second occurence of ','
    self._current_lat_lng = ",".join(link_part.split(",", 2)[:2])

    # Return Google Maps Link for dropped location 
    return ('https://www.google.com/maps/place/' + self._current_lat_lng + '/'
            + self._current_lat_lng + ',15z')

  def get_lat_lng(self):
    return self._current_lat_lng

  def wait(self, round_num):
    if round_num == 5:
       self._finished = True
    else:
      while(self.get_round_number() == round_num and not self._finished):
        sleep(2)

  def finished(self):
    return self._finished

def main():                                               
  print(BANNER)
  url = input("Please enter a url: ")

  # Create and add Chrome Options
  chrome_options = webdriver.ChromeOptions() 
  chrome_options.add_argument('--log-level=3')

  # Open GeoGuesser
  game = Game('./drivers/chromedriver.exe' ,chrome_options)
  game.get(url)
  while not game.finished():
    round_num = game.get_round_number()
    link = game.get_link()
    lat_lng = game.get_lat_lng()
    print("\nRound " + str(round_num) + "\nLat, Long: " + lat_lng)

    # Checks to see if we have another active tab available
    # to open the google maps page in.
    if len(game.window_handles) == 1:
      game.execute_script("window.open('');")
      
    # Switch to the new window
    game.switch_to.window(game.window_handles[1])
    game.get(link)
    
    # Switch to Original Window
    game.switch_to.window(game.window_handles[0])
    game.wait(round_num)
    

if __name__ == "__main__":
    main()