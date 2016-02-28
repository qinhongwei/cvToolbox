function writeMatInt(name, list)
fid = fopen(name, 'w');
for i = 1:size(list, 1)
    fprintf(fid, '%.0f ', list(i, :));
    fprintf(fid, '\n');
end
fclose(fid);
end
