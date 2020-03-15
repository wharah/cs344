'''
@assignment: Lab 6, Exercise 3
@student: Sarah Whitten
@date: March 14, 2020
'''

import numpy as np
from tensorflow.python.keras.datasets import boston_housing

# load data
(train_images, train_labels), (test_images, test_labels) = boston_housing.load_data()


# print number of training and testing examples
# from the class example guide
def print_structures():
    print(
        'training images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n\n'.format(
            len(train_images),
            train_images.ndim,
            train_images.shape,
            train_images.dtype
        ),
        'testing images \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {} \
            \n\tvalues: {}\n'.format(
            len(test_labels),
            train_labels.ndim,
            test_labels.shape,
            test_labels.dtype,
            test_labels
        )
    )


# each first block prints training images, second block prints testing images
print_structures()

'''
I've been trying to run this but my computer isn't able to verify the "certificate" from tensorflow for the boston
housing dataset. Here is what the error looks like:

Exception: URL fetch failure on https://storage.googleapis.com/tensorflow/tf-keras-datasets/boston_housing.npz: None --
 [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777)
 
And that error is just at the end of a very long line of errors coming from not being able to get the thing from
tensorflow. But if my computer could verify the certificate, I feel like my code should work because it's basically the
same as the code you put in the class example that's linked in the lab.
'''
