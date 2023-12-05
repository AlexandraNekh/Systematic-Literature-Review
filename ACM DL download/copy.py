import os


foldername=os.getcwd()+'/bib/'  #folder name
all_files = os.listdir(foldername) #get all filenames
bib_files =  [ filename for filename in all_files if filename.endswith('.bib') ] #get  .bib filenames
print(bib_files)

for bib_file in bib_files: #loop over .bib files
    # open both files
    print(bib_file)
    with open(os.getcwd()+'/bib/'+bib_file,'r', encoding="utf8") as firstfile, open(foldername+'copy.bib','a', encoding="utf8") as secondfile:

        # read content from first file
        for line in firstfile:
            # append content to second file
            secondfile.write(line)