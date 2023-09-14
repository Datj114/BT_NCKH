import numpy as np
import matplotlib.pyplot as plt
vector_a=np.array([1,2,3])
vector_b=np.array([11,4,4])
vector_sum=vector_a + vector_b

#tạo không gian
# fig=plt.figure()
# ax=fig.add_subplot(projection='3d')
ax=plt.figure().add_subplot(projection='3d')
#vẽ vector
ax.quiver(0,0,0,vector_a[0],vector_a[1],vector_a[2],color='b',label='vector a')
ax.quiver(vector_a[0],vector_a[1],vector_a[2],vector_b[0],vector_b[1],vector_b[2],color='r',label='vector b')
ax.quiver(0,0,0,vector_sum[0],vector_sum[1],vector_sum[2],color='g',label='vector sum')

#giới hạn trục
ax.set_xlim(0,15)
ax.set_ylim(0,15)
ax.set_zlim(0,15)

#đặt nhãn trục
ax.set_xlabel('truc x')
ax.set_ylabel('truc y')
ax.set_zlabel('truc z')

plt.legend()
plt.show()

