from contribuidor import Contribuidor

class Moderador(Contribuidor):
    def pode_moderar(self):
        return True