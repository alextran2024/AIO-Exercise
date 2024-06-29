# Bai 2
from PIL import Image
import numpy as np
import streamlit as st
import cv2  # thong bao cho may su dung ham cv2 de xu ly hinh anh
MODEL = "model/MobileNetSSD_deploy.caffemodel"
PROTOTXT = "model/MobileNetSSD_deploy.prototxt.txt"


def process_image(image):
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )  # Chuyển đổi hình ảnh đầu vào thành một blob (định dạng chuẩn hóa) và thay đổi kích thước thành (300, 300).
    # Nhân hình ảnh với hệ số 0.007843 và trừ đi giá trị trung bình 127.5 để chuẩn hóa dữ liệu.
    # Đọc mô hình từ tệp Prototxt và Caffe model.
    net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
    net.setInput(blob)  # Đặt blob làm đầu vào
    detections = net.forward()
    return detections


def annotate_image(image, detections, confidence_threshold=0.5):
    (h, w) = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > confidence_threshold:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(image, (startX, startY), (endX, endY), 70, 2)
    return image


def main():
    st.title('Object Detection for Images')
    file = st.file_uploader('Upload Image', type=['jpg', 'png', 'jpeg'])
    if file is not None:
        st.image(file, caption="Uploaded Image")

        image = Image.open(file)
        image = np.array(image)
        detections = process_image(image)
        processed_image = annotate_image(image, detections)
        st.image(processed_image, caption="Processed Image")


if __name__ == "__main__":
    main()
