from PIL import Image
 
def get_crop_vertex_pos(index):
    x1 = 3 + index * 15
    y1 = 7
    x2 = 17 + index * 15
    y2 = 31
    return x1, y1, x2 + 1, y2 + 1   

def crop_template(img_file, save_name, index):
    x1, y1, x2, y2 = get_crop_vertex_pos(index)
    img = Image.open(img_file)
    cropped_template = img.crop((x1, y1, x2, y2))
    cropped_template.save("./template/" + save_name)

crop_template("./imgs/4.png", "0.png", 2)
crop_template("./imgs/4.png", "1.png", 4)
crop_template("./imgs/0.png", "2.png", 2)
crop_template("./imgs/0.png", "3.png", 0)
crop_template("./imgs/5.png", "4.png", 0)
crop_template("./imgs/1.png", "5.png", 4)
crop_template("./imgs/1.png", "6.png", 0)
crop_template("./imgs/3.png", "7.png", 4)
crop_template("./imgs/3.png", "8.png", 0)
crop_template("./imgs/6.png", "9.png", 0)

crop_template("./imgs/3.png", "plus.png", 3)
crop_template("./imgs/1.png", "minus.png", 1)
crop_template("./imgs/3.png", "multiply.png", 1)
