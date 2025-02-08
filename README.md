# CS231 Numeric Gesture Recognition

## 👥 Group Members  

- Nguyễn Trần Khương An
- Hồng Phúc Hải
- Tăng Mỹ Hân

---

## Introduction

This project focuses on recognizing digits in hand signs to assist hearing-impaired individuals in daily communication. It serves as a foundation for more complex research and applications, such as translating sign language into sentences or paragraphs.

## Problem Statement

- **Input**: Images containing hand signs representing digits (0-9).  
- **Output**: Predicted label corresponding to the hand sign digit.  
- **Constraints**: Each input image contains only one hand captured at an optimal distance to maintain image quality.  

## Feature Extraction

The project utilizes the following feature extraction methods:

- **Histogram of Oriented Gradients (HOG)**: Extracts local features based on pixel gradient orientations.  
- **Scale-Invariant Feature Transform (SIFT)**: Detects and describes scale-invariant features.  
- **Bag of Visual Words (BoVW)**: Constructs feature representations based on visual word dictionaries.  

## Classification Models

We experimented with three machine learning models for classification:

- **Support Vector Machines (SVM)**: Finds an optimal boundary between classes.  
- **k-Nearest Neighbors (KNN)**: Classifies based on the k-nearest neighbors.  
- **Random Forest**: An ensemble learning model based on multiple decision trees.  

## Experiments

### Dataset

- **Dataset Used**: Sign Language Digits Dataset  
- **Image Size**: 100 x 100 pixels  
- **Color Space**: RGB  
- **Number of Classes**: 10 (Digits 0-9)  
- **Collected From**: 218 students, each contributing 10 samples.  

### Model Evaluation

5-fold Cross-Validation was used to assess model accuracy.

#### Test Set Performance:

- **HOG + SVM**: Best with `C=100`, `gamma=0.01`, `kernel='rbf'`.  
- **HOG + KNN**: Best with `k=23`.  
- **HOG + Random Forest**: Best with `n=140`.  
- **BoVW + SVM**: Best with `C=1`, `gamma=0.01`, `kernel='rbf'`.  
- **BoVW + KNN**: Best with `k=27`.  
- **BoVW + Random Forest**: Best with `n=120`.  

## Demo

[![Video Title](https://img.youtube.com/vi/p8tA5KuV5Lc/hqdefault.jpg)](https://www.youtube.com/watch?v=p8tA5KuV5Lc)

## References

[1] Paper: **Visual Categorization with Bags of Keypoints** Gabriella Csurka, Christopher R. Dance, Lixin Fan, Jutta Willamowski, Cédric Bray Xerox Research Centre Europe 6, chemin de Maupertuis 38240 Meylan, France

[2] Paper: **Hand Gesture Recognition via Bag of Visual Words** Guoming Chen ,Qiang Chen ,Yiqun Chen,Xiongyong Zhu Department of Computer Science, Guangdong University of Education Guangdong 510303,China

[3] Paper: **Hand Gesture Recognition Using Bag-of-Features and Multi-Class Support Vector Machine** Nasser Dardas, Qing Chen, Nicolas D. Georganas, Fellow, IEEE, and Emil M. Petriu, Fellow, IEEE

[4] Paper: **Hand Gesture Recognition using Support Vector Machine and Bag of Visual Words model** Vipul Mehra May 13, 2018

[5] Paper: **Object Recognition from Local Scale-Invariant Features** David G. Lowe Computer Science Department University of British Columbia Vancouver, B.C., V6T 1Z4, Canada

[6] **https://www.pinecone.io/learn/series/image-search/bag-of-visual-words/**

[7] github: **https://github.com/talhaimran96/Image-features-Detection-and-Matching-Image-Classification-UsingBag-of-Visual-Words/tree/main**

[8] Paper: Cortes, Corinna; Vapnik, Vladimir (1995). **"Support-vector networks"** (PDF)

[9] Navneet Dalal and Bill Triggs. **Histograms of oriented gradients for human detection.** IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR), 1:886–893, 2005 

## Contact

For any questions regarding the project, please reach out via email or create an issue on this GitHub repository.
