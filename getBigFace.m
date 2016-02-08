function getBigFace(bigFaceName, bigFaceBoxName, imgPath, savePath)
bigFaceList = getList(bigFaceName);
bigFaceBoxList = getList(bigFaceBoxName);
bigFaceNum = length(bigFaceList);
notExistIndex = [];
tic;
for i = 1:bigFaceNum
    dirName = fileparts(bigFaceList{i});
    savePathFull = fullfile(savePath, dirName);
    if ~exist(savePathFull, 'dir')
        mkdir(savePathFull);
    end;
    imgPathFull = fullfile(imgPath, bigFaceList{i});
    if ~exist(imgPathFull, 'file')
        notExistIndex = [notExistIndex, i];
        fprintf('%d %s\n', i, imgPathFull);
        continue;
    end
    copyfile(imgPathFull, savePathFull);
    h = toc;
    if ~mod(i, 500)
        fprintf('%d / %d \t', i, bigFaceNum);
        fprintf('speed: %.3fs per image, %.1f minites to go.\n', h/i, h / i * (bigFaceNum - i) / 60); 
    end
end
shrinkList = setdiff(1:bigFaceNum, notExistIndex);
bigFaceListShrink = bigFaceList(shrinkList);
bigFaceBoxListShrink = bigFaceBoxList(shrinkList);
bigFaceNameShrink = strrep(bigFaceName, '.txt', '_shrink.txt');
bigFaceBoxNameShrink = strrep(bigFaceBoxName, '.txt', '_shrink.txt');
writeList(bigFaceNameShrink, bigFaceListShrink);
writeList(bigFaceBoxNameShrink, bigFaceBoxListShrink);
end
