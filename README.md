## Introduction
This repository contains minimalistic usage examples of ONNX models for computer vision tasks such as face/object detection. Download and inference codes can be found in their respective folders. You can find a set of faces used for validating clusters in [faces](faces), these are randomly taken from [LFW (Labeled Faces in the Wild)](http://vis-www.cs.umass.edu/lfw/).

### Available Models
Below is an index of existing models in this repository:

|Model Class |Reference |Description |Model/Code Source|
|-|-|-|-|
|<b>[ArcFace](models/arcface)</b>|[Deng et al.](https://arxiv.org/abs/1801.07698)|A CNN based model for face recognition which learns discriminative features of faces and produces embeddings for input face images.| [InsightFace](https://insightface.ai/arcface)|
|<b>[FaceNet](models/facenet)</b>|[Schroff et al.](https://arxiv.org/abs/1503.03832)|A CNN based model for face recognition that maps face images to a compact Euclidean space where distances directly correspond to a measure of face similarity.| [FaceNet Pytorch](https://github.com/timesler/facenet-pytorch)|
|<b>[YOLOv8](models/yolov8)</b>|[Jocher et al.](https://github.com/ultralytics/ultralytics)|A CNN model for real-time object detection that can identify multiple object categories simultaneously. It uses a single network evaluation, making it extremely fast and efficient. This implementation, based on Ultralytics' YOLOv8, offers state-of-the-art performance in speed and accuracy. The model is typically trained on datasets like COCO, capable of detecting 80 common object classes in various scenarios.|[YOLOv8](https://github.com/ultralytics/ultralytics), [YOLOv8-face](https://github.com/akanametov/yolo-face), [ONNX code](https://github.com/ibaiGorordo/ONNX-YOLOv8-Object-Detection)|

For more comprehensive list models, visit the original repositry of [ONNX Models](https://github.com/onnx/models) 

## License
[Apache License v2.0](LICENSE)