import random
from game.settings import ACCENT, RED, GREEN, BLUE, YELLOW

AGENT_COLORS = [
    (200, 100, 255),  # Purple
    (100, 200, 255),  # Cyan
    (100, 255, 150),  # Green
    (255, 200, 100),  # Orange
    (255, 100, 150),  # Pink
]

AGENT_NAMES = [
    "Shadow",
    "Veil",
    "Wraith",
    "Phantom",
    "Specter",
    "Echo",
    "Null",
    "Void",
    "Silent",
    "Ghost",
]

def get_random_agent_name():
    return random.choice(AGENT_NAMES)

def get_random_agent_color():
    return random.choice(AGENT_COLORS)

def distance_between(pos1, pos2):
    """Calculate distance between two positions"""
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    return (dx**2 + dy**2)**0.5

def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))
