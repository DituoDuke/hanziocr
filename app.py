from screenshot import capture_region

top = int(input("cima: "))
left = int(input("esquerda: " ))
right = int(input("direita: " ))
down = int(input("baixo: "))


capture_region(left,top,right,down)