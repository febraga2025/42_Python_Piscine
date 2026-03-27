class GameEngine:
    def __init__(self, factory, strategy):
        self.factory = factory
        self.strategy = strategy
        self.hand = []
        self.battlefield = []

    def setup_game(self):
        # Usa a fábrica para criar um deck e puxar 3 cartas para a mão
        deck_info = self.factory.create_themed_deck(size=5)
        # (Aqui você instanciaria as cartas reais para a mão)
        self.hand = [self.factory.create_creature("goblin"), 
                     self.factory.create_spell("fireball")]

    def run_turn(self):
        print(f"--- Turn Start ({self.strategy.get_strategy_name()}) ---")
        report = self.strategy.execute_turn(self.hand, self.battlefield)
        return report