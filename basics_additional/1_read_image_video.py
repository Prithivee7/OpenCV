import cv2

# Inside the waitKey if 0 is passed as an argument the image remains indefinitely
# Other than that it works as milliseconds.


def read_image(image):
    img = cv2.imread(image)
    cv2.imshow("Output", img)
    cv2.waitKey(2000)


# When pressed 'q' the video terminates
def read_video(video):
    cap = cv2.VideoCapture(video)
    while True:
        success, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


""" For recording the webcam argument of '0' need to be passed to VideoCapture
    id for width - 3
    id for height - 4
    id for brightness - 10
    along with this arguments we also the number of pixels 
"""


def read_web_cam():

    cap = cv2.VideoCapture(0)
    cap.set(3, 480)
    cap.set(4, 720)
    cap.set(10, 100)
    while True:
        success, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


read_image("./Images/audi.jpg")
read_video("akon.mp4")
read_web_cam()
