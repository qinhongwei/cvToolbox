function print_speed(i, t, n)
%% printf speed of for loop
%% i is index; t is used time; n is total number.
%% by Hongwei Qin on Dec. 3, 2015
average_time = t / i;
remaining_time = (n - i) * average_time;
remaining_hour = floor(remaining_time / 3600);
remaining_min = round(remaining_time / 60 - remaining_hour * 60);
fprintf('%d / %d \t speed: %.3fs/iter, %d:%d (H:M) to go\n', i, n, average_time, remaining_hour, remaining_min); 
end
