# Code Style Guide - Brawlers Arena

This document outlines coding standards and architectural principles for the Brawlers Arena refactor (2026+).

## Philosophy

Our codebase follows three core principles:

1. **SOLID**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
2. **KISS**: Keep It Simple, Stupid - Avoid unnecessary complexity
3. **Pygame Best Practices**: Leverage Pygame efficiently without over-engineering

---

## Project Structure

```
brawlers_arena/
├── src/
│   ├── core/              # Core game engine
│   │   ├── game.py        # Main game loop
│   │   ├── events.py      # Event handling
│   │   └── clock.py       # Timing and FPS control
│   ├── scenes/            # Game scenes/states
│   │   ├── menu.py
│   │   ├── character_selection.py
│   │   ├── map_selection.py
│   │   └── battle.py
│   ├── entities/          # Game objects
│   │   ├── player.py
│   │   ├── enemy.py
│   │   └── projectile.py
│   ├── systems/           # Game systems
│   │   ├── collision.py
│   │   ├── physics.py
│   │   ├── animation.py
│   │   └── sound.py
│   ├── graphics/          # Rendering
│   │   ├── renderer.py
│   │   ├── camera.py
│   │   └── ui.py
│   ├── input/             # Input handling
│   │   ├── keyboard.py
│   │   ├── joystick.py
│   │   └── input_manager.py
│   ├── config/            # Configuration
│   │   ├── constants.py
│   │   ├── settings.py
│   │   └── colors.py
│   ├── utils/             # Utilities
│   │   ├── loader.py      # Asset loading
│   │   ├── logger.py      # Logging
│   │   └── helpers.py     # Helper functions
│   └── main.py            # Entry point
├── tests/                 # Unit tests
├── assets/                # Game assets
│   ├── images/
│   ├── sounds/
│   └── fonts/
├── docs/                  # Documentation
└── requirements.txt
```

---

## Naming Conventions

### Files and Modules
- Use `snake_case` for filenames: `player_controller.py`, `collision_system.py`
- Keep filenames short and descriptive
- One main class per module

### Classes
- Use `PascalCase`: `PlayerCharacter`, `CollisionManager`, `EventHandler`
- Prefix abstract base classes with `Base`: `BaseEntity`, `BaseScene`
- Prefix interfaces/protocols with `I`: `IRenderable`, `ICollidable`

### Functions and Methods
- Use `snake_case`: `update_position()`, `handle_collision()`
- Use verb-first naming: `get_`, `set_`, `handle_`, `update_`, `render_`
- Private methods: prefix with `_`: `_calculate_damage()`

### Constants
- Use `UPPER_SNAKE_CASE`: `SCREEN_WIDTH`, `PLAYER_SPEED`, `MAX_HEALTH`
- Group related constants in modules

---

## SOLID Principles Applied

### 1. Single Responsibility Principle (SRP)
**Each class should have one reason to change.**

```python
# ❌ Bad: Multiple responsibilities
class Player:
    def update(self):
        self.x += self.vx
        self.health -= 1
        pygame.draw.rect(SCREEN, self.color, self.rect)
        
# ✅ Good: Separated concerns
class Player(BaseEntity):
    """Handles player state and logic."""
    def update(self, dt):
        self.move(dt)
        self.take_damage(dt)

class PlayerRenderer:
    """Handles only rendering."""
    def render(self, player, surface):
        pygame.draw.rect(surface, player.color, player.rect)
```

### 2. Open/Closed Principle (OCP)
**Classes should be open for extension, closed for modification.**

```python
# ❌ Bad: Adding new entity types requires modifying the system
class GameSystem:
    def update(self, entities):
        for entity in entities:
            if isinstance(entity, Player):
                entity.player_update()
            elif isinstance(entity, Enemy):
                entity.enemy_update()

# ✅ Good: New entity types work without modification
class BaseEntity:
    def update(self, dt):
        raise NotImplementedError

class Player(BaseEntity):
    def update(self, dt):
        self.move(dt)

class Enemy(BaseEntity):
    def update(self, dt):
        self.ai_move(dt)
```

