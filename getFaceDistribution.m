function getFaceDistribution(faceListName)
faceStrList = getList(faceListName);
faceNum = length(faceStrList);
faceSize = zeros(faceNum, 1);
for i = 1:faceNum
    faceLocation = str2num(faceStrList{i});
    faceSize(i) = faceLocation(4);
end
percent_lessthan20 = sum(faceSize < 20) / faceNum * 100;
fprintf('face < %d is %.1f%%\n', 20, percent_lessthan20);
percent_20 = sum(faceSize >= 20 & faceSize < 50) / faceNum * 100;
fprintf('face %d - %d is %.1f%%\n', 20, 50, percent_20);
percent_50 = sum(faceSize >= 50 & faceSize < 100) / faceNum * 100;
fprintf('face %d - %d is %.1f%%\n', 50, 100, percent_50);
percent_100 = sum(faceSize >= 100 & faceSize < 200) / faceNum * 100;
fprintf('face %d - %d is %.1f%%\n', 100, 200, percent_100);
percent_200 = sum(faceSize >= 200 & faceSize < 300) / faceNum * 100;
fprintf('face %d - %d is %.1f%%\n', 200, 300, percent_200);
percent_300 = sum(faceSize >= 300 & faceSize < 400) / faceNum * 100;
fprintf('face %d - %d is %.1f%%\n', 300, 400, percent_300);
percent_400 = sum(faceSize >= 400 & faceSize < 500) / faceNum * 100;
fprintf('face %d - %d is %.1f%%\n', 400, 500, percent_400);
percent_500 = sum(faceSize >= 500) / faceNum * 100;
fprintf('face > %d is %.1f%%\n', 500, percent_500);

end
