#!/bin/sh
BASE_PWD=$PWD

# download pretrained models
PRETRAINED_MODEL_PATH="./network/pretrained_model/"
STYLES=("cartoongan_hayao.pth" "cartoongan_hosoda.pth" "cartoongan_paprika.pth" "cartoongan_shinkai.pth"
        "cyclegan_cezanne.pth" "cyclegan_monet.pth" "cyclegan_ukiyoe.pth" "cyclegan_vangogh.pth"
        "cartoongan_vangogh.ckpt" "cartoongan2_mulan.ckpt" "cartoongan2_pelissero.ckpt")

len=${#STYLES[@]}

if [ ! -d $PRETRAINED_MODEL_PATH ]; then
  echo "creating $PRETRAINED_MODEL_PATH"
  mkdir -p $PRETRAINED_MODEL_PATH;
else
  echo "$PRETRAINED_MODEL_PATH already exists"
fi

cd $PRETRAINED_MODEL_PATH
for ((i=0;i<len;i++)); do
  FILEPATH="${STYLES[$i]}"
  if [ -e "$FILEPATH" ]; then
    echo "$FILEPATH exist"
  else
    url="https://drive.google.com/drive/u/1/folders/126Oat85ofwr4ghIfVwNc7N_biFA3ehdv"
    echo "download ${STYLES[i]}"
    wget $url -O ${STYLES[i]}
    echo
  fi
done

# wget --no-check-certificate ‘https://drive.google.com/drive/u/1/folders/126Oat85ofwr4ghIfVwNc7N_biFA3ehdv’ -O cyclegan_cezanne_300.pth

cd $BASE_PWD
