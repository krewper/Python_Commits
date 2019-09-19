import os
import cv2
import numpy as np
import tensorflow as tensorflow
import sys

sys.path.append("..")
#utility import
from utils import label_map_util
from utils import visualization_utils as visualization_utils

#Name of the directory containing the object detection
MODEL_NAME = 'inference_graph'
IMAGE_NAME = '11man.jpg'

CWD_PATH = os.getcwd()

PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')

PATH_TO_IMAGE = os.path.join(CWD_PATH, IMAGE_NAME)

NUM_CLASSES = 2

#Load the label map
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(
    label_map, max_num_classes = NUM_CLASSES, use_display_name = True)
category_index = label_map_util.create_category_index(categories)

#load the tensorflow model into memory
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name = '')
    sess = tf.Session(graph = detection_graph)    

#define input and output tensors(i.e. data) for the object detection classifier
#input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')

detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

#num of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

#load the image
image = cv2.imread(PATH_TO_IMAGE)
image_expanded = np.expand_dims(image, axis = 0)

#perform actual object detection
(boxes, scores, classes, num) = sess.run(
    [detection_boxes, detection_scores, detection_classes, num_detections])
    feed_dict = {image_tensor: image_expanded}    
)

#draw the results of the detection(aka 'visualise the results')
vis_util.visualize_boxes_and_labels_on_image_array(
    image, np.squeeze(boxes)
    np.squeeze(classes.astype(np.int32),
    np.squeeze(scores)
    category_index,
    use_normalized_coordinates = True,
    line_thickness = 8,
    min_score_thresh = 0.60)
)

#all the results have been drawn on the image, now display the image.
cv2.imshow('Object detector')

#press any key to close the image
cv2.waitKey(0)

#clean up
cv2.destroyAllWindows()