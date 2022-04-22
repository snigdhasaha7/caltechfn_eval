## Instructions for Running

This repo has been cloned and modified from https://github.com/ultralytics/yolov5.

To run the model, please use the following command:
```shell
python train.py --data svhn.yaml --weights '' --cfg yolov5s.yaml
```

In order to calculate mAP_50 scores, change the value of `iou_thres` on Line 103 of `val.py` to 0.5.

In order to calculate mAP_75 scores, change the value of `iou_thres` on Line 103 of `val.py` to 0.75.

Note that we have only provided the set up to train on SVHN and test on SVHN. To run the rest of the models (SVHN on CaltechFN, CaltechFN on SVHN, CaltechFN on CaltechFN), you will have to adjust the directories and create .yaml files like the one provided in the data folder.
