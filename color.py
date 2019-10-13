import binascii
import struct
from PIL import Image
from scipy import cluster
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import colorsys

NUM_CLUSTERS = 5

class artCritic():
    def __init__(self, img):
        self.img = img # = Image.open("reference_image.jpg")
        self.img = img.resize((100, 100))
    
    def findColor(self):
        img_arr = np.asarray(img)
        shape = img_arr.shape
        img_arr = img_arr.reshape(scipy.product(shape[:2]), shape[2]).astype(float)
        
        # find clusters
        codes, dist = scipy.cluster.vq.kmeans(img_arr, NUM_CLUSTERS)

        vecs, dist = scipy.cluster.vq.vq(img_arr, codes)         # assign codes
        counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

        index_max = scipy.argmax(counts)                    # find most frequent
        peak = codes[index_max]
        colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
        print('most frequent is %s (#%s)' % (peak, colour))
        return colorsys.rgb_to_hsv(peak[0], peak[1], peak[2])

def main():
    img = Image.open("reference_image.jpg")
    img = img.resize((100, 100))
    img_arr = np.asarray(img)
    shape = img_arr.shape
    img_arr = img_arr.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

    print('finding clusters')
    codes, dist = scipy.cluster.vq.kmeans(img_arr, NUM_CLUSTERS)
    print('cluster centres:\n', codes)

    vecs, dist = scipy.cluster.vq.vq(img_arr, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

    index_max = scipy.argmax(counts)                    # find most frequent
    peak = codes[index_max]
    colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    print('most frequent is %s (#%s)' % (peak, colour))
    print(colorsys.rgb_to_hsv(peak[0], peak[1], peak[2]))
    

if __name__ == "__main__":
    main()