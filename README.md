# Asteroids Game

This is a simple implementation of the classic Asteroids game using Pygame.

## Features

* Player spaceship with movement and shooting capabilities.
* Asteroids of various sizes that split into smaller ones when shot.
* Collision detection between player and asteroids, and shots and asteroids.

## Installation

1. Make sure you have Python installed.
2. Install Pygame:
   ```bash
   pip install pygame
   ```

## How to Run

1. Clone this repository or download the source code.
2. Navigate to the project directory in your terminal.
3. Run the game:
   ```bash
   python main.py
   ```

## Gameplay

* Use the **arrow keys** to move your spaceship.
* Press the **spacebar** to shoot.
* Avoid colliding with asteroids.
* Shoot asteroids to destroy them and earn points (scoring system to be implemented).

## Project Structure

* `main.py`: The main game loop and initialization.
* `player.py`: Defines the Player class.
* `asteroid.py`: Defines the Asteroid class.
* `asteroidfeild.py`: Manages the asteroid field.
* `shot.py`: Defines the Shot class.
* `constants.py`: Contains game constants like screen dimensions.
* `circleshape.py`: for handling circular collision detection and drawing


