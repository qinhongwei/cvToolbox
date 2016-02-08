function writeList(name, list)
fid = fopen(name, 'w');
for i = 1:length(list)
    fprintf(fid, '%s\n', list{i});
end
fclose(fid);
end
