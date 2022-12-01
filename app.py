from flask import Flask
from flask import request
from cal import *
from yolov4.ESG_Detect import img_detect, model_init

app = Flask(__name__)
yolo, num_classes = model_init()
app.config['JSON_AS_ASCII'] = False


@app.post('/')
def hello():
    file = request.files['file']
    save_to = f'contents/input/{file.filename}'
    output_to = f'contents/output/{file.filename}'
    file.save(save_to)
    image, ingredients_list = img_detect(yolo, num_classes, save_to, output_to)
    if sum(ingredients_list) == 0:
        return {'idx': [0], 'ingredients': [""]}
    idx_ingredients = cal_similarity(ingredients_list)[:5]
    keys = ['idx', 'ingredients']
    output = dict(zip(keys, idx_ingredients))
    return output


if __name__ == '__main__':
    app.run(host='0.0.0.0')
