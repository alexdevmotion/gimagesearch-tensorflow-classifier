# gimagesearch-tensorflow-classifier
A classifier similar to the google image search tool; categories: face, photo, clip art, line drawing
... with a state of the art GUI!


## Prerequisites
- Python 3.5 with pip (I used 64bit Anaconda 5.2.0)


## Setup
```
pip install tensorflow
pip install tensorflow_hub
pip install flask
```

## Firing up the app
#### Windows only
Linux users, I'm sure you'll figure out how to rewrite the complex start script :)
```
start.cmd
```
Note: The python installation and Scripts folders need to be in your ``%PATH%``


## Enriching the dataset
- Make a google image search
- Scroll down until images become irrelevant to your model
- Open the browser console
- Paste the js code from ``gimages_dataset_builder/js_console.js`` as indicated in the file's comments
- A ``urls.txt`` file will be downloaded with the paths to all images in the search
- Download the images using the download script

### Downloading images
Image downloader params example (``photo_urls`` is the ``urls.txt`` exported by the js script)
```
--urls gimages_dataset_builder\image_lists\photo_urls --output tensorflow_classifier\input\photo
```
This will automatically avoid unsupported formats and try to delete invalid images at the end, however, invalid images may still remain (sometimes, image extensions are not correct).
If you get an error during training, just delete the image.


## Retraining the model
Followed official guide for retraining an image classifier for new categories: https://www.tensorflow.org/tutorials/image_retraining
#### Defaults:
- model: https://www.tensorflow.org/hub/modules/google/imagenet/inception_v3/feature_vector/1
- learning rate: 0.01
- steps: 4000
```
--image_dir input --summaries_dir model/retrain_logs --output_labels model/output_labels.txt --output_graph model/output_graph.pb
 --print_misclassified_test_images
```
Using the included dataset and the params above, on a Core i5 @ 3.3Ghz + Nvidia GTX 970 using latest tensorflow-gpu, CUDA, cuDNN it took ~ 25 mins

I also attempted to use ``--random_crop 10 --random_scale 10 --random_brightness 10 --flip_left_right`` but training took way too long on my machine (30 mins for 30 steps).


## Training & testing results
90% train, 10% test
```
INFO:tensorflow:Final test accuracy = 98.1% (N=424)
INFO:tensorflow:=== MISCLASSIFIED TEST IMAGES ===
INFO:tensorflow:                                            input\clipart\00000518.jpg  line
INFO:tensorflow:                                            input\clipart\00000518.jpg  line
INFO:tensorflow:                                               input\face\00000326.jpg  line
INFO:tensorflow:                                               input\face\00000326.jpg  line
INFO:tensorflow:                                               input\line\00000315.jpg  clipart
INFO:tensorflow:input\line\stock-vector-sea-life-wildlife-animal-white-shark-decal-art-vector-isolated-decor-tribal-tattoo-design-632947772.jpg  clipart
INFO:tensorflow:                                               input\line\00000315.jpg  clipart
INFO:tensorflow:input\line\stock-vector-sea-life-wildlife-animal-white-shark-decal-art-vector-isolated-decor-tribal-tattoo-design-632947772.jpg  clipart
```