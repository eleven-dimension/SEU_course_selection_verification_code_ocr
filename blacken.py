from PIL import Image
import numpy as np

def blacken(img_file):
    img = Image.open("./template/" + img_file + ".png")
    grey_img = img.convert('L')
    grey_img_mat = np.array(grey_img)
    balck_img_mat = np.zeros((25, 15))
    
    for h in range(25):
        for w in range(15):
            if grey_img_mat[h][w] >= 200:
                balck_img_mat[h][w] = 255

    balck_img = Image.fromarray(balck_img_mat.astype('uint8')).convert('L')
    balck_img.save("./template/" + img_file + "_blacken.png")


for index in range(10):
    blacken(str(index))
blacken("minus")
blacken("plus")
blacken("multiply")
