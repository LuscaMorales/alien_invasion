class Settings():
    def __init__(self):
        self.screen_widht = 1200
        self.screen_height = 650
        self.bg_collor = (30,26,29)
        self.nave_speed = 5
        self.nave_size = (50,100)
        #config dos tiros
        self.tiro_speed_factor = 3
        self.tiro_widht = 15
        self.tiro_height = 3
        self.tiro_color = (240,240,240)
        self.tiros_allowed = 3
        #config da gota
        self.gota_speed = 1
        self.star_speed = 1
        #config limites
        self.lost_star = 0
        self.lost_limit = 3