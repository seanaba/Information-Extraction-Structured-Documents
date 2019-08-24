import cv2
import numpy as np


def align_brute_force(temp_path, test_path, good_match_pct=0.9, max_feat=100):
    """
    aligns images with the template
    using brute force method
    """
    # reads template image
    img_temp = cv2.imread(temp_path, cv2.IMREAD_COLOR)
    # reads test image
    img_test = cv2.imread(test_path,  cv2.IMREAD_COLOR)
    # converts test image to grayscale
    img_1 = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY)
    # converts template image to grayscale
    img_2 = cv2.cvtColor(img_temp, cv2.COLOR_BGR2GRAY)
    # feature detection (ORB)
    orb = cv2.ORB_create(max_feat)
    # compute the key points and descriptors
    kp_1, des_1 = orb.detectAndCompute(img_1, None)
    kp_2, des_2 = orb.detectAndCompute(img_2, None)
    # detects matchers using Brute-Force method
    match = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    match_feat = match.match(des_1, des_2, None)
    # sorts descriptor matches
    match_feat.sort(key=lambda x: x.distance, reverse=False)
    # selects good matches
    good_feat = match_feat[:int(len(match_feat)*good_match_pct)]
    # extracts locations
    points_1 = np.zeros((len(good_feat), 2), dtype=np.float32)
    points_2 = np.zeros((len(good_feat), 2), dtype=np.float32)
    for i, m in enumerate(good_feat):
        points_1[i, :] = kp_1[m.queryIdx].pt
        points_2[i, :] = kp_2[m.queryIdx].pt
    # compute homography
    h, mask = cv2.findHomography(points_1, points_2, cv2.RANSAC)
    height, width, channels = img_temp.shape
    # aligns the test image
    img_aligned = cv2.warpPerspective(img_test, h, (width, height))
    # saves the test image
    cv2.imwrite(test_path, img_aligned)