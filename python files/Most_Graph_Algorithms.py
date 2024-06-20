class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        
        
def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y

def is_on_segment(p, a, b):
    """
        returns ture if the point p lies on line from a to b
    """
    area = signed_area(p,a,b)
    if area == 0:
        test = (p-a).lensq() <= (a-b).lensq()and (p-b).lensq() <= (a-b).lensq()
        return test
    return False
    
#a = Vec(1000, 2000)
#b = Vec(0, 0)
#p = Vec(500, 1000)
#print(is_on_segment(p, a, b))

#a = Vec(0, 0)
#b = Vec(1000, 2000)
#point_tuples = [
    #(-1, -1),
    #(-1, -2),
    #(-1000, -2000),
    #(0, 0),
    #(1, 2),
    #(500, 1000),
    #(500, 1001),
    #(500, 999),
    #(1000, 2000),
    #(1001, 2001),
    #(1001, 2002),
    #(2000, 4000)]
#points = [Vec(p[0], p[1]) for p in point_tuples]
#for p in points:
    #print(p, is_on_segment(p, a, b))
    
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise."""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area > 0
    
def classify_points(line_start, line_end, points):
    """
        returns a tuple the first element is the number of points the lie
        on the right of the given line, the second is the number of points 
        they lie on the left of the given line
    """
    right = 0
    left = 0
    for items in points:
        area = is_ccw(line_start, line_end, items)
        if area == True:
            left += 1
        elif area == False:
            right += 1
            
    return (right, left)
    

#points = [
    #Vec(1, 99),
    #Vec(0, 100),
    #Vec(50, 0),
    #Vec(50, 1),
    #Vec(50, 99),
    #Vec(50, 50),
    #Vec(100, 100),
   #Vec(99, 99)]
#print(classify_points(Vec(0, 49), Vec(100, 49), points))

def intersecting(a, b, c, d):
    """
        returns True if the line segment from a to b intersects the line
        segment for c to d
    """

    if is_ccw(c, a, d) == is_ccw(c, b, d):
        return False
    elif is_ccw(a, d, b) != is_ccw(a, c, b):
        return True    
    else:
        return False

#a = Vec(0, 0)
#b = Vec(100, 0)
#c = Vec(101, 1)
#d = Vec(101, -1)
#print(intersecting(a, b, c, d))

#a = Vec(0, 0)
#b = Vec(100, 0)
#c = Vec(99, 1)
#d = Vec(99, -1)
#print(intersecting(a, b, c, d))

#a = Vec(-1000, -999)
#b = Vec(1000, 1001)
#d = Vec(1, 0)
#c = Vec(1, -3)
#print(intersecting(a, b, c, d))

def is_strictly_convex(vertices):
    """
        returns True of and only if the vertices, taken in the given order
        define a strictly-convex counter-clockwisw polygon. Else return false
    """
    prev = None
    current = None
    after = None
    result = None
    for items in range(len(vertices)+2):
             
        if prev == None:
            prev = vertices[items%len(vertices)]
        elif current == None:
            current = vertices[items%len(vertices)]
        elif after == None:
            after = vertices[items%len(vertices)]
        if prev != None and current != None and after != None:
            result = is_ccw(prev, current, after)
            if result == False:
                return False
            else:
                prev = current
                current = after
                after = None
    return result  
#verts = [
    #(0, 0),
    #(100, 0),
    #(100, 100),
    #(0, 100)]
#points = [Vec(v[0], v[1]) for v in verts]
#print(is_strictly_convex(points))

#verts = [
    #(0, 0),
    #(0, 100),
    #(100, 100),
    #(100, 0)]
#points = [Vec(v[0], v[1]) for v in verts]
#print(is_strictly_convex(points))

#verts = [
    #(60, 60),
    #(100, 0),
    #(100, 100),
    #(0, 100)]
#points = [Vec(v[0], v[1]) for v in verts]
#print(is_strictly_convex(points))





def gift_wrap(points):
    """ Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most point (and left-most if necessary).
    assert len(points) >= 3
    bottommost = min(points, key=lambda p: (p.y, p.x))
    hull = [bottommost]
    done = False
    
    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull
        for p in points:
            if p is hull[-1]:
                continue
            if candidate == None or is_ccw(candidate, hull[-1], p ):
                candidate = p
        if candidate is bottommost:
            done = True    # We've closed the hull
        else:
            hull.append(candidate)

    return hull

points = [
    Vec(1, 99),
    Vec(0, 100),
    Vec(50, 0),
    Vec(50, 1),
    Vec(50, 99),
    Vec(50, 50),
    Vec(100, 100),
   Vec(99, 99)]
verts = gift_wrap(points)
for v in verts:
    print(v)


#points = [
    #Vec(1, 1),
    #Vec(99, 1),
    #Vec(100, 100),
    #Vec(99, 99),
    #Vec(0, 100),
    #Vec(100, 0),
    #Vec(1, 99),
    #Vec(0, 0),
    #Vec(50, 50)]
#verts = gift_wrap(points)
#for v in verts:
    #print(v)
        
class PointSortKey:
    """A class for use as a key when sorting points wrt bottommost point"""
    def __init__(self, p, bottommost):
        """Construct an instance of the sort key"""
        self.direction = p - bottommost
        self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost
        
    def __lt__(self, other):
        """Compares two sort keys. p1 < p2 means the vector the from 
        bottommost point
           to p2 is to the left of the vector from the bottommost to p1.
        """
        if self.is_bottommost:
            return True   # Ensure bottommost point is less than all other points
        elif other.is_bottommost:
            return False  # Ensure no other point is less than the bottommost
        else:
            area = self.direction.x * other.direction.y - other.direction.x * self.direction.y
            return area > 0
        
        
        
def simple_polygon(points):
    """
        selects the bottom most vert as an start point, then sorts the verts
        in oder of smallest angle to biggest starting from the start point to 
        the right most vert
    """
    
    bottommost = min(points, key=lambda p: (p.y, p.x))
    
    return sorted(points, key=lambda p: PointSortKey(p, bottommost))


#points = [
    #Vec(100, 100),
    #Vec(0, 100),
    #Vec(50, 0)]
#verts = simple_polygon(points)
#for v in verts:
    #print(v)
    
#print("******************")

#points = [
    #Vec(100, 100),
    #Vec(0, 100),
    #Vec(100, 0),
    #Vec(0, 0),
    #Vec(49, 50)]
#verts = simple_polygon(points)
#for v in verts:
    #print(v)    
    
def graham_scan(points):

    sorted_list = simple_polygon(points)
    first_3 = sorted_list[0:3]

    for i in range(3, len(sorted_list)):
        while not is_ccw(first_3[-2], first_3[-1], sorted_list[i]):
            first_3.pop()
        first_3.append(sorted_list[i])
        
    return first_3

    