function getUniqueList(imgListName)
list = getList(imgListName);
list = unique(list);
writeList(strrep(imgListName, '.txt', '_unique.txt'), list);
end
