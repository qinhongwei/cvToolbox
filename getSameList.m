function getSameList(listName1, listName2, listName)
list1 = getList(listName1);
list2 = getList(listName2);
list = intersect(list1, list2);
writeList(listName, list);
end
