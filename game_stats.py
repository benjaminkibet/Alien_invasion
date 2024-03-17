class GameStats():
    """Track game statistics """
    def __init__(self,ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #start the game actiuve flag as true
        self.game_active = False
        self.high_score = 0

    def reset_stats(self,) :
        """initialize stats that can change during the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        
        


           

      