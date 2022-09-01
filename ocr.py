from PIL import Image
import numpy as np

def hamming_distance(mat, template):
    dis = 0
    for h in range(25):
        for c in range(15):
            if mat[h][c] != template[h][c]:
                dis += 1
    return dis

def get_crop_vertex_pos(index):
    x1 = 3 + index * 15
    y1 = 7
    x2 = 17 + index * 15
    y2 = 31
    return x1, y1, x2 + 1, y2 + 1   

def ocr_number(img_file, index):
    img = Image.open("./test_imgs/" + img_file + ".png")
    x1, y1, x2, y2 = get_crop_vertex_pos(index)

    cropped_test_img = img.crop((x1, y1, x2, y2))

    grey_img = cropped_test_img.convert('L')
    grey_img_mat = np.array(grey_img)
    balck_img_mat = np.zeros((25, 15))

    for h in range(25):
        for w in range(15):
            if grey_img_mat[h][w] >= 200:
                balck_img_mat[h][w] = 255

    distance_pairs = []
    for number_index in range(10):
        template_img = Image.open("./template/" + str(number_index) + "_blacken.png")
        template_img_mat = np.array(template_img)
        distance = hamming_distance(balck_img_mat, template_img_mat)
        distance_pairs.append((distance, number_index))
    
    distance_pairs.sort()
    # print(distance_pairs)
    return str(distance_pairs[0][1])

def ocr_operator(img_file, index):
    img = Image.open("./test_imgs/" + img_file + ".png")
    x1, y1, x2, y2 = get_crop_vertex_pos(index)

    cropped_test_img = img.crop((x1, y1, x2, y2))

    grey_img = cropped_test_img.convert('L')
    grey_img_mat = np.array(grey_img)
    balck_img_mat = np.zeros((25, 15))

    for h in range(25):
        for w in range(15):
            if grey_img_mat[h][w] >= 200:
                balck_img_mat[h][w] = 255

    distance_pairs = []
    for op in ["minus", "plus", "multiply"]:
        template_img = Image.open("./template/" + op + "_blacken.png")
        template_img_mat = np.array(template_img)
        distance = hamming_distance(balck_img_mat, template_img_mat)
        distance_pairs.append((distance, op))

    distance_pairs.sort()
    # print(distance_pairs)

    if distance_pairs[0][1] == "minus":
        return "-"
    elif distance_pairs[0][1] == "plus":
        return "+"
    else:
        return "*"

def calc(img_file):
    equ_string = ""
    for index in range(5):
        if index % 2 == 0:
            equ_string += ocr_number(img_file, index)
        else:
            equ_string += ocr_operator(img_file, index)
    return equ_string

ocr = calc("2")
print(ocr)
print(eval(ocr))