import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """create a score board on the screen """
    def __init__(self,ai_settings,screen,stats):
      """initialize the score"""
      self.screen = screen
      self.screen_rect = screen.get_rect()
      self.ai_settings = ai_settings
      self.stats = stats
      # Font settings for scoring information.
      self.text_color = (30, 30, 30)
      self.font = pygame.font.SysFont(None, 48)
      #prepare the score
      self.prep_score()
      self.prep_high_score()
      self.prep_level()
      self.prep_ships()




    def prep_score(self):
      """Turn the score into a rendered image"""
      score_str = str(self.stats.score)
      self.score_image = self.font.render(score_str, True, self.text_color,self.ai_settings.bg_color)
    #display the score at the top of the screen
      self.score_rect = self.score_image.get_rect()
      self.score_rect.right = self.screen_rect.right - 20
      self.score_rect.top = 20

    def show_score(self):
     """Display the score on the screen"""
     self.screen.blit(self.score_image, self.score_rect) 
     self.screen.blit(self.high_score_image, self.high_score_rect)   
     self.screen.blit(self.level_image, self.level_rect)

     #Draw ships
     self.ships.draw(self.screen)
    def prep_high_score(self):
       """Turn the high score to a rendered image """
       high_score = int(round(self.stats.high_score, -1))  
       high_score_str = "{:,}".format(high_score)
       self.high_score_image = self.font.render(high_score_str, True,self.text_color, self.ai_settings.bg_color)
        # Center the high score at the top of the screen.
       self.high_score_rect = self.high_score_image.get_rect()
       self.high_score_rect.centerx = self.screen_rect.centerx  
       self.high_score_rect.top = self.score_rect.top 

    def prep_level(self):
      """Turn the level into a rendered image"""
      self.level_image = self.font.render(str(self.stats.level), True,self.text_color, self.ai_settings.bg_color)
      #position the level below the score 
      self.level_rect = self.level_image.get_rect()
      
    def prep_ships(self):
      """Display the number of ships we have """
      self.ships = Group()
      for ship_number in range(self.stats.ship_left):
        ship = Ship(self.ai_settings, self.screen)
        ship.rect.x = 10 + ship_number * ship.rect.width
        ship.rect.y = 10
        self.ships.add(ship)