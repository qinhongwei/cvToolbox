function splitList(list_name, batch_length, is_shuffle)
%% split one list to multiple list
%% input: list_name, batch_length, is_shuffle
rng(2);
list = getList(list_name);
if is_shuffle
    list = list(randperm(length(list)));
end
list_length = length(list);
batch_num = ceil(list_length / batch_length);
t = tic();
for batch_index = 1:batch_num
    list_index = (1 + batch_length * (batch_index - 1)) : min(batch_length * batch_index, list_length);
    list_current = list(list_index);
    list_current_name = strrep(list_name, '.txt', ['_', num2str(batch_index), '.txt']);
    writeList(list_current_name, list_current);
    print_speed(batch_index, toc(t), batch_num);
end
