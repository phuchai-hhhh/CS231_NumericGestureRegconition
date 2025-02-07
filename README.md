# CS231_NumericGestureRegconition

# Introduction

This project focuses on recognizing digits in hand signs to assist hearing-impaired individuals in daily communication. It can serve as a foundation for more complex research and applications, such as translating sign language into sentences or paragraphs.

Problem Statement

Input: Images containing hand signs representing digits (0-9).

Output: Predicted label corresponding to the hand sign digit.

Constraints: Each input image contains only one hand captured at an optimal distance to maintain image quality.

Feature Extraction

The project utilizes the following feature extraction methods:

Histogram of Oriented Gradients (HOG): Extracts local features based on pixel gradient orientations.

Scale-Invariant Feature Transform (SIFT): Detects and describes scale-invariant features.

Bag of Visual Words (BoVW): Constructs feature representations based on visual word dictionaries.

Classification Models

We experimented with three machine learning models for classification:

Support Vector Machines (SVM): Finds an optimal boundary between classes.

k-Nearest Neighbors (KNN): Classifies based on the k-nearest neighbors.

Random Forest: An ensemble learning model based on multiple decision trees.

Experiments

Dataset

Dataset Used: Sign Language Digits Dataset

Image Size: 100 x 100 pixels

Color Space: RGB

Number of Classes: 10 (Digits 0-9)

Collected from 218 students, each contributing 10 samples.

Model Evaluation

5-fold Cross-Validation was used to assess model accuracy.

Test set performance:

HOG + SVM: Best with C=100, gamma=0.01, kernel='rbf'.

HOG + KNN: Best with k=23.

HOG + Random Forest: Best with n=140.

BoVW + SVM: Best with C=1, gamma=0.01, kernel='rbf'.

BoVW + KNN: Best with k=27.

BoVW + Random Forest: Best with n=120.

Demo

The project includes a demo showcasing model predictions on the test dataset. Correct and incorrect predictions are displayed for analysis.

References

"Visual Categorization with Bags of Keypoints" - Gabriella Csurka, Christopher R. Dance, Lixin Fan, Jutta Willamowski

"Hand Gesture Recognition using Support Vector Machine and Bag of Visual Words model" - Vipul Mehra

"Support-vector networks" - Corinna Cortes, Vladimir Vapnik (1995)

"Histograms of Oriented Gradients for Human Detection" - Navneet Dalal, Bill Triggs (2005)

Contact

For any questions regarding the project, please reach out via email or create an issue on this GitHub repository.

