# How to run a docker?

```shell
docker --version
cd the/path/to/repo/Datacon/Challenge1/AI_cq1_attachment/docker-cq1 # If you want to run cq1
docker build -t ai_cq1 . # ai_cq1 is the name of image
mkdir result
docker ps -a
docker cp <CONTAINER ID>:/result.txt ./result/result.txt
```