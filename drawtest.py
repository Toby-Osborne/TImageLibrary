from PIL import Image
import timg
#index by (y,x)
dim = (1000,1000)
center = (500,500)
radius = 400

circleObj = []
dVector = []

with Image.new('L', dim) as im:
    points = timg.polyReg(center,radius,8)
    for point in points:
        im.putpixel(point,255)
    im.show()
