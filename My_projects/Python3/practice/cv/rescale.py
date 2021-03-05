import cv2 as cv

img = cv.imread("photos/kep001.jpg");
cv.imshow("Cat", img);

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale);
    height = int(frame.shape[0] * scale);

    dimensions = (width, height);

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA);


resized_image = rescaleFrame(img);
cv.imshow("Kep", resized_image);
# Reading videos
capture = cv.VideoCapture("videos/Youtube.mp4");

while True:
    isTrue, frame = capture.read();

    frame_resized = rescaleFrame(frame, scale=.2);

    cv.imshow("Video", frame);
    cv.imshow("Video_resized", frame_resized);

    if cv.waitKey(20) & 0xFF==ord('d'):
        break;

capture.release();
cv.destroyAllWindows();