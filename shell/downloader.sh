#!/usr/bin/env sh
start=$1
end=$2

for i in $(seq $start $end)
do
    {
        echo $i
        wget -c -nc -o "log"${i}".txt" "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_"${i}".tar"
    }&
done
wait

