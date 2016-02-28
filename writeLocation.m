function writeLocation(name, list)
% list is a cell, each item is a vector
fid = fopen(name, 'w');
tic();
for i = 1:length(list)
    fprintf(fid, '%.0f ', list{i});
    fprintf(fid, '\n');
    if mod(i, 10000) == 0
        print_speed(i, toc(), length(list));
    end
end
fclose(fid);
end
