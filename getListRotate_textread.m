function [imgList, rotateAngle] = getListRotate_textread(imgListName)
[imgList, rotateAngle] = textread(imgListName, '%s %d');
imgList = strrep(imgList, '\', '/');
writeList(strrep(imgListName, '.txt', '_name.txt'), imgList);
writeNum(strrep(imgListName, '.txt', '_rotate.txt'), rotateAngle);
end
