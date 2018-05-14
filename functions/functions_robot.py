# funtions_robot.py

def dh(theta, d, a, alpha):
	#
	# Retorna a matriz transformação homogenea entre juntas sucessivas
	# Os parâmetros de entrada estão de acordo com a convecão de Denavit-Hartenberg
	#
	A=[cos(theta)  -cos(alpha)*sin(theta)   sin(alpha)*sin(theta)   a*cos(theta);
       sin(theta)   cos(alpha)*cos(theta)  -sin(alpha)*cos(theta)   a*sin(theta);
       0                 sin(alpha)             cos(alpha)               d      ;
       0                     0                     0                     1      ]
    return A
#Fim da função DH

__version__ = '0.1'
__name__ = 'kinematics funtions'