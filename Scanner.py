import cv2
import numpy as np
import sys
from matplotlib import pyplot as plt

# Function to display the image
def show_image(img, title="Image"):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

def scan_document(input_path, output_path):
    # Read the image in grayscale
    image = cv2.imread(input_path)

    show_image(image, "Original Image")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur and perform Otsu's thresholding
    blurred = cv2.GaussianBlur(gray, (233, 233), 0)
    _, binary_image = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    show_image(binary_image, "Binary Image")

    # Find contours in the image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)

    # Approximate the contour to a four-point polygon
    epsilon = 0.02 * cv2.arcLength(largest_contour, True)
    approx = cv2.approxPolyDP(largest_contour, epsilon, True)

    # If we found four points, proceed
    if len(approx) == 4:
        # Calculate the width and height of the document
        points = approx.reshape(4, 2)
        rect = np.zeros((4, 2), dtype="float32")

        # Order the points as TL, TR, BR, BL
        s = points.sum(axis=1)
        rect[0] = points[np.argmin(s)]
        rect[2] = points[np.argmax(s)]

        diff = np.diff(points, axis=1)
        rect[1] = points[np.argmin(diff)]
        rect[3] = points[np.argmax(diff)]

        # Define the destination points based on the width and height of the document
        (tl, tr, br, bl) = rect
        widthA = np.linalg.norm(br - bl)
        widthB = np.linalg.norm(tr - tl)
        maxWidth = max(int(widthA), int(widthB))
        heightA = np.linalg.norm(tr - br)
        heightB = np.linalg.norm(tl - bl)
        maxHeight = max(int(heightA), int(heightB))

        dst = np.array([
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]
        ], dtype="float32")

        # Calculate the perspective transform matrix and apply it
        M = cv2.getPerspectiveTransform(rect, dst)
        warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

        # Save the image
        cv2.imwrite(output_path, warped)

        show_image(warped, "Straightened Image")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_image output_image")
        sys.exit(1)

    input_path, output_path = sys.argv[1], sys.argv[2]
    scan_document(input_path, output_path)

# python3 Scanner.py img2how2.jpg output_image.jpg
# python3 Scanner.py img3how2.jpg output_image.jpg
# python3 Scanner.py how2imge.jpg output_image.jpg