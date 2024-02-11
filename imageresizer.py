import cv2

def resize_image(input_image_path, output_image_path, new_width=None, new_height=None):
    """Resize an image."""
    image = cv2.imread(input_image_path)
    if new_width is None and new_height is None:
        return image

    if new_width is None:
        new_width = int(image.shape[1] * (new_height / image.shape[0]))
    elif new_height is None:
        new_height = int(image.shape[0] * (new_width / image.shape[1]))

    resized_image = cv2.resize(image, (new_width, new_height))
    cv2.imwrite(output_image_path, resized_image)
    return resized_image

if __name__ == "__main__":
    input_path = "input_image.jpg"
    output_path = "output_image.jpg"
    new_width = 400  # specify new width in pixels
    new_height = None  # specify new height in pixels, or leave as None

    resized_image = resize_image("D:\\Coding\\Python\\ImageResizer\\Valo.png","D:\\Coding\\Python\\ImageResizer\\Valo2.png",1280,920)
    print("Image resized successfully.")
