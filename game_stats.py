class GameStats():
    """follow game stats"""
    def __init__(self, ai_settings):
        """initial statistics info"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # game active
        self.game_active = False

    def reset_stats(self):
        # initial in game running statistics info
        self.ships_left = self.ai_settings.ship_limit
