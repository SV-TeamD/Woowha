#!/bin/bash

LWHITE="\033[1;37m"
LCYAN="\033[1;36m"

echo "${LCYAN}Model Server Start"

echo ""
echo "${LWHITE}Download Pretrained Model Weights"
bash ./load-models.sh
echo ""
echo "${LWHITE}RUN TEST"
pytest
echo ""
echo "${LWHITE}Create image from GAN"
echo "Pytorch Models CartoonGAN [Chen et al., CVPR18]. With the released pretrained models by the authors."

## wait-for-it.sh ##
# Usage:
#     ...
#     -- COMMAND ARGS             Execute command with args after the test finishes
bash ../wait-for-it.sh rabbitmq:15672 -s -t 30
python3 app/worker.py
# python3 network/Runner.py
