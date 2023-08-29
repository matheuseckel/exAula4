from enum import Enum
import math


class Directions(Enum):
    ESQUERDA = -1
    DIREITA = 1


def moveTrain(commands, initialPosition=0, begin=-math.inf, end=math.inf):
    if len(commands) > 30:
        return "Dá não"

    currentPosition = initialPosition

    for command in commands:
        if (currentPosition > begin and currentPosition < end):
            currentPosition += command.value

    return currentPosition


print(moveTrain(commands=[Directions.ESQUERDA,
      Directions.ESQUERDA], initialPosition=0))
print(moveTrain(commands=[Directions.ESQUERDA,
      Directions.DIREITA], initialPosition=1, begin=-2))
print(moveTrain(commands=[Directions.DIREITA,
      Directions.ESQUERDA], initialPosition=1, begin=-2, end=10))
