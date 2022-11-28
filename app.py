from flask import Flask
from flask import request
from cal import *
from yolov4.ESG_Detect import img_detect, model_init

app = Flask(__name__)
yolo, num_classes = model_init()
app.config['JSON_AS_ASCII'] = False


# @app.route('/')
# def hello_world():  # put application's code here
#     image, ingredients_list = img_detect(yolo, num_classes, "yolov4/IMAGES/aa.jpg", "contents/output.jpg")
#     if len(ingredients_list) == 0:
#         return '0'
#     return cal_similarity(ingredients_list)


# @app.post('/')
# def hello():
#     file = request.files['file']
#     save_to = f'contents/input/{file.filename}'
#     output_to = f'contents/output/{file.filename}'
#     file.save(save_to)
#     image, ingredients_list = img_detect(yolo, num_classes, save_to, output_to)
#     if sum(ingredients_list) == 0:
#         return '0'
#     sim_lists = cal_similarity(ingredients_list)[:5]
#     sim_keys = ['name', 'url', 'score']
#     sim_dict = list(map(lambda x: dict(zip(sim_keys, x)), sim_lists))
#     return sim_dict

@app.post('/')
def hello():
    file = request.files['file']
    save_to = f'contents/input/{file.filename}'
    output_to = f'contents/output/{file.filename}'
    file.save(save_to)
    image, ingredients_list = img_detect(yolo, num_classes, save_to, output_to)
    if sum(ingredients_list) == 0:
        return '0'
    indices = cal_similarity(ingredients_list)[:5]
    return ' '.join(map(str, indices))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
