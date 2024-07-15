import os
import cv2
from yolov8 import YOLOv8
from yolov8.utils import class_names

model_path = os.getenv('MODEL_PATH')
yolov8_detector = YOLOv8(model_path, conf_thres=0.2, iou_thres=0.3)

img_path = os.getenv('IMAGE_PATH')
img = cv2.imread(img_path)

if img is None:
    print(f"Failed to load image: {img_path}")
    exit()

boxes, scores, class_ids = yolov8_detector(img)
print(scores, "\n", class_ids)
for x in class_ids: print(class_names[x], end=" ")
print()

combined_img = yolov8_detector.draw_detections(img)
cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
cv2.imshow("Detected Objects", combined_img)
cv2.imwrite("outputs/detected_objects.jpg", combined_img)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.getWindowProperty("Detected Objects", cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()
