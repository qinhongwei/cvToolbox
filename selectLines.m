function selectLines(list_name, first, last)
% select lit [first, last] from list_name
fprintf('selecting list [%d, %d] from %s\n', first, last, list_name);
assert(first > 0, 'line number must be positive int');
time = tic();
fid_r = fopen(list_name, 'r');
save_name = strrep(list_name, '.txt', ['_', num2str(first), '_', num2str(last), '.txt']);
fid_w = fopen(save_name, 'w');
for i = first:last
    line = fgetl(fid_r);
    fprintf(fid_w, '%s\n', line);
    if ~mod(i, 1000000)
        print_speed(i, toc(time), last - first + 1);
    end
end
fclose(fid_w);
fclose(fid_r);
fprintf('done, selectLines used %.3f s\n', toc(time));
end
