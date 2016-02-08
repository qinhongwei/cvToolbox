function [imgList, rotateAngle] = getListRotate(imgListName)
fid = fopen(imgListName);
tline = fgetl(fid);
lineNum = 0;
while ischar(tline)
    lineNum = lineNum + 1;
    strCell = strsplit(tline);
    imgList{lineNum} = strCell{1};
    rotateAngle(lineNum) = str2num(strCell{2});
    tline = fgetl(fid);
end
fclose(fid);
imgList = strrep(imgList, '\', '/');
end
