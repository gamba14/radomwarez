# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# MODO DE USO: Ejecute por consola el siguiente comando python pat.py <patente>
# donde <patente> no debe contener espacio entre letras y numeros
# es importante tener instalado python.
#
# gambirassi.a@gmail.com Agustin Gambirassi 2017
#!/usr/bin/env python
import sys
from functools import reduce
pat = {
       'A':14, 'B':1, 'C':0, 'D':16, 'E':5, 'F':20,
       'G':19, 'H':9, 'I':24, 'J':7, 'K':21, 'L':8,
       'M':4, 'N':13, 'O':25, 'P':22, 'Q':18, 'R':10,
       'S':2, 'T':6, 'U':12, 'V':23, 'W':11, 'X':3,
       'Y':15, 'Z':17
       }
def main():
      if len(sys.argv)==2:
        tgt = sys.argv[1].upper()
        #tgt = input('ingrese patente sin espacios\n').upper()
        comp = []
        #Obtengo lista de numeros
        for let in tgt:
            try:
                if pat[let] >= 10:
                    comp = comp+list(divmod(pat[let],10))
                else:
                     comp.append(0)
                     comp.append(pat[let])
            except:
                comp.append(int(let))
        #Realizo la operacion para obtener DV
        #Busco el digito de la izquierda
        idx = len(comp)
        dv2= 0
        for numero in range(0,idx,2):
            dv2 += comp[numero]
        if dv2 >= 10:
            temp1 = list(divmod(dv2,10))
            dv2 = reduce ((lambda x,y: x+y),temp1)
            if dv2 == 10: dv2=1
        #Busco el digito de la derecha
        dv1= 0
        for numero in range(1,idx-1,2):
            dv1 += comp[numero]
        if dv1 >= 10:
            temp1 = list(divmod(dv1,10))
            dv1 = reduce ((lambda x,y: x+y),temp1)
            if dv1 == 10: dv1=1
        print('el digito verificador para el dominio '+tgt+' es '+ str(dv2)+str(dv1))

if __name__ == '__main__':

   main()

