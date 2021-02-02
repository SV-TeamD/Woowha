#!/bin/sh
BASE_PWD=$PWD

# download pretrained models
PRETRAINED_MODEL_PATH="./network/pretrained_model/"
STYLES=("cartoongan_hayao.pth" "cartoongan_hosoda.pth" "cartoongan_paprika.pth" "cartoongan_shinkai.pth"
        "cyclegan_cezanne.pth" "cyclegan_monet.pth" "cyclegan_ukiyoe.pth" "cyclegan_vangogh.pth"
        "cartoongan_vangogh.ckpt" "cartoongan2_mulan.ckpt" "cartoongan2_pelissero.ckpt")
IDS=("1rYWWlwOr7bCapNjcxLOesd8hApuYQWIZ" "1HU7wLeC15Unt6C1RC7q34fDEjnj-fNP-" "1i0-Q5qOZWk2K2SIFER6wADxofEtWAZps" "1bdausoRH1IX4mAEPHyovJqGF9Aq2MfSO"
    "1kykudsLL8rD_PACpcg6EIMXiwyDSyq00" "1Sgal9LNhqGlSGfnBDMvILDxKiPoJIA9g" "1mzfUaZg_K7r6jupXx3ZvqcDBRnaigq82" "19fDPwKkTUTSCF92H_MVUkv5HMsUPzRyZ"
    "12nR6_QN_ZG_xes1TuTJNdV_MaDa6fhW4" "1VYI9No6r6ZB1go4BjQH1OXdFFiFFk7vG" "1hlDJLIC_MDPtXmF0QVBH5GFKH-2R-f9O")

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
    echo "download ${STYLES[i]}"
    # wget --no-check-certificate "https://drive.google.com/uc?export=download&id=${IDS[i]}" -O ${STYLES[i]}
    curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${IDS[i]}" > /dev/null
    code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
    curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${IDS[i]}" -o ${STYLES[i]}
    echo
  fi
done

cd $BASE_PWD
