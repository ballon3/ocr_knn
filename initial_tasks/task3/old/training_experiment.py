
import sys, os
import numpy as np
import cv2



x,y,w,h = 0, 0, 38, 30

samples = np.empty((0, 100), np.float32)
responses = []
keys = [i for i in range(48, 58)]


for image in os.listdir(os.getcwd()+'/train_digits/'):
    print image
    im = cv2.imread('train_digits/'+image)
    im3 = im.copy()

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

    #################      Now finding Contours         ###################

    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 2)
    roi = thresh[y:y + h, x:x + w]
    roismall = cv2.resize(roi, (10, 10))
    cv2.imshow('norm', im)
    key = cv2.waitKey(0)
    key = 48+(key-1114032)

    if key == chr(27).encode():  # (escape to quit)
        sys.exit()
    elif key in keys:
        responses.append(int(chr(key)))
        sample = roismall.reshape((1, 100))
        samples = np.append(samples, sample, 0)



responses = np.array(responses, np.float32)
responses = responses.reshape((responses.size, 1))
print "training complete"

samples = np.float32(samples)
responses = np.float32(responses)

cv2.imwrite("train_result.png", im)
np.savetxt('generalsamples.data', samples)
np.savetxt('generalresponses.data', responses)