### 3. Liskov Substitution Principle (LSP)
**Derived classes must be substitutable for their base classes.**

```python
# ✅ All entities can be updated the same way
entities = [player, enemy1, enemy2, projectile]
for entity in entities:
    entity.update(dt)  # Works for all because they inherit from BaseEntity
```

### 4. Interface Segregation Principle (ISP)
**Clients should depend on specific interfaces, not general ones.**

```python
# ❌ Bad: Large interface with unrelated methods
class IGameObject:
    def update(self): pass
    def render(self): pass
    def collide(self): pass
    def take_damage(self): pass
    def play_sound(self): pass

# ✅ Good: Segregated, specific interfaces
class IUpdateable:
    def update(self, dt): pass

class IRenderable:
    def render(self, surface): pass

class ICollidable:
    def collide(self, other): pass

class Player(IUpdateable, IRenderable, ICollidable):
    pass
```

### 5. Dependency Inversion Principle (DIP)
**Depend on abstractions, not concretions.**

```python
# ❌ Bad: Direct dependency on concrete class
class Game:
    def __init__(self):
        self.input_handler = KeyboardInputHandler()

# ✅ Good: Dependency injection via abstraction
class Game:
    def __init__(self, input_handler):
        self.input_handler = input_handler  # Could be Keyboard, Joystick, etc.
```

---

## KISS Principles Applied

### Keep Functions Small
- Maximum 20-30 lines per method
- One clear purpose per function
- Extract complex logic into helper methods

```python
# ❌ Too complex
def handle_collision(self, other):
    if isinstance(other, Enemy):
        self.health -= other.damage
        if self.health <= 0:
            self.alive = False
            self.play_death_sound()
            self.spawn_particles()
        self.knockback(other.velocity)
        self.play_hurt_sound()

# ✅ Simpler and more readable
def handle_collision(self, other):
    self.take_damage(other.damage)
    self.apply_knockback(other.velocity)
    self.play_hurt_sound()
```

### Avoid Deep Nesting
- Maximum 2-3 levels of nesting
- Use early returns/continue to reduce nesting

```python
# ❌ Deep nesting
if self.is_alive:
    if self.is_in_world:
        if self.collision_rect.colliderect(other.collision_rect):
            if other.is_enemy:
                self.take_damage(other.damage)

# ✅ Early returns
def try_collide(self, other):
    if not self.is_alive or not self.is_in_world:
        return
    if not self.collision_rect.colliderect(other.collision_rect):
        return
    if other.is_enemy:
        self.take_damage(other.damage)
```

### Prefer Composition Over Inheritance
- Use 1-2 levels of inheritance max
- Favor composition for adding behaviors

```python
# ❌ Deep inheritance hierarchy
class Character(Entity):
    pass

class Player(Character):
    pass

class Warrior(Player):
    pass

# ✅ Composition with behaviors
class Character(BaseEntity):
    def __init__(self, ai_system=None, attack_system=None):
        self.ai = ai_system
        self.attacks = attack_system
```

---

## Code Style

### Formatting
- **Indentation**: 4 spaces (no tabs)
- **Line Length**: Max 100 characters
- **Imports**: Group stdlib, third-party, local (PEP 8)

```python
# Standard imports
import sys
from typing import List, Optional

# Third-party imports
import pygame

# Local imports
from src.config.constants import SCREEN_WIDTH
from src.entities.player import Player
```

### Type Hints
- Use type hints for all function parameters and returns
- Use `Optional[]` for nullable values

```python
def calculate_damage(self, attacker: 'Player', defender: 'Enemy') -> int:
    base_damage: int = attacker.attack_power
    defense: int = defender.defense
    return max(0, base_damage - defense)

def get_nearest_entity(self, entities: List['Entity']) -> Optional['Entity']:
    if not entities:
        return None
    return min(entities, key=lambda e: self.distance_to(e))
```

### Docstrings
- Use docstrings for all classes and public methods
- Follow Google-style docstrings

