function percent = getFaceSize(faceListName, largeFaceSize)
faceStrList = getList(faceListName);
faceNum = length(faceStrList);
faceSize = zeros(faceNum, 1);
for i = 1:faceNum
    faceLocation = str2num(faceStrList{i});
    faceSize(i) = faceLocation(4);
end
percent = sum(faceSize > largeFaceSize) / faceNum * 100;
fprintf('face larger than %d is %.1f\%\n', largeFaceSize, percent);
end
