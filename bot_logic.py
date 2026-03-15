import random
from imageai.Detection import ObjectDetection

import os
_detector = None
MODEL_PATH = r"C:\Users\gkond\Desktop\ai bot\yolov3.pt"
CROWD_THRESHOLD = 30
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"


def get_class(image_path):
    global _detector
    # Ленивая инициализация детектора при первом вызове
    if _detector is None:
        _detector = ObjectDetection()
        _detector.setModelTypeAsYOLOv3()
        _detector.setModelPath(MODEL_PATH)
        _detector.loadModel()

    # Детекция объектов на изображении
    detections = _detector.detectObjectsFromImage(
        input_image=image_path,
        output_image_path=None,          # не сохраняем размеченное фото
        minimum_percentage_probability=30
    )

    # Оставляем только людей
    people = [d for d in detections if d["name"] == "person"]
    count = len(people)

    if count > CROWD_THRESHOLD:
        return f"⚠️ ВНИМАНИЕ: скопление людей! На фото {count} человек (порог {CROWD_THRESHOLD})"
    else:
        return f"Людей на фото: {count} (порог {CROWD_THRESHOLD} не превышен)"
