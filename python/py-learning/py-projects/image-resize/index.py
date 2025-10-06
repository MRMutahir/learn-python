import cv2

# Step 1: Read image
img = cv2.imread("img.jpg")

# Step 2: Check if image loaded successfully
if img is None:
    print("Error: Image not found!")
else:
    # Step 3: Resize image (width, height)
    new_width = 10
    new_height = 40
    reImageSize = cv2.resize(img, (new_width, new_height))

    # Step 4: Save new image with extension
    cv2.imwrite("./new_img.jpg", reImageSize)

    # Step 5: Cleanup
    cv2.destroyAllWindows()
