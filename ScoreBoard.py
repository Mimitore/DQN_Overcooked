import pygame

class ScoreBoard:
    def __init__(self, initial_score=0):
        self.score = initial_score

    def draw(self, screen):
        score_text = pygame.font.Font(None, 36).render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def update_score(self, points=1):
        self.score += points
        print(f"Score updated: {self.score}")

    def reset(self):
        self.score = 0