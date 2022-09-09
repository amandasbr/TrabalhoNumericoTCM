import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


#Seleção do problema:
print("Selecione o problema 1, 2 ou 3")
Problema=input('Problema:')

#Definição de variáveis
alpha=1
N = 100 #300
L = 1.0
dx = L/N
dt= 0.2*dx*dx
t=float(input("Instante de tempo:"))
k_final = int(t//dt)
T = np.zeros((N+1,k_final), float) 

#Condições iniciais e de contorno:
if Problema=='1':
  T[:,0]+=1
  T[0,:]=0.0
  T[N,:]=0.0
elif Problema=='2':
  T[0,:]=1.0
  T[N,:]=0.0
elif Problema=='3':
  T[:,0]+=np.sin(0.5)
  T[0,:]=0.0
  T[N,:]=0.0

#Criação dos vetores para plotar
x=np.linspace(0.0,L,N+1) 
temp=np.linspace(0,k_final*dt,k_final)

#Equação para solução numérica aplicada
for k in range (0,k_final-1):
    for i in range (1, N) :
      T [ i,k+1 ] = T[i,k] + (alpha*(dt/(dx*dx))) * (T[i+1,k]-2.0*T[i,k] + T[i-1,k])

#Plot2D 
fig = plt.figure( )
ax = fig.add_subplot( )

fig.suptitle( 'Instante de Tempo = %.3f' %t , fontsize=18, fontweight='bold' )
ax.set_ylabel( '$T$' , fontsize=18)
ax.set_xlabel( '$x$' , fontsize=18)
  
plt.plot( x , T[:,k_final-1], '-r' , lw = 2 )
plt.show( )

#Plot3D
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

X,Y = np.meshgrid(temp,x)

surf = ax.plot_surface(X,Y,T,cmap=cm.jet, linewidth=20)

fig.colorbar(surf, shrink=0.5, aspect=10)

ax.set_xlabel('Tempo',fontsize=9)
ax.set_ylabel('Comprimento de barra', fontsize=9)
ax.set_zlabel('Temperatura',fontsize=9)

plt.show()


