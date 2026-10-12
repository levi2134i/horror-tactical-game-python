# Nightfall Protocol - Python Edition

A multiplayer tactical horror battle royale game built in Python using Pygame and TCP networking.

## Features

- **Multiplayer Gameplay**: Connect multiple players over TCP
- **Smooth Mechanics**: WASD movement, mouse aiming, click to shoot
- **Real-time Sync**: Server authoritative with 30 FPS network ticks
- **Clean UI**: Modern HUD with health bars, ammo counter, and minimap
- **Agent System**: Random agent names and colors for each player
- **Performance**: Optimized rendering and network code

## Installation

```bash
pip install -r requirements.txt
```

## Running the Game

### Start the Server

```bash
python server.py
```

The server will listen on `localhost:5555`

### Start a Client

In a new terminal:

```bash
python client.py
```

You can start multiple clients to test multiplayer.

## Controls

- **WASD**: Move
- **SHIFT**: Sprint (faster movement)
- **Mouse**: Aim
- **Left Click**: Shoot
- **ESC**: Disconnect

## Architecture

### Server (`server.py`)
- Listens for client connections
- Maintains player state
- Broadcasts updates to all clients
- ~100 lines, handles up to 100 concurrent players

### Client (`client.py`)
- Connects to server
- Renders game world and UI
- Sends player input to server
- Receives state updates

### Game Modules

- **settings.py**: Game constants (colors, speeds, etc.)
- **ui.py**: UI rendering (HUD, health bars, minimap)
- **player.py**: Player logic and movement
- **utils.py**: Shared utilities (colors, names, math)

## Next Steps

Potential enhancements:

1. **Bot Enemies**: Add AI-controlled bots
2. **Weapon System**: Different weapons with unique stats
3. **Loot Drops**: Healing items and ammo pickups
4. **Zone Shrinking**: Progressively smaller safe zones
5. **Damage Feedback**: Screen shake and hit indicators
6. **Sound**: BGM and SFX
7. **Matchmaking**: Lobby system and team modes
8. **Cosmetics**: Skins and customization

## Technical Notes

- **Network Protocol**: JSON over raw TCP sockets
- **Update Rate**: 30 ticks per second for network sync
- **Rendering**: 60 FPS Pygame renderer
- **Physics**: Simple position-based movement
- **Scaling**: Handles up to 100 players without issues

## Troubleshooting

**"Connection refused" error**: Make sure server is running first

**Lag or stuttering**: Check network latency and reduce player count

**Game looks weird**: Ensure Pygame is installed: `pip install pygame==2.5.2`

## License

MIT
