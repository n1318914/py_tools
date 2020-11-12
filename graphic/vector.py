import numpy as np


# vector angle
# return angle 角度, is Clockwise 是否顺时针
# 计算两个二维向量的夹角和 方向
def v_angle(x, y):
    dot = np.inner(x,y)
    a = np.linalg.norm(x)
    b = np.linalg.norm(y)
    l = np.arccos(dot / (a * b))
    d = np.around(np.degrees(l))
    c = np.cross(x,y) < 0
    return d, c

if __name__ == '__main__':
    a = np.array([-4,4])
    b = np.array([-4,0])
    print(v_angle(a,b))