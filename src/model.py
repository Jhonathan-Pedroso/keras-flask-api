from keras.applications import ResNet50


def load_model():
    print('Initializing model..', flush=True)
    model = ResNet50(weights='imagenet')
    print('Initialization done.', flush=True)

    return model
