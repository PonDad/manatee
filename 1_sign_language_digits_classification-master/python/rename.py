import os, shutil

original_dataset_dir = '/home/pondad/keras_js_examples/4_webcam_sign_language_digits_classification/python3/Dataset'
folder_name = ["0","1","2","3","4","5","6","7","8","9"]

for j in range(0, len(folder_name)):
    print (folder_name[j])

    files = os.listdir(original_dataset_dir + "/" + folder_name[j] + "/")

    for i in range(0, len(files)):
        print (files[i])
        root, extension = os.path.splitext(files[i])
        if files[i] == ".DS_Store":
            print("This is no image.")
        elif extension == ".png" or ".jpeg" or ".jpg":
            shutil.move(original_dataset_dir + "/" + folder_name[j] + "/" + files[i], original_dataset_dir + "/" + folder_name[j] + "/" + folder_name[j] + "_" + str(i + 1) + ".jpg")

print("Rename Done.")
