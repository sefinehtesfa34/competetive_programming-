import cv2 as cv
sefi=cv.imread("C:/Users/tesfasefineh34/Desktop/sefi.jpg")
sami=cv.imread("C:/Users/tesfasefineh34/Desktop/sami.jpg")
brothers=cv.vconcat([sami,sefi])
cv.imwrite("C:/Users/tesfasefineh34/Desktop/sefiandsami.jpg",brothers)
cv.imshow("sefineh and samuel",brothers)
cv.waitKey(0)






