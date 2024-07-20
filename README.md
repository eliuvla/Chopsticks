# Chopsticks

## Game description:

Chopsticks is a hand game which has differents variations, so in this projecto the game rules are the follow:

- It's a turn-based game
- It's a two player game
- Each player have 2 hands
- Both playes start with one finger in each hand


- notation: a dead hand is when it have 0 finger in it 

## In your's turn you can do only one of the two accions:

- attack: escoge una mano tuya y una de tu rival (no muertas) agrégale el número de dedos de tu mano a la del rival módulo 5.
- split: Si tienes una mano muerta y en la otra tienes un número par de dedos, puedes mandar la mitad de tus dedos a la otra mano (ambas manos tendrá la misma cantidad de dedos).

## How to win:

- A player wins when the other have simultaneously 2 dead hands
