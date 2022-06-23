import os
def rename_file(old_folder_path,new_folder_path):    
    for file in os.listdir(old_folder_path):
        old_file_path = os.path.join(old_folder_path,file)
        if os.path.isfile(old_file_path):
            old_file_name = os.path.basename(old_file_path)
            old_file_title,ext = os.path.splitext(old_file_name)
            new_file_name = str(int(old_file_title)+100)+ext
            new_file_path = os.path.join(new_folder_path,new_file_name)
            
            os.rename(old_file_path,new_file_path)



home = os.environ['HOME']            
old_folder_path = home+"/research_project/benchmark-tracker/ai_benchmark/data2/enhancement"
new_folder_path = home+"/research_project/benchmark-tracker/ai_benchmark/data/enhancement"
rename_file(old_folder_path,new_folder_path)