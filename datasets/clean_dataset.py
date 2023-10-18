import argparse
import os
import shutil



parser = argparse.ArgumentParser()

parser.add_argument('dataset', default=None, help='Specify the dataset')

parser.add_argument('--force_run', action='store_true')


args = parser.parse_args()

dataset = args.dataset
force_run = args.force_run

print(force_run)

def get_yon():
    while True:
        user_input = input("Enter 'yes' or 'no': ").strip().lower()
        if user_input == 'yes':
            break
        elif user_input == 'no':
            break
        else:
            print(f"Please enter yes or no")
            continue
    return user_input

def main():
    if dataset is not None:
        print(f'Dataset specified: {dataset}')
    else:
        print('No dataset specified.')
        return

    datasets = os.listdir()

    assert dataset in datasets

    dataset_sub_folders = os.listdir(dataset)
    
    # need to prepare the dataset
    if "test" not in dataset_sub_folders or "train" not in dataset_sub_folders or force_run == True: 
        if "rgb" not in dataset_sub_folders or "poses" not in dataset_sub_folders or "calibration" not in dataset_sub_folders:
            print(f"{dataset} does not have rgb, poses or calibration folders. Please check your datasets!")
        else:
            print(f"Do you want to check the dataset? (Check if the three folders have different files).")
            user_input = get_yon()
            if user_input == 'no':
                print(f"Nothing to do. Bye...")
                return
            elif user_input == 'yes':
                print(f'Now checking {dataset}')
                rgb_folder_path = os.path.join(dataset, 'rgb')
                poses_folder_path = os.path.join(dataset, 'poses')
                calibration_folder_path = os.path.join(dataset, 'calibration')
                rgb_files = sorted(os.listdir(rgb_folder_path))
                rgb_ids = set([item.split('.')[0] for item in rgb_files])
                poses_files = sorted(os.listdir(poses_folder_path))
                poses_ids = set([item.split('.')[0] for item in poses_files])
                calibration_files = sorted(os.listdir(calibration_folder_path))
                calibration_ids = set([item.split('.')[0] for item in calibration_files])

                if rgb_ids == poses_ids and rgb_ids == calibration_ids:
                    print(f"Check {dataset} PASS")
                else:
                    print(f"Check {dataset} FAILED. Need to clean the dataset.")

                    keep_list = sorted(list(rgb_ids.intersection(poses_ids, calibration_ids)))

                    print(f"######## Before cleaning ########")
                    print(f"Len of rgb files {len(rgb_files)}")
                    print(f"Len of poses files {len(poses_files)}")
                    print(f"Len of calibration files {len(calibration_files)}")
                    print(f"We are going to keep {len(keep_list)} files to align files in the three folders.")
                    user_input = get_yon()
                    if user_input == 'no':
                        print(f"User refuse to delete files. Exiting...")
                        return
                    elif user_input == 'yes':
                        # clean rgb folder
                        for filename in rgb_files:
                            fileID = filename.split('.')[0]
                            if fileID not in keep_list:
                                os.remove(os.path.join(rgb_folder_path, filename))
                        
                        # clean poses folder
                        for filename in poses_files:
                            fileID = filename.split('.')[0]
                            if fileID not in keep_list:
                                os.remove(os.path.join(poses_folder_path, filename))

                        # clean calibration folder
                        for filename in calibration_files:
                            fileID = filename.split('.')[0]
                            if fileID not in keep_list:
                                os.remove(os.path.join(calibration_folder_path, filename))
                        
                    rgb_files = sorted(os.listdir(rgb_folder_path))
                    poses_files = sorted(os.listdir(poses_folder_path))
                    calibration_files = sorted(os.listdir(calibration_folder_path))
                    print(f"######## After cleaning ########")
                    print(f"Len of rgb files {len(rgb_files)}")
                    print(f"Len of poses files {len(poses_files)}")
                    print(f"Len of calibration files {len(calibration_files)}")
                    

            print()
            print(f"{dataset} dataset does not have train and test folder. Do you want to split it?")
            user_input = input("Enter 'yes' or 'no': ").strip().lower()
            if user_input == 'yes':
                while True:
                    try:
                        user_input = float(input("Enter a number between 0.5 and 1 as training dataset ratio: "))
                        if 0.5 <= user_input <= 1:
                            break
                        else:
                            print("Input must be between 0.5 and 1. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number between 0 and 1.")
            
                # split training and testing dataset
                file_count = len(sorted(os.listdir(rgb_folder_path)))
                train_count = int(user_input * file_count)
                test_count = file_count - train_count

                # make dirs
                folder_list = ['train', 'test']
                subfolder_list = ['rgb', 'poses', 'calibration']
                for folder in folder_list:
                    for subfolder in subfolder_list:
                        os.makedirs(os.path.join(dataset, folder, subfolder), exist_ok=True)
                
                id_list = [item.split(".")[0] for item in sorted(os.listdir(rgb_folder_path))]

                for i, id in enumerate(id_list):
                    for subfolder in subfolder_list:
                        if subfolder == 'rgb':
                            filename = id + '.jpg'
                        else:
                            filename = id + '.txt'
                        source_path = os.path.join(dataset, subfolder, filename)
                        dest_path = os.path.join(dataset, 'train' if i < train_count else 'test', subfolder, filename)
                        try:
                            shutil.move(source_path, dest_path)
                        except Exception as e:
                            print(f"Error {e}")
                
                shutil.rmtree(rgb_folder_path)
                shutil.rmtree(poses_folder_path)
                shutil.rmtree(calibration_folder_path)

                 



            elif user_input == 'no':
                print("You entered 'no'. Exiting.")
                return
    else:
        print(f"Datatset {dataset} has train and test folder. You should be good to go.")


if __name__ == "__main__":
    main()
    



