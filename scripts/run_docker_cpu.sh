#!/bin/bash
# Launch an experiment using the docker cpu image

cmd_line="$@"

echo "Executing in the docker (cpu image):"
echo $cmd_line

docker run -it --rm --network host --ipc=host \
 --mount src=$(pwd),target=/root/code/pytorch_agents,type=bind pytorch_agents/pytorch_agents-cpu:latest \
  bash -c "cd /root/code/pytorch_agents/ && $cmd_line"
