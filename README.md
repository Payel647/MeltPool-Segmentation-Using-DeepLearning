# Melt Pool Segmentation Using Deep Learning

## Overview

This project focuses on automatic melt pool segmentation in Directed Energy Deposition (DED) manufacturing processes using deep learning-based semantic segmentation techniques. Accurate melt pool detection is important for monitoring and improving additive manufacturing quality.

The project includes dataset preparation, manual annotation, preprocessing, model training, and performance evaluation using state-of-the-art segmentation architectures.

## Features

* Video frame extraction using OpenCV
* Region of Interest (ROI) extraction
* Manual annotation using LabelMe
* Automatic mask generation for supervised learning
* Deep learning-based segmentation
* Performance evaluation using multiple metrics
* Comparison of U-Net and DeepLabV3 models

## Dataset Preparation

1. Extract frames from DED melt pool videos.
2. Crop the Region of Interest (ROI).
3. Annotate melt pool regions using LabelMe.
4. Generate binary segmentation masks.
5. Train segmentation models using image-mask pairs.

### Dataset Information

* Dataset Type: Custom DED Melt Pool Dataset
* Approximate Size: 100 manually annotated images
* Annotation Tool: LabelMe

## Models Used

### U-Net

A convolutional neural network designed specifically for biomedical and image segmentation tasks.

### DeepLabV3

A semantic segmentation architecture that uses atrous convolutions for capturing multi-scale contextual information.

## Results

### U-Net Performance

| Metric     | Value  |
| ---------- | ------ |
| IoU        | 0.832  |
| Dice Score | 0.908  |
| Precision  | 1.000  |
| Recall     | 0.832  |
| Accuracy   | 99.63% |

### DeepLabV3 Performance

| Metric     | Value  |
| ---------- | ------ |
| IoU        | 0.824  |
| Dice Score | 0.903  |
| Precision  | 0.988  |
| Recall     | 0.832  |
| Accuracy   | 99.61% |

### Best Model

U-Net achieved the best overall performance with:

* Dice Score: 0.908
* IoU: 0.832
* Accuracy: 99.63%

## Tech Stack

* Python
* PyTorch
* OpenCV
* NumPy
* Matplotlib
* LabelMe

## Future Improvements

* Increase dataset size
* Experiment with advanced segmentation architectures
* Real-time melt pool monitoring
* Hyperparameter optimization
* Deployment as an industrial quality monitoring system
