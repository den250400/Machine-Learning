import numpy
import cv2

#For shuffling data and labels in unison
def shuffle_in_unison(a, b):
    assert len(a) == len(b)
    shuffled_a = numpy.empty(a.shape, dtype=a.dtype)
    shuffled_b = numpy.empty(b.shape, dtype=b.dtype)
    permutation = numpy.random.permutation(len(a))
    for old_index, new_index in enumerate(permutation):
        shuffled_a[new_index] = a[old_index]
        shuffled_b[new_index] = b[old_index]
    return shuffled_a, shuffled_b

def shift_hsv(image, delta_h, delta_s, delta_v):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #convert it to hsv
    
    new_hue = numpy.copy(hsv[:, :, 0])
    new_saturation = numpy.copy(hsv[:, :, 1])
    new_value = numpy.copy(hsv[:, :, 2])
    cv2.add(new_hue, delta_h, new_hue)
    cv2.add(new_saturation, delta_s, new_saturation)
    cv2.add(new_value, delta_v, new_value)
    hsv[:, :, 0] = new_hue
    hsv[:, :, 1] = new_saturation
    hsv[:, :, 2] = new_value
    image_processed = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return image_processed