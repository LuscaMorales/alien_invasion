class GameStats():
    """Armazena dados estatisticos da invasao alienigena."""

    def __init__(self, ai_settings):
        """Iniciliza os dados estatíticos"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #inicia alien invasion em um estado ativo
        self.game_active = True

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo """
        self.ships_left = self.ai_settings.ship_limit
