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

    return "Resultado: " + str(currentPosition)


print(moveTrain(commands=[Directions.ESQUERDA,
      Directions.ESQUERDA, Directions.ESQUERDA, Directions.ESQUERDA, Directions.ESQUERDA], initialPosition=0))
print(moveTrain(commands=[Directions.ESQUERDA,
      Directions.ESQUERDA, Directions.ESQUERDA, Directions.ESQUERDA, Directions.ESQUERDA], initialPosition=1, begin=-2))

commands = []
i = 0
while i < 30:
    i += 1
    result = input("Direção " + str(i) + ": ")
    if (result == "DIREITA"):
        commands.append(Directions.DIREITA)
    elif (result == "ESQUERDA"):
        commands.append(Directions.ESQUERDA)
    elif (result == "FIM"):
        break

initialPosition = int(input("Posição inicial: "))
begin = int(input("Começo: "))
end = int(input("Fim: "))
print(moveTrain(commands, initialPosition, begin, end))
