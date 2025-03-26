import cv2

# The Configurable Parameter
source = "HHHH (1).png"
des = 'new_image2.jpeg'
scale_pr = 50

src = cv2.imread(source,cv2.IMREAD_UNCHANGED)
#cv2.imshow("title",src)

# now calculate the 60 percent of org dimension
new_width = int(src.shape[1] * scale_pr /100)
new_height = int(src.shape[0] * scale_pr /100)
# resize image
out = cv2.resize(src,(new_width,new_height))
cv2.imwrite(des,out)
cv2.waitKey(0)