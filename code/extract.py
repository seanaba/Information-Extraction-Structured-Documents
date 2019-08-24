# -*- coding: utf-8 -*-
import align
import os
import json
import pytesseract
import cv2
from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


class ExtractDoc(object):
    def __init__(self, data_path, config_path):
        self.data_path = data_path
        self.config_path = config_path

    def get_data(self):
        """
        get template and test images
        """
        template_img_path = os.path.join(self.data_path, 'template')
        test_img_path = os.path.join(self.data_path, 'test')
        template_img = [os.path.join(template_img_path, img) for img in os.listdir(template_img_path)
                        if os.path.isfile(os.path.join(template_img_path, img))]
        test_img = [os.path.join(test_img_path, img) for img in os.listdir(test_img_path)
                    if os.path.isfile(os.path.join(test_img_path, img))]
        return template_img[0], test_img

    def read_info(self, img_aligned):
        config_temp = json.load(open(os.path.join(self.config_path, "config.json")))
        for item in config_temp:
            print("Information extracted for ", item["name"])
            coor_1, coor_2, coor_3, coor_4 = item["bounding_box"]
            img = img_aligned[coor_1:coor_2, coor_3:coor_4]
            plt.imshow(img,)
            plt.show()
            try:
                print(pytesseract.image_to_string(img, config="--oem 1"))
            except:
                print("Text extraction error")

    def extract_info(self):
        """
        Basic information extraction (structured documents)
        1- Collect template/test documents
        2- Align test documents with the template
        3- Extract information
        """
        # loads template and test images
        temp_img, test_img = self.get_data()
        # aligns test images with the template image
        # extracts information
        for img in test_img:
            align.align_brute_force(temp_img, img)
            self.read_info(cv2.imread(img, 0))
