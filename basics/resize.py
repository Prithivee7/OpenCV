import cv2

# Can rescale images,videos and live videos
def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)
    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)


capture = cv2.VideoCapture('videos/aala poraan tamilan.mkv')
while True:
    isTrue, frame = capture.read()
    cv2.imshow('Video',frame)
    frame_resized = rescaleFrame(frame,0.75)
    cv2.imshow('Resized',frame_resized)


    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()