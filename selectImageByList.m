function selectImageByList(listName, imgPath, savePath)
%% input: listName, imgPath, savePath
imageList = getList(listName);
imageList = unique(imageList); % remove duplicated
imageNum = length(imageList);
notExistIndex = [];
if ~exist(savePath, 'dir')
    mkdir(savePath)
end
tic;
for i = 1:imageNum
    dirName = fileparts(imageList{i});
    savePathFull = fullfile(savePath, dirName);
    if ~exist(savePathFull, 'dir')
        mkdir(savePathFull);
    end;
    imgPathFull = fullfile(imgPath, imageList{i});
    if ~exist(imgPathFull, 'file')
        notExistIndex = [notExistIndex, i];
        fprintf('%d %s\n', i, imgPathFull);
        continue;
    end
    copyfile(imgPathFull, savePathFull);
    h = toc;
    if ~mod(i, 500)
        fprintf('%d / %d \t', i, imageNum);
        fprintf('speed: %.3fs per image, %.1f minites to go.\n', h/i, h / i * (imageNum- i) / 60); 
    end
end
if ~isempty(notExistIndex)
    shrinkList = setdiff(1:imageNum, notExistIndex);
    imageListShrink = imageList(shrinkList);
    listNameShrink = strrep(listName, '.txt', '_shrink.txt');
    writeList(listNameShrink, imageListShrink);
end
