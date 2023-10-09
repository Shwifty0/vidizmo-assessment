# Vidizmo Assessment

## Author: Muhammad Ozair

### Task 1: Permutation.py

In Task 1, I have implemented two solutions for generating permutations of unique integers:
1. Using the `itertools.permutation` class.
2. Implementing a recursion-based algorithm for performing permutations.

The goal is to create a function that takes an array of unique integers as input and returns an array containing all permutations of those integers in no particular order. If the input array is empty, the function will return an empty array.

**Sample Input:**
```python
array = [1, 2, 3]
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Task 2: Deep Learning CNN (RESNET-50)

In Task 2, I performed image classification using the RESNET-50 architecture on the STL-10 dataset. However, due to resource limitations on Colab, I couldn't train the model for longer epochs.

## Task 3: Deep Learning - YOLO

Task 3 involves fine-tuning a Yolov8 model using the Yolo nano model as a base. The goal was to train the model on the MS COCO car damage detection dataset for 2 epochs and then apply the trained model to infer on a provided video.

Task 3 files are stored in the "Yolo" folder.

**Note:** There might be issues with reproducibility for these tasks due to limited resources and storage constraints. Some files were not uploaded:

- Task 2: RESNET-50's weights were not uploaded.
- Task 3: The MS COCO dataset and the fine-tuned "yolov8n.pt" model weren't uploaded.

Please make sure to address these limitations if you plan to reproduce the tasks or need access to missing files.
