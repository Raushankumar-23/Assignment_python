# Writing a video

import cv2

video = cv2.VideoCapture("C:\\Users\\Raushan Kumar\\Videos\\Accident excel recording.mp4")

# get original video resolution
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('Output.mp4', fourcc, 25.0, (width, height))

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    output.write(frame)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(18) & 0xFF == ord('s'):
        break

video.release()
output.release()
cv2.destroyAllWindows()