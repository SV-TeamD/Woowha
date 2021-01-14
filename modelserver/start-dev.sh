#!/bin/bash

LWHITE="\033[1;37m"
LCYAN="\033[1;36m"

echo ""
echo "${LWHITE}Download Pretrained Model Weights"
bash ./load-models.sh
# echo ""
# echo "${LWHITE}RUN TEST"
# pytest
echo ""
echo "${LWHITE}Pytorch Models CartoonGAN [Chen et al., CVPR18]. With the released pretrained models by the authors."

bash ../wait-for-it.sh rabbitmq:15672 -s -t 30

echo "${LCYAN}Model Server Start"
python3 app.py
