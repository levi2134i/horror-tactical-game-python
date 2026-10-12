import pygame
from game.settings import (
    WIDTH, HEIGHT, WHITE, BLACK, TEXT_LIGHT, TEXT_GRAY,
    DARK, DARK_GRAY, RED, GREEN, BLUE, ACCENT, HEALTH_RED, HEALTH_GREEN
)

class UIRenderer:
    def __init__(self):
        self.font_large = pygame.font.SysFont("Arial", 28, bold=True)
        self.font_medium = pygame.font.SysFont("Arial", 20, bold=True)
        self.font_small = pygame.font.SysFont("Arial", 16)
        self.font_tiny = pygame.font.SysFont("Arial", 14)

    def draw_hud(self, screen, player_hp, player_ammo, players_alive, zone_info):
        """Draw main HUD elements"""
        # Health Bar
        self._draw_health_bar(screen, player_hp)
        
        # Top Stats
        self._draw_top_stats(screen, players_alive, zone_info)
        
        # Ammo Counter
        self._draw_ammo(screen, player_ammo)
        
        # FPS Counter
        self._draw_fps(screen)

    def _draw_health_bar(self, screen, hp):
        """Draw health bar at bottom left"""
        bar_width = 300
        bar_height = 30
        bar_x = 20
        bar_y = HEIGHT - 50
        
        # Background
        pygame.draw.rect(screen, DARK_GRAY, (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, ACCENT, (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Health fill
        health_ratio = max(0, hp / 100)
        fill_width = bar_width * health_ratio
        fill_color = HEALTH_GREEN if health_ratio > 0.3 else HEALTH_RED
        pygame.draw.rect(screen, fill_color, (bar_x + 2, bar_y + 2, fill_width - 4, bar_height - 4))
        
        # Text
        hp_text = self.font_medium.render(f"HP: {int(hp)} / 100", True, WHITE)
        screen.blit(hp_text, (bar_x + 10, bar_y + 4))

    def _draw_top_stats(self, screen, players_alive, zone_info):
        """Draw top bar with match stats"""
        # Background panel
        pygame.draw.rect(screen, DARK_GRAY, (0, 0, WIDTH, 60))
        pygame.draw.line(screen, ACCENT, (0, 60), (WIDTH, 60), 2)
        
        # Title
        title = self.font_large.render("NIGHTFALL PROTOCOL", True, ACCENT)
        title_rect = title.get_rect(center=(WIDTH // 2, 30))
        screen.blit(title, title_rect)
        
        # Players alive
        players_text = self.font_small.render(f"ALIVE: {players_alive}", True, TEXT_LIGHT)
        screen.blit(players_text, (20, 70))
        
        # Zone timer
        if zone_info:
            zone_text = self.font_small.render(f"ZONE: {zone_info}", True, TEXT_LIGHT)
            screen.blit(zone_text, (WIDTH - 200, 70))

    def _draw_ammo(self, screen, ammo):
        """Draw ammo counter at bottom right"""
        mag, reserve = ammo
        ammo_text = self.font_medium.render(f"{mag} / {reserve}", True, BLUE)
        ammo_label = self.font_small.render("AMMO", True, TEXT_GRAY)
        
        screen.blit(ammo_label, (WIDTH - 120, HEIGHT - 60))
        screen.blit(ammo_text, (WIDTH - 120, HEIGHT - 35))

    def _draw_fps(self, screen):
        """Draw FPS counter at top right"""
        fps = int(pygame.time.Clock().get_fps())
        fps_text = self.font_tiny.render(f"FPS: {fps}", True, TEXT_GRAY)
        screen.blit(fps_text, (WIDTH - 100, 10))

    def draw_player_info(self, screen, players):
        """Draw player names and HP above their models"""
        for pid, p in players.items():
            if pid.startswith('p'):
                px = p.get('x', 0)
                py = p.get('y', 0)
                hp = p.get('hp', 100)
                name = p.get('name', 'Agent')
                
                # Name label
                name_surf = self.font_tiny.render(name, True, TEXT_LIGHT)
                screen.blit(name_surf, (px - name_surf.get_width() // 2, py - 35))
                
                # Small HP bar above player
                bar_width = 32
                bar_height = 4
                pygame.draw.rect(screen, DARK_GRAY, (px - bar_width // 2, py - 25, bar_width, bar_height))
                fill_color = HEALTH_GREEN if hp > 50 else HEALTH_RED if hp > 25 else RED
                pygame.draw.rect(screen, fill_color, (px - bar_width // 2, py - 25, int(bar_width * (hp / 100)), bar_height))

    def draw_crosshair(self, screen, mouse_pos):
        """Draw aiming crosshair"""
        size = 15
        thickness = 2
        x, y = mouse_pos
        
        # Vertical line
        pygame.draw.line(screen, ACCENT, (x, y - size), (x, y + size), thickness)
        # Horizontal line
        pygame.draw.line(screen, ACCENT, (x - size, y), (x + size, y), thickness)
        # Center dot
        pygame.draw.circle(screen, ACCENT, (x, y), 3)

    def draw_minimap(self, screen, player_pos, players, map_width=150):
        """Draw minimap at top right"""
        map_x = WIDTH - map_width - 20
        map_y = 80
        
        # Minimap background
        pygame.draw.rect(screen, DARK_GRAY, (map_x, map_y, map_width, map_width))
        pygame.draw.rect(screen, ACCENT, (map_x, map_y, map_width, map_width), 2)
        
        # Scale factor (assuming world is 1600x900)
        scale_x = map_width / 1600
        scale_y = map_width / 900
        
        # Draw players
        for pid, p in players.items():
            px = p.get('x', 0) * scale_x
            py = p.get('y', 0) * scale_y
            color = p.get('color', (255, 255, 255))
            pygame.draw.circle(screen, color, (int(map_x + px), int(map_y + py)), 3)
        
        # Draw self
        self_x = player_pos[0] * scale_x
        self_y = player_pos[1] * scale_y
        pygame.draw.circle(screen, (0, 255, 0), (int(map_x + self_x), int(map_y + self_y)), 4)

    def draw_connection_status(self, screen, connected):
        """Draw connection status indicator"""
        status_text = "ONLINE" if connected else "OFFLINE"
        status_color = GREEN if connected else RED
        status = self.font_small.render(status_text, True, status_color)
        screen.blit(status, (WIDTH - 200, HEIGHT - 35))

    def draw_loading_screen(self, screen):
        """Draw initial loading/connecting screen"""
        screen.fill(DARK)
        
        title = self.font_large.render("NIGHTFALL PROTOCOL", True, ACCENT)
        subtitle = self.font_medium.render("Connecting to server...", True, TEXT_LIGHT)
        
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, HEIGHT // 2 + 20))

    def draw_death_screen(self, screen, rank, survivors):
        """Draw match over screen"""
        screen.fill((0, 0, 0, 150))
        
        title = self.font_large.render("ELIMINATED", True, RED)
        rank_text = self.font_medium.render(f"Rank: #{rank}", True, TEXT_LIGHT)
        survivors_text = self.font_small.render(f"Survivors: {survivors}", True, TEXT_GRAY)
        
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 80))
        screen.blit(rank_text, (WIDTH // 2 - rank_text.get_width() // 2, HEIGHT // 2))
        screen.blit(survivors_text, (WIDTH // 2 - survivors_text.get_width() // 2, HEIGHT // 2 + 50))
