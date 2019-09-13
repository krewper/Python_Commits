class AlexNet_model:

    def __init__(self):
        self.AlexNet = (imported AlexNet)
        self.optimizer = tf.train.SGD

    def fit(X):
        ouput = self.AlexNet(X)
        return output

    def loss(output, labels):
        return tf,reduce_mean(tf.sub(ouput, label)))
    
    def train(loss):
        self.optimizer(lr).minimize(loss)
        