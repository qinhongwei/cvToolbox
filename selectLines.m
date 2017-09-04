function selectLines(list_name, first, last)
% select lit [first, last] from list_name
fprintf('selecting list [%d, %d] from %s\n', first, last, list_name);
assert(first > 0, 'line number must be positive int');
time = tic();
fid_r = fopen(list_name, 'r');
save_name = strrep(list_name, '.txt', ['_', num2str(first), '_', num2str(last), '.txt']);
fid_w = fopen(save_name, 'w');
for i = 1:last
    line = fgetl(fid_r);
    if i >= first
        fprintf(fid_w, '%s\n', line);
    end
    if ~mod(i, 1000000)
        print_speed(i, toc(time), last);
    end
end
fclose(fid_w);
fclose(fid_r);
fprintf('done, selectLines used %.3f s\n', toc(time));
end
