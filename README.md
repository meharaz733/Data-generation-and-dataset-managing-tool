# Image-generation-and-dataset-managing-tool
This repository contains two Python scripts designed to assist with data generation with image augmentation, and dataset restructuring for machine learning tasks.



## Scripts Overview

### 1. **Image Generation with Augmentation Script**
The **class_balancing_script.py** enhances the existing image by generating augmented images. The script:
- Takes images from a source folder and applies transformations like rotations and elastic distortions.
- Augments images that have fewer than a specified number (e.g., 2500) per class.

#### Features:
- Performs augmentations (rotations, elastic distortions).
- Configurable target image count per class.
- Augments images and saves them in the same directory.
  

### 2. **Dataset Restructuring Script**
The **make_structured.py** organizes images into **train**, **test**, and **validation** sets based on user-defined ratios. The script:
- Accepts a source directory with class subfolders.
- Distributes images into the **train**, **test**, and **val** folders according to the given ratios (e.g., 80% train, 10% test, 10% validation).

#### Features:
- Automatically creates **train**, **test**, and **validation** folders.
- Configures ratios for training, testing, and validation splits.
- Randomly shuffles images to ensure even distribution.


  
## Setup and Installation

Make sure you have Python installed. Then, install the required dependencies using the following command:

```bash
pip install -r requirement.txt
```


## Usage   
### Image Generation with Augmentation Script:

  - Provide the source folder containing the images.
  - Set the target number of images for each class.
  - The script augments the images that have fewer than the target count.

### Dataset Restructuring Script:   

  - Set the source directory where the dataset is currently stored.
  - Set the destination directory where you want the structured dataset to be saved.
  - The script will automatically create train, test, and validation folders.
  - It then splits the images from each class into these folders based on your configured ratios.



## Example   
  1. **Image Generation with Augmentation Script**
```bash
  python class_balancing_script.py
```
  2. **Dataset Restructuring Script**
```bash
  python make_structured.py
```


## Future Development   
I plan to improve the scripts by adding a user-friendly interface for easy configuration, allowing users to:
  - Set parameters (source folder, destination folder, image augmentations) via an interactive command-line or GUI interface.
  - Backup datasets before augmentation or restructuring.
  - Provide advanced augmentation options (e.g., color variations, cropping).
  - Dynamically configure the dataset splitting ratios.
  - Add error handling and logging for smoother execution.

## Contributing   
  - Feel free to submit a pull request or open an issue if you want to contribute to the project!
