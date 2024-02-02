#-----Correcto-------------------------------------------Incorrecto-----#
def negate(num):                                    #def negate(num):
    return -num                                         #return -num
def large_num(num):                                 #def large_num(num):
    return num > 10000                                  #res = (num > 100000)

b = 9000                                            #negate(b)
neg_b = negate(b)                                   #neg_b = num
print("b:", b, "neg_b:", neg_b)                     #print "b:", b, "neg_b:",neg_b

big = large_num(b)                                  #big = large_num(b)
print("b in big:", big)                             #print "b in big:",big


#1. Definir un valor para b
#2. Llamar a la función negate con el valor de b y asignar el resultado a neg_b
#3. Llamar a la función large_num con el valor de b y asignar el resultado a big

## Desarrollado por Eduar Damian Chanaga GOnzalez - 1095581647