```python
class Player(BaseEntity):
    """Represents a playable character.
    
    Attributes:
        health (int): Current health points.
        max_health (int): Maximum health points.
        position (tuple): Current (x, y) position.
    """
    
    def take_damage(self, amount: int) -> None:
        """Apply damage to the player.
        
        Args:
            amount: Damage amount to apply.
        """
        self.health = max(0, self.health - amount)
```

### Comments
- Avoid obvious comments
- Explain the "why", not the "what"
- Keep comments up-to-date

```python
# ❌ Obvious comment
x += 5  # Add 5 to x

# ✅ Explains intent
x += PLAYER_KNOCKBACK_DISTANCE  # Push player back after collision
```

---

## Pygame-Specific Guidelines

### Sprite Management
- Use Pygame sprite groups for efficient updates
- Keep sprite groups organized by type

```python
class Scene:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        
    def update(self, dt):
        self.all_sprites.update(dt)
        
    def render(self, surface):
        self.all_sprites.draw(surface)
```

### Event Handling
- Centralize event handling in an EventManager
- Use custom events for game-specific logic

```python
class EventManager:
    def __init__(self):
        self.player_damaged = pygame.USEREVENT + 1
        self.enemy_defeated = pygame.USEREVENT + 2
        
    def emit_player_damaged(self):
        pygame.event.post(pygame.event.Event(self.player_damaged))
```

### Performance
- Use dirty rect updates for efficient rendering
- Profile before optimizing
- Batch similar operations together

```python
# Batch updates
for entity in self.entities:
    entity.update(dt)

# Single draw call for all
self.all_sprites.draw(self.screen)
```

---

## Testing Guidelines

- Write unit tests for logic-heavy classes
- Use mocking for external dependencies (Pygame)
- Aim for 70%+ code coverage

```python
# tests/test_player.py
import unittest
from src.entities.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(x=0, y=0)
        
    def test_take_damage(self):
        initial_health = self.player.health
        self.player.take_damage(10)
        self.assertEqual(self.player.health, initial_health - 10)
        
    def test_health_cannot_go_below_zero(self):
        self.player.take_damage(1000)
        self.assertEqual(self.player.health, 0)
```

---

## Configuration Management

- Use `constants.py` for all magic numbers
- Use `settings.py` for user-configurable values
- Never hardcode values in game logic

```python
# ✅ Good
from src.config.constants import PLAYER_SPEED, SCREEN_WIDTH

class Player:
    def move(self, dt):
        self.x += PLAYER_SPEED * dt
```

---

## Error Handling

- Use try-except for external operations (file I/O, Pygame init)
- Log errors appropriately
- Fail gracefully with meaningful messages

```python
def load_image(path: str) -> pygame.Surface:
    """Load image from path.
    
    Args:
        path: Path to image file.
        
    Returns:
        Loaded pygame Surface.
        
    Raises:
        FileNotFoundError: If image file not found.
    """
    try:
        return pygame.image.load(path)
    except pygame.error as e:
        logger.error(f"Failed to load image {path}: {e}")
        raise FileNotFoundError(f"Image not found: {path}")
```

---

## Git Workflow

### Branch Naming
- `feature/` - New features
- `bugfix/` - Bug fixes
- `refactor/` - Code refactoring
- `docs/` - Documentation updates

### Commit Messages
- Use imperative mood: "Add feature" not "Added feature"
- Keep first line under 50 characters
- Provide detailed explanation in body if needed

```
Add player collision detection

Implement AABB collision system for player-enemy interactions.
Detects collisions frame-by-frame and triggers damage events.
```

---

## Checklist Before Committing

- [ ] Code follows naming conventions
- [ ] No hardcoded values (use constants)
- [ ] Functions have type hints
- [ ] Complex functions have docstrings
- [ ] No unused imports
- [ ] No commented-out code
- [ ] Unit tests added/updated
- [ ] No obvious performance issues
- [ ] Code follows SOLID principles

---

## Resources

- [PEP 8 - Style Guide for Python](https://www.python.org/dev/peps/pep-0008/)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
