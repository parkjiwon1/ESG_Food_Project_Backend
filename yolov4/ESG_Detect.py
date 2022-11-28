import os
from yolov4.yolov3.utils import detect_image, Create_Yolo, make_ingredients_list
from yolov4.yolov3.configs import *
from yolov4.yolov3.yolov4 import read_class_names


def model_init():
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    yolo = Create_Yolo(input_size=YOLO_INPUT_SIZE, CLASSES=TRAIN_CLASSES)  # 모델 불러오기
    yolo.load_weights("yolov4/checkpoints/yolov4_custom")  # 모델 weight 불러오기
    num_classes = read_class_names(TRAIN_CLASSES)  # CLASSES NUM
    return yolo, num_classes


def img_detect(yolo, num_classes, img_input_path, img_output_path):
    image, pred_classes = detect_image(yolo, img_input_path, img_output_path,
                                       input_size=YOLO_INPUT_SIZE, show=False, CLASSES=TRAIN_CLASSES,
                                       rectangle_colors=(255, 0, 0), score_threshold=0.3)
    ingredients_list = make_ingredients_list(num_classes, pred_classes)  # 재료 리스트 벡터화
    return image, ingredients_list
