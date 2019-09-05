from imageai.Prediction import ImagePrediction
import os
import threading

execution_path = os.getcwd()
prediction.setModelTypeAsDenseNet()
prediction.setModelPath(os.path.join(execution_path, "C:\\Users\aditys\Documents\Image Manipulation"))

picturesfolder = os.environ["aditys"] + "\\Pictures\\"
allfiles = os.listdir(picturesfolder)

class PredictionThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        prediction.loadModel()
        for eachPicture in allfiles:
            if eachPicture.endswith(".png") or eachPicture.endswith(".jpg"):
                predictions, percentage_probabilities = prediction.predictImage(picturesfolder + eachPicture, result_count=1)
                for prediction, percentage_probability in zip(predictions, probabilities):
                    print(prediction , " : " , percentage_probability)

predictionThread = PredictionThread ()
predictionThread.start()