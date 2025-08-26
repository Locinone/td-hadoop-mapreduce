#!/bin/bash

LOCAL_BASE=./twitter_data_partitioned_local
HDFS_BASE=/twitter_data_partitioned

# Récupère l'ID du conteneur namenode automatiquement
NAMENODE_CONTAINER=$(docker ps | grep hadoop_namenode | awk '{print $1}')

for year_dir in $LOCAL_BASE/year=*; do
    year=$(basename $year_dir)
    for month_dir in $year_dir/month=*; do
        month=$(basename $month_dir)
        hdfs_path=$HDFS_BASE/$year/$month

        echo "Uploading $month_dir to $hdfs_path"

        # Crée le dossier HDFS dans le conteneur
        docker exec -i $NAMENODE_CONTAINER bash -c "hdfs dfs -mkdir -p $hdfs_path"

        # Copier le fichier depuis l'hôte vers le conteneur et le mettre dans HDFS
        docker cp $month_dir/tweets.json $NAMENODE_CONTAINER:/tmp/tweets.json
        docker exec -i $NAMENODE_CONTAINER bash -c "hdfs dfs -put -f /tmp/tweets.json $hdfs_path/"
        docker exec -i $NAMENODE_CONTAINER bash -c "rm /tmp/tweets.json"
    done
done
