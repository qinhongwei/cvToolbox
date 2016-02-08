function writeNum(name, list)
fid = fopen(name, 'w');
for i = 1:length(list)
    fprintf(fid, '%.0f\n', list(i));
end
fclose(fid);
end
