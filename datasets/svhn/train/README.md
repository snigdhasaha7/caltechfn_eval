## Instructions to obtain SVHN Train Data

1. Download the train.tar.gz from Format 1 on http://ufldl.stanford.edu/housenumbers/.
2. Run the following commands in terminal to extract the training data:
    ```bash
    foo@bar:~$ tar -xvf train.tar.gz
    ```
3. Copy the training images into the train folder. Delete all non image files (do NOT delete the provided JSON file).

To create the Coco-formatted json file from the .mat files, we used https://github.com/roboflow-ai/voc2coco. 