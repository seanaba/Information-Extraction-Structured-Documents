# Information Extraction (Template-Based)
![](https://github.com/seanaba/Information-Extraction-Structured-Documents/blob/master/doc/pic/pic1.png)
## **Table of Contents**
- [Introduction](#intro)
- [Feature Extraction](#fe)
- [Information Extraction](#ie)
<a name="intro"></a>
## Introduction
Information extraction methodologies are used to extract desired information from any type of documents. The extraction accuracy and methodology solely depend on the format of document that is targeted to be processed and type of information required to be extracted from documents. Template-based information extraction is one of the most common techniques in the field of information extraction. It generates highly accurate information from documents under one condition. The template must be consistent with documents which are targeted to be processed by the information extraction template-based technique.
The information extraction process is simple. It requires basic image processing methods. First of all, the template document which can be simply one of the documents is selected; then, the coordinates of required information are derived from the template and saved in a configuration file.  Finally, target documents are aligned with the template and the desired information are extracted. The advantage of using the template-based information extraction is accuracy of extracted information; however, templates must be consistent with documents. The methodology is useful for structured documents such as forms. 
<a name="fe"></a>
## Feature Extraction
As mentioned above, after template is being selected and the coordinates of desired information from the template derived, documents need to be aligned with the template. Basic pre-processing on the documents is required before the aligning process such as correcting the angle of documents to make sure for instance documents are not up-side-down. Then, here is how the aligning process executes. Two main algorithms are used for the document alignments: Brute-force-based and Flann-based alignment. I will not go into details but both algorithms aim to find the closest distance of features from documents in the template. Once the features are extracted, the documents are changed based on the features to become as similar as possible with the template. 
<a name="ie"></a>
## Information Extraction
The final step is what we are looking for which is information extraction after documents are aligned with the template. As mentioned above briefly, coordinates of desired information are collected in a configuration file. The coordinates are in the format of bounding box in x-y directions. Thus, the configuration file provides 4 numbers corresponding to the coordinates of each individual piece of information required to be extracted from documents. Note that the coordinates are derived from the template not the documents, part of image is cropped based on the coordinates, and corresponding text is extracted after the aligning process.
