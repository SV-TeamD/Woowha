#!/bin/sh
BASE_PWD=$PWD

# download pretrained models
PRETRAINED_MODEL_PATH="./network/pretrained_model/"
STYLES=("Hayao" "Hosoda" "Paprika" "Shinkai")
MODEL_POSTFIX="_net_G_float.pth"

len=${#STYLES[@]}
cd $PRETRAINED_MODEL_PATH
for ((i=0;i<len;i++)); do
  FILEPATH="${STYLES[$i]}${MODEL_POSTFIX}"
  if [ -e "$FILEPATH" ]; then
    echo "$FILEPATH exist"
  else
    url="http://vllab1.ucmerced.edu/~yli62/CartoonGAN/pytorch_pth/${STYLES[i]}_net_G_float.pth"
    echo "download ${STYLES[i]}"
    wget -c $url
    echo
  fi
done

cd $BASE_PWD
