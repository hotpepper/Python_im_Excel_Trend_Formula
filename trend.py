
               
def LeastSquaresValueAtX(points, knownX, xBar, x):
    '''
        Gets the value at a given x using the line of best fit
        (least square method) to determine the equation
    '''
    slope = SlopeOfPoints(points, knownX, xBar)
    yIntercept = YInterceptOfPoints(points, xBar, slope)
    return (slope * x) + yIntercept

def SlopeOfPoints(points, knownX, xBar):
    '''
        Gets the slope for a set of points using the formula:
        m=sum(x-avg(x)(y-avg(y))/sum(x-avg(x))**2
    '''
    yBar=dividend=divisor=0.0
    for i in points:
        yBar=yBar+i
    yBar=yBar/5
    for j in points:
        kx = knownX.pop()
        dividend+=((kx-xBar)*(j-yBar))
        divisor+=((kx-xBar)**2)
    return dividend / divisor      

def YInterceptOfPoints(points, xBar, slope):
    '''
        Gets the y-intercept for a set of points using the formula:
        b-avg(y)-m(avg(x))
    '''
    yBar =0.0
    for i in points:
        yBar=yBar+i
    yBar=yBar/5
    return yBar - (slope * xBar)



def test(knownX, t):
    if t==1: return LeastSquaresValueAtX([4,13,10,22,20],[2011,2010,2009,2008,2007],2009,2012)
    if t==2: return LeastSquaresValueAtX([7,20,26,29,23],knownX, 2009,2012)
    if t==3: return LeastSquaresValueAtX([6,5,4,3,7], knownX, 2009,2012)
    

print test([2011,2010,2009,2008,2007], 1)##26.1
print test([2011,2010,2009,2008,2007], 2)##33.3
print test([2011,2010,2009,2008,2007], 3)##5.0
