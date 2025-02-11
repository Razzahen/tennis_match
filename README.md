# Tennis Scoring System

A Python implementation of a tennis scoring system that handles regular games, sets, and tie-breaks according to standard tennis rules.

## Overview

This system accurately models tennis scoring rules, including:

- Regular game scoring (0, 15, 30, 40, Deuce, Advantage)
- Set scoring with tie-breaks
- Complete match state tracking

## Components

### Game (Abstract Base Class)

The foundation of the scoring system, defining the basic structure for all game types:

#### Regular Game

Handles standard tennis game scoring with:

- Traditional point system (0, 15, 30, 40)
- Deuce and advantage rules
- Win by two points rule

#### Tie-Break Game

Implements tie-break specific rules:

- Points counted normally (1, 2, 3, etc.)
- First to 7 points with 2-point lead wins

#### Set

Manages the overall set structure:

- Tracks games won by each player
- Handles transition to tie-break at 6-6
- Enforces win by two games rule
- Manages set completion rules

## Usage

## Testing

The system includes comprehensive unit tests covering:

- Regular game scoring
- Deuce and advantage situations
- Set completion scenarios
- Tie-break handling

Run tests using:

```bash
python -m unittest
```
