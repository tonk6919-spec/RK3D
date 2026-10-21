def cyrus_beck(p0, p1, polygon):
    n = len(polygon)
    area = sum(polygon[i][0] * polygon[(i + 1) % n][1] -
               polygon[(i + 1) % n][0] * polygon[i][1] for i in range(n))
    poly = polygon if area > 0 else polygon[::-1]

    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    t_in, t_out = 0.0, 1.0

    for i in range(n):
        vx, vy = poly[i]
        wx, wy = poly[(i + 1) % n]
        nx, ny = -(wy - vy), wx - vx                    

        num = nx * (p0[0] - vx) + ny * (p0[1] - vy)     
        den = nx * dx + ny * dy                         

        if den == 0:                                    
            if num < 0:
                return None
            continue

        t = -num / den
        if den > 0:
            t_in = max(t_in, t)
        else:
            t_out = min(t_out, t)
        if t_in > t_out:
            return None

    return ((p0[0] + t_in * dx, p0[1] + t_in * dy),
            (p0[0] + t_out * dx, p0[1] + t_out * dy))
            
            
            
square = [(0, 0), (4, 0), (4, 4), (0, 4)]

#Отрезок пересекает квадрат насквозь
print(cyrus_beck((-2, 2), (6, 2), square))

#Один конец внутри, другой снаружи
print(cyrus_beck((2, 2), (8, 2), square))


