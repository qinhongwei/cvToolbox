# unzip zip file
for i in $(find -name "*.zip"); do unzip -od ${i%/*} $i; done
# unrar rar file
for i in $(find -name "*.rar"); do mkdir -p ${i%/*} && rar x $i ${i%/*}; done
# find video file
find -type f ! \( -name "*.zip" -o -name "*.rar" -o -name "*.txt" -o -name "*.py" -o -name "*.sh" \) > all_video_list.txt
python videolist2frame.py --video_list all_video_list.txt --save_dir frames
