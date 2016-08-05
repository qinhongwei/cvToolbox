function writeList(name, list)
%% write string list to file
%% input: name list
fid = fopen(name, 'w');
for i = 1:length(list)
    fprintf(fid, '%s\n', list{i});
end
fclose(fid);
end
