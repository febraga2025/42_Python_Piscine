from abc import ABC, abstractmethod

class Rankable(ABC):
    @abstractmethod
    def update_rating(self, opponent_rating: int, won: bool) -> int:
        """Calcula e atualiza a pontuação (ELO) da carta."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Retorna as estatísticas de ranking (Rating e Record)."""
        pass