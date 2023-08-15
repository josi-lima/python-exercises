import math

# Crie um programa que permite calcular a área e o perímetro de um círculo.

# O programa deve pedir à pessoa usuária para inserir o raio do círculo e, em seguida, exibir na tela a área e o perímetro do círculo.

# O valor de π é 3,141593.
# A fórmula para calcular a área de um círculo é π vezes o raio ao quadrado.
# A fórmula para calcular o perímetro é 2 vezes π vezes o raio.

def Circle():
  radius = float(input('Please, insert the radius of a circle: '))
  
  # using the math module
  pi = float(format(math.pi,'2f'))
  print(pi)  # 3.141593
    
  area = round((pi * radius ** 2), 2)
  perimeter = round((2 * pi * radius), 2)

  print(f'The area of the circle is {area}.') 
  print(f'The perimeter of the circle is {perimeter}.')  

Circle()

# ===========================================================
