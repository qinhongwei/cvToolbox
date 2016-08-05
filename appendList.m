function appendList(name, list)
%% write string list to file, append mode
%% input: name list
%% by Hongwei Qin on Aug. 5, 2016
fid = fopen(name, 'a');
for i = 1:length(list)
    fprintf(fid, '%s\n', list{i});
end
fclose(fid);
end
