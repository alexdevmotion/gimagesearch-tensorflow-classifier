# gimagesearch-tensorflow-classifier
A classifier similar to the google image search tool; categories: face, photo, clip art, line drawing
... with a state of the art GUI!


## Prerequisites
- Python 3.5 with pip (I used Anaconda)


## Setting up
```
pip install tensorflow
pip install tensorflow_hub
pip install flask
```
There may be other requirements which I missed; just do a pip install of whatever missing module pops up


## Firing up the app
#### Windows only
Linux users, I'm sure you'll figure out how to rewrite the complex start script :)
```
start.cmd
```


## Enriching the dataset
- Make a google image search
- Scroll down until images become irrelevant to your model
- Open the browser console
- Paste the js code from ``gimages_dataset_builder/js_console.js`` as indicated in the file's comments
- A ``urls.txt`` file will be downloaded with the paths to all images in the search

### Downloading images
Dataset builder params example (``photo_urls`` is the ``urls.txt`` exported by the js script)
```
--urls gimages_dataset_builder\image_lists\photo_urls --output tensorflow_classifier\input\photo
```


## Retraining the model
#### Uses ``https://www.tensorflow.org/hub/modules/google/imagenet/inception_v3/feature_vector/1`` by default
```
--image_dir input --summaries_dir model/retrain_logs --output_labels model/output_labels.txt --output_graph model/output_graph.pb
 --print_misclassified_test_images
 --random_crop 10 --random_scale 10 --random_brightness 10 --flip_left_right
```