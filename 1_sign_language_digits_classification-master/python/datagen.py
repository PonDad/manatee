import os, shutil

original_dataset_dir = 'Dataset'
base_dir = 'hand_sign_digit_data'
os.mkdir(base_dir)

train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)
validation_dir = os.path.join(base_dir, 'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir)

folder_name = ["0","1","2","3","4","5","6","7","8","9"]

for j in range(0, len(folder_name)):
    os.mkdir(os.path.join(train_dir, folder_name[j]))
    os.mkdir(os.path.join(validation_dir, folder_name[j]))
    os.mkdir(os.path.join(test_dir, folder_name[j]))

    fnames = [folder_name[j] + '_{}.jpg'.format(i) for i in range(1,101)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, folder_name[j], fname)
        dst = os.path.join(train_dir, folder_name[j], fname)
        shutil.copyfile(src, dst)

    fnames = [folder_name[j] +'_{}.jpg'.format(i) for i in range(102, 151)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, folder_name[j], fname)
        dst = os.path.join(validation_dir, folder_name[j], fname)
        shutil.copyfile(src, dst)

    fnames = [folder_name[j] +'_{}.jpg'.format(i) for i in range(151, 201)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, folder_name[j], fname)
        dst = os.path.join(test_dir, folder_name[j], fname)
        shutil.copyfile(src, dst)

print("Data generate Done.")
