import turtle as t
from random import random
from math import sqrt

def brown (x0,y0,x1,y1, disp, p, n=5, m=400):
     ''' Рекурсивная функция построения Броуновского моста.
     Параметры:
     x0, y0, x1, y1 - координаты двух точек
     disp -дисперсия
     p - плавность
     n - глубина рекурсии
     m - масштаб

     xm, ym - координаты середины
     delta - смещение
     '''
     if n==0:
          t.penup()
          t.goto(x0*m-m/2,y0*m-m/2)
          t.pendown()
          t.goto(x1*m-m/2,y1*m-m/2)
          return
     xm=(x0+x1)/2.0
     ym=(y0+y1)/2.0
     delta_x = random()*sqrt(disp)
     delta_y = random() * sqrt(disp)
     brown(x0,y0,xm+delta_x,ym+delta_y, disp/p, p, n-1)
     brown(xm+delta_x,ym+delta_y, x1, y1, disp/p, p, n-1)

def main():
     h=0.5
     a = 2.0**(2.0*h)
     brown(-0.3, -0.2, -0.1, 0.4, 0.01, a)
     brown(-0.1, 0.4, -0.5, 0.4, 0.01, a)
     brown(-0.5, 0.4, -0.5, 0.9, 0.01, a)
     brown(-0.5, 0.9, -0.1, 0.1, 0.01, a)
     brown(-0.1, 0.1, -0.2, 0.3, 0.01, a)
     brown(-0.2, 0.3, -0.3, -0.2, 0.01, a)



     t.exitonclick()
if __name__ == '__main__':
    main()