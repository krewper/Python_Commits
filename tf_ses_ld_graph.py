import tensorflow as tf

def get_frozen_graph(graph_file):
    """Read Frozen Graph file from disk."""
    with tf.gfile.FastGFile(graph_file, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
    return graph_def
    
pb_fname = "./model/trt_graph.pb"
trt_graph = get_frozen_graph(pb_fname)

input_names = ['image_tensor']

#Create and load graph
tf_config = tf.ConfigProto()
tf_config.gpu_options.allow_growth = True
tf_sess = tf.session(config= tf_config)
tf.import_graph_def(trt_graph, name='')

tf_input = tf_sess.graph.get_tensor_by_name(input_names[0] + ':0')
tf_scores = tf_sess.graph.get_tensor_by_name('detection_scores: 0')
tf_boxes = tf_sess.graph.get_tensor_by_name('detection_boxes: 0')
tf_classes = tf_sess.graph.get_tensor_by_name('detection_classes: 0')
tf_num_detections = tf_sess.graph.get_tensor_by_name('num_detections: 0')