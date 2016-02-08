function face_location_data = getLocation(face_location_name, lineNum);
    fprintf('reading %s\n', face_location_name);
    face_location_data = cell(lineNum, 1);
    fid = fopen(face_location_name);
    for i = 1:lineNum
        face_location_data{i} = str2num(fgets(fid));
        if mod(i,10000) == 0
            fprintf('%d / %d finished.\n', i, lineNum);
        end;
    end;
    fclose(fid);
end
