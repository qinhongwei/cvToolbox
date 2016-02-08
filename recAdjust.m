function faceBox = recAdjust(recBox, height, width)
faceBox(1) = max(1, recBox(1));
faceBox(2) = max(1, recBox(2));
x2 = recBox(1) + recBox(3) - 1;
y2 = recBox(2) + recBox(4) - 1;
faceBox(3) = min(width, x2) - faceBox(1) + 1;
faceBox(4) = min(height, y2) - faceBox(2) + 1;
