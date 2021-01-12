#!/bin/bash

LWHITE="\033[1;37m"
LCYAN="\033[1;36m"

echo "${LCYAN}Model Server Start"
# python3 manage.py run
echo ""
echo "${LWHITE}Download Pretrained Model Weights"
bash ./load-models.sh
echo ""
echo "${LWHITE}TEST"
pytest
echo ""
echo "${LWHITE}Create image from GAN"
echo "Pytorch Models CartoonGAN [Chen et al., CVPR18]. With the released pretrained models by the authors."
python3 network/Runner.py