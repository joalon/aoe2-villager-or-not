from fastai.vision import load_learner, open_image
from PIL import Image

learn = load_learner('./webapp/')

image_names = ['villager-test.png', 'gold-test.png', 'champion-test.png']

for i in range(3):
    image = open_image(image_names[i])
    prediction = learn.predict(image)
    print(image_names[i] + ': ' + str(prediction[0]))
