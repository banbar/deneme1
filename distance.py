# We have to test this!
# Link to Postgres
import math
from math import atan
from math import atan2
from math import cos
from math import radians
from math import sin
from math import sqrt
from math import tan
from math import asin
def oklid(lat1,lon1,lat2,lon2):
    result=sqrt((lat1-lat2)**2+(lon1-lon2)**2)
    print("oklid distance:",result,"meter")
#Haversine represents the world like sphere
def Haversine(lat1,lon1,lat2,lon2):
    r=6371000 #metre
    
    lat1=math.radians(lat1)
    lat2=math.radians(lat2)
    lon1=math.radians(lon1)
    lon2=math.radians(lon2)

    d=sqrt((sin((lat2-lat1)/2)**2)+cos(lat1)*cos(lat2)*(sin((lon2-lon1)/2)**2))
    result=2*r*asin(d)

    print("result:",result,"meter")
    

    a=sin((lat1-lat2)/2)**2+(cos(lat1)*cos(lat2)*(sin((lon2-lon1)/2)**2))
    c=2*atan2(sqrt(a),sqrt(1-a))
    d=r*c

    print("distance:",d,"meter")
#Haversine represents the world like ellipsoid
def Vincenty(lat1,lon1,lat2,lon2):
    lat1=math.radians(lat1)
    lat2=math.radians(lat2)
    lon1=math.radians(lon1)
    lon2=math.radians(lon2)
    #WGS84 Parameters
    f=1/298.257223563
    a=6378137 #meter
    b=6356752.314245 #meter
    #Other Constants
    U1=atan((1-f)*tan(lat1))
    U2=atan((1-f)*tan(lat2))
    L=lon2-lon1
    Lamb=L
    
    sin_u1=sin(U1)
    cos_u1=cos(U1)
    sin_u2=sin(U2)
    cos_u2=cos(U2)
    #iteration
    while 1:
        sin_lamb=sin(Lamb)
        cos_lamb=cos(Lamb)

        sin_sig=sqrt((cos_u2*sin_lamb)**2+(cos_u1*sin_u2-sin_u1*cos_u2*cos_lamb)**2)
        cos_sig=sin_u1*sin_u2+cos_u1*cos_u2*cos_lamb
        sigma=atan2(sin_sig,cos_sig)

        sin_alpha=(cos_u1*cos_u2*sin_lamb)/sin_sig
        cos_squ_alpha=1-(sin_alpha**2)
        cos_2sig=cos_sig-(2*sin_u1*sin_u2)/cos_squ_alpha

        C=(f/16)*cos_squ_alpha*(4+f*(4-3*cos_squ_alpha))

        pre_Lamb=Lamb
        Lamb=L+(1-C)*f*sin_alpha*(sigma+C*sin_sig*(cos_2sig+C*cos_sig*(-1+2*(cos_2sig**2))))
        if abs(pre_Lamb-Lamb)<10**-12:
            break
        
    u_square=cos_squ_alpha*((a**2-b**2)/b**2)
    A=1+u_square/16384*(4096+u_square*(-768+u_square*(320-175*u_square)))
    B=(u_square/1024)*(256+u_square*(-128+u_square*(74-47*u_square)))
    delta_sig=B*sin_sig*(cos_2sig+0.25*B*(cos_sig*(-1+2*cos_2sig**2)-(B/6)*cos_2sig*(-3+4*sin_sig**2)*(-3+4*cos_2sig**2)))

    S=b*A*(sigma-delta_sig)
    print("Vincenty=",S,"meter")

    

#Example 1 (Ankara)
print("Example 1")
oklid(4425972.428590606,-523286.7999742433,4420039.971459754,-510336.1321717317)
Haversine(39.967648,32.727430,39.914476,32.879110)
Vincenty(39.967648,32.727430,39.914476,32.879110)
#example 2
print("Example 2")
Vincenty(37.95083333,144.4248679,37.65282114,143.9264955) #54972.71 meter
#example 3
print("Example 3")
oklid(4628502.681691515,-194210.6107193170,4617749.242036330,-589755.6303796207)
Haversine(41.49008, -71.312796,41.499498, -81.695391)
Vincenty(41.49008, -71.312796,41.499498, -81.695391) #866455.4329158525 meter
#example 4
#-73.993896484375,40.750110626220703,-73.974784851074219,40.750617980957031
#close distance, real data
print("Example 4")
oklid(-8215434.074834888,553858.2687813015,-8213302.364820029,553936.4903558953)
Haversine(-73.993896484375,40.750110626220703,-73.974784851074219,40.750617980957031)
Vincenty(-73.993896484375,40.750110626220703,-73.974784851074219,40.750617980957031)
#example 5 long distance
#41.902277,87.258789,65.874725,16.626573
print("Example 5")
oklid(4640814.946133788,521465.0579780309,7309831.648756316,574179.8908168557)
Haversine(41.902277,87.258789,65.874725,16.626573)
Vincenty(41.902277,87.258789,65.874725,16.626573)
#example 6
#long distance
print("Example 6")
oklid(-8215434.074834888,553858.2687813015,7309831.648756316,574179.8908168557)
Haversine(-73.993896484375,40.750110626220703,65.874725,16.626573)
Vincenty(-73.993896484375,40.750110626220703,65.874725,16.626573)








