#!/bin/sh
BASE_PWD=$PWD

# download pretrained models
PRETRAINED_MODEL_PATH="./network/pretrained_model/"
STYLES=("cartoongan_hayao" "cartoongan_hosoda" "cartoongan_paprika" "cartoongan_shinkai" "cyclegan_cezanne" "cyclegan_monet" "cyclegan_ukiyoe" "cyclegan_vangogh")
MODEL_POSTFIX=".pth"

len=${#STYLES[@]}
cd $PRETRAINED_MODEL_PATH
for ((i=0;i<len;i++)); do
  FILEPATH="${STYLES[$i]}${MODEL_POSTFIX}"
  if [ -e "$FILEPATH" ]; then
    echo "$FILEPATH exist"
  else
    pthname = "${STYLES[i]}.pth"
    url = "https://drive.google.com/drive/u/1/folders/126Oat85ofwr4ghIfVwNc7N_biFA3ehdv"
    #url="http://vllab1.ucmerced.edu/~yli62/CartoonGAN/pytorch_pth/${STYLES[i]}_net_G_float.pth"
    echo "download ${STYLES[i]}"
    #wget -c $url
    wget --no-check-certificate $url -O pthname
    echo
  fi
done

# wget --no-check-certificate 'https://drive.google.com/drive/u/1/folders/126Oat85ofwr4ghIfVwNc7N_biFA3ehdv' -O cyclegan_cezanne_300.pth

cd $BASE_PWD
