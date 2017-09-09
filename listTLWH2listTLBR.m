function listTLWH2TLBR(imgListName)
%% change bounding box lists from TLWH 2 TLBR
%% input: imageListName(each line in %s %d %d %d %d ... format
%% %d %d %d %d is TLWH
fid = fopen(imgListName);
saveListName = strrep(imgListName, '.txt', 'TLBR.txt');
fid_w = fopen(saveListName, 'w');
tline = fgetl(fid);
while ischar(tline)
    strCell = strsplit(tline);
    imgName = strCell{1};
    x1 = str2num(strCell{2});
    y1 = str2num(strCell{3});
    w = str2num(strCell{4});
    h = str2num(strCell{5});
    x2 = x1 + w - 1;
    y2 = y1 + h - 1;
    tline_end = strjoin(strCell(6:end));
    fprintf(fid_w, '%s %d %d %d %d %s\n', imgName, x1, y1, x2, y2, tline_end);
    tline = fgetl(fid);
end
fclose(fid);
fclose(fid_w);

end
