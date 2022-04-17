## Instructions to obtain SVHN Test Data

1. Download the test.tar.gz from Format 1 on http://ufldl.stanford.edu/housenumbers/.
2. Run the following commands in terminal to extract the testing data:
    ```bash
    foo@bar:~$ tar -xvf test.tar.gz
    ```
3. Copy the testing images into the test folder. Delete all non image files (do NOT delete the provided json file).

To create the Coco-formatted json file from the .mat files, we used https://github.com/roboflow-ai/voc2coco. 