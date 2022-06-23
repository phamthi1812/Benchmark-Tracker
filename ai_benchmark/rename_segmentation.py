import os
def rename_file(old_folder_path,new_folder_path):    
    for file in os.listdir(old_folder_path):
        old_file_path = os.path.join(old_folder_path,file)
        if os.path.isfile(old_file_path):
            old_file_name = os.path.basename(old_file_path)
            old_file_title,ext = os.path.splitext(old_file_name)
            if len(old_file_title) >10:
                if len(old_file_title)==11:
                    old_file_nb = old_file_title[0]
                if len(old_file_title)==12:
                    old_file_nb = old_file_title[0:2]
                new_file_name = str(int(old_file_nb)+30)+'_segmented'+ext
            if len(old_file_title) <3:
                old_file_nb = old_file_title
                new_file_name = str(int(old_file_nb)+30)+ext

            
            new_file_path = os.path.join(new_folder_path,new_file_name)

            os.rename(old_file_path,new_file_path)



home = os.environ['HOME']            
old_folder_path = home+"/research_project/benchmark_tracker/ai_benchmark/data2/segmentation"
new_folder_path = home+"/research_project/benchmark_tracker/ai_benchmark/data/segmentation"
rename_file(old_folder_path,new_folder_path)