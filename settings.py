class Settings():
    """a place to store all settings for the game """
    def __init__(self):
        #initialize the settings for the game
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,255,0)

    #ship speed settings
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 5
        self.bullet_width = 1
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60 
        self.bullets_allowed = 30    
        self.alien_speed_factor = 1
        self.ship_limit = 3
        #how quickly the alien point values increase
        self.score_scale = 1.5
         
         # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 0.3
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_drop_speed = 10    

        #how quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings thta change during the game play""" 
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1

        #scoring
        self.alien_points = 50 

# fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale   
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        
        