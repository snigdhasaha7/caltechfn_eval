## Instructions for Running

We simply used the code from https://github.com/ultralytics/yolov5.

To train the model, please use the following command (adjust per dataset):
```shell
python train.py --data svhn.yaml --weights '' --cfg yolov5s.yaml
```
Then, use val.py to validate the trained model.

In order to calculate mAP_50 scores, change the value of `iou_thres` on Line 103 of `val.py` to 0.5.

In order to calculate mAP_75 scores, change the value of `iou_thres` on Line 103 of `val.py` to 0.75.
