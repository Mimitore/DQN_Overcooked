class Actions:
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
    SPACE = 4
    CUT = 5

    # Créer un dictionnaire pour convertir les numéros en noms d'action
    action_names = {
        0: 'LEFT',
        1: 'RIGHT',
        2: 'UP',
        3: 'DOWN',
        4: 'SPACE',
        5: 'CUT'
    }


    # Fonction pour obtenir le nom de l'action
    def get_action_name(self,action_id):
        return self.action_names.get(action_id, "Unknown Action")