function getGif(imgListName)
imgList = getList(imgListName);
gifIndex = [];
for i = 1:length(imgList)
    if ~strcmp(imgList{i}(end-3:end), '.jpg') && ~strcmp(imgList{i}(end-3:end), '.JPG')
       gifIndex = [gifIndex, i]; 
   end
end
gifList = imgList(gifIndex);
gifListName = strrep(imgListName, '.txt', '_NonJPG.txt');
writeList(gifListName, gifList);
end
