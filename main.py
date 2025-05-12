import cv2
import numpy as np

# Load reference image (real note)
reference = cv2.imread('reference/500_real.png', 0)  # grayscale

# Load test image (note to verify)
test = cv2.imread('test_images/fake__500.png', 0)

# Feature detector
orb = cv2.ORB_create()

# Detect keypoints and descriptors
kp1, des1 = orb.detectAndCompute(reference, None)
kp2, des2 = orb.detectAndCompute(test, None)

# Match features
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# Draw top matches
matched_img = cv2.drawMatches(reference, kp1, test, kp2, matches[:20], None, flags=2)

# Show result
cv2.imshow("Feature Matching", matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Basic result logic
if len(matches) > 50:
    print("✅ Possibly a real note")
else:
    print("❌ Possibly a fake note")
