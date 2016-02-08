function getGif(imgListName)
imgList = getList(imgListName);
gifIndex = [];
for i = 1:length(imgList)
   if strcmp(imgList{i}(end-3:end), '.gif')
       gifIndex = [gifIndex, i]; 
   end
end
gifList = imgList(gifIndex);
gifListName = strrep(imgListName, '.txt', '_gif.txt');
writeList(gifListName, gifList);
end
