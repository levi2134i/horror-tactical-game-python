import math
from game.settings import PLAYER_SPEED, MAX_HP, SHOOTER_COOLDOWN

class Player:
    def __init__(self, player_id, name, x, y, color):
        self.id = player_id
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.hp = MAX_HP
        self.angle = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.shoot_cooldown = 0

    def update(self, keys, mouse_pos, dt, world_bounds):
        """Update player position and state"""
        # Movement
        move_x = 0
        move_y = 0
        
        if keys[pygame.K_w]:
            move_y -= 1
        if keys[pygame.K_s]:
            move_y += 1
        if keys[pygame.K_a]:
            move_x -= 1
        if keys[pygame.K_d]:
            move_x += 1
        
        # Normalize diagonal movement
        if move_x != 0 or move_y != 0:
            length = math.hypot(move_x, move_y)
            move_x /= length
            move_y /= length
        
        # Sprint modifier
        speed = PLAYER_SPEED
        if keys[pygame.K_LSHIFT]:
            speed *= 1.5
        
        # Apply velocity
        self.x += move_x * speed * dt
        self.y += move_y * speed * dt
        
        # Clamp to world
        min_x, max_x, min_y, max_y = world_bounds
        self.x = max(min_x, min(max_x, self.x))
        self.y = max(min_y, min(max_y, self.y))
        
        # Aiming
        mx = mouse_pos[0] - self.x
        my = mouse_pos[1] - self.y
        self.angle = math.degrees(math.atan2(my, mx))
        
        # Cooldowns
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt * 1000

    def shoot(self):
        """Try to shoot, return True if successful"""
        if self.shoot_cooldown <= 0:
            self.shoot_cooldown = SHOOTER_COOLDOWN
            return True
        return False

    def take_damage(self, damage):
        """Take damage and return True if dead"""
        self.hp = max(0, self.hp - damage)
        return self.hp <= 0

    def heal(self, amount):
        """Heal player"""
        self.hp = min(MAX_HP, self.hp + amount)

    def get_position(self):
        return (self.x, self.y)

    def to_dict(self):
        """Serialize to dict for network"""
        return {
            "id": self.id,
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "hp": self.hp,
            "angle": self.angle,
            "color": self.color
        }

import pygame
