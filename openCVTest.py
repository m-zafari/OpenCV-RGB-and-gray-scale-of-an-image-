
import cv2
import numpy as np





img = cv2.imread('original.jpg') # Combination of all colors

b,g,r = cv2.split(img)       # get b,g,r
rgb_img = cv2.merge([r,g,b])
x,y,z = np.shape(img)
print(x, y, z)

red = np.zeros((x,y,z),dtype=int)
green = np.zeros((x,y,z),dtype=int)
blue = np.zeros((x,y,z),dtype=int)

for i in range(0,x):
    for j in range(0,y):
        blue[i][j][0] = rgb_img[i][j][0]
        green[i][j][1]= rgb_img[i][j][1]
        red[i][j][2] = rgb_img[i][j][2]
 
cv2.imwrite('Red.jpg',red)
cv2.imwrite('Green.jpg',green)
cv2.imwrite('Blue.jpg',blue)


retrack_original = np.zeros((x,y,z),dtype=int)
for i in range(0,x):
    for j in range(0,y):
        retrack_original[i][j][0] = red[i][j][2]
        retrack_original[i][j][1] = green[i][j][1]
        retrack_original[i][j][2] = blue[i][j][0]

cv2.imwrite('retrack_original.jpg',retrack_original)

gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imwrite('GrayScale.jpg',gray_image)

# RGB to Gray:Y = (0.299 * R) + (0.587 * G) + (0.114 * B)
test_gray = np.zeros((x,y,z),dtype=int)
for i in range(0,x):
    for j in range(0,y):
        test_gray[i][j][0:3] = 0.299 * red[i][j][2] + 0.587 * green[i][j][1] + 0.114 * blue[i][j][0]

cv2.imwrite('TestGray.jpg',test_gray)