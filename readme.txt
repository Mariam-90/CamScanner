# Project Title: Image Straightening Tool

 Authors:

  - Email: maryam19455@gmail.com

 Description:
This program is designed to straighten photos of rectangular pages, facilitating document digitization with enhanced readability. It is developed as part of a coursework project for the "Image Processing and Computer Vision" course. The program systematically executes a series of steps starting from applying a binary threshold to the image, identifying the page's contour as the largest contour in the image, and proceeding through to calculating and applying a perspective transformation to straighten the image based on the page's corners. The outcome is a saved, straightened image ready for further processing or archival.

 Steps:
1. **Binary Threshold Application:** The image is first converted to grayscale, then a binary threshold is applied to enhance the contrast between the page and its background.
2. **Largest Contour Identification:** The program identifies the largest contour, presumed to be the target page.
3. **Minimum Area Rectangle:** It finds the bounding rectangle of this contour that has the minimum area, effectively capturing the page's outline.
4. **Dimension Calculation:** The program calculates the page's height and width based on the identified contour.
5. **Transformation Matrix Definition:** A transformation matrix is defined to map the corners of the page to the corners of the output image.
6. **Perspective Transformation:** This matrix is then used to apply a perspective transformation, straightening the image.
7. **Image Saving:** Finally, the straightened image is saved to a specified output path.

## Environment:
- **Operating System:** macOS
- **Requirements:**
  - **Python** 3.11.0
  - **OpenCV** package
  - **Matplotlib** package

## Installation and Running Instructions:
1. Ensure Python 3.11.0 is installed on your system.
2. (Optional) Create a virtual environment for project dependencies:
   - **Creation:** `python -m venv opencv-env`
   - **Activation:** `source opencv-env/bin/activate`
   - **Deactivation:** `deactivate`
3. Install the required packages using pip: `pip install opencv-contrib-python matplotlib`
4. To run the program, navigate to the directory containing `Scanner.py` and execute it with the following command, ensuring any virtual environment is active if utilized:
   - `python3 Scanner.py <path_to_input_image> <path_to_output_image>`

### Example Commands:
- `python3 Scanner.py img2how2.jpg output_image.jpg`
- `python3 Scanner.py img3how2.jpg output_image.jpg`
- `python3 Scanner.py how2imge.jpg output_image.jpg`

## Assumptions:
- The primary subject of the image is a page.
- The photographed page has a rectangular shape.
- The page's height is greater than its width.
- The page is brighter than its surrounding background.

## Notes:
- The script file `Scanner.py` contains all the necessary source code to execute the image straightening process.
- The `<path_to_input_image>` parameter should be replaced with the actual file path of the image you wish to straighten.
- The `<path_to_output_image>` parameter should be replaced with the desired file path for the straightened image output.
