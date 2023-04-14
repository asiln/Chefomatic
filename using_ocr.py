import easyocr
import cv2

reader = easyocr.Reader(["en"], gpu=True)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = reader.readtext(frame)
    for i in range(len(results)):
        cords = results[i][0]
        label = results[i][1]
        confidence = results[i][2]
        x1, y1 = map(int, cords[3])
        x2, y2 = map(int, cords[1])
        if confidence > 0.7:
            bgr = (0, 0, 255)
            print(label)
            cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
            cv2.putText(frame, label, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, bgr, 2)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
