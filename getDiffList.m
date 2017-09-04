function getDiffList(listName1, listName2, listName)
%% get diff list of list1, list2
%% input: listName1, listName2, listName)
list1 = getList(listName1);
list2 = getList(listName2);
list = setdiff(list1, list2);
writeList(listName, list);
end
