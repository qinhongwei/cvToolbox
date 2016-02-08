function imgList = getList(imgListName);
fid = fopen(imgListName);
tline = fgetl(fid);
lineNum = 0;
while ischar(tline)
    lineNum = lineNum + 1;
    imgList{lineNum} = tline;
    tline = fgetl(fid);
end
fclose(fid);
imgList = strrep(imgList, '\', '/');
end
