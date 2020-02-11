#!/bin/bash

# how to use?
echo "Usage:" $0 "<target dir>"
echo ""
echo "<target dir> : Full path to a target dir.  Should be different from the"
echo "               conda installation."
echo ""
[ $# -ne 1 ] && exit

# read target dir
target_dir=$1
mkdir -p "${target_dir}"

# create tmp dir
[[ -n ${TMPDIR} ]] || TMPDIR=/tmp
tmp_dir=${TMPDIR}/`date +%s%N`_get_full_cartopy
mkdir "${tmp_dir}"

version=`python -c "import cartopy_userconfig; print(cartopy_userconfig.__version__)"`

# cd to tmp dir, get cartopy source, download data to repo data path
(
    cd "${tmp_dir}"
    wget https://raw.githubusercontent.com/SciTools/cartopy/v${version}/tools/feature_download.py
    python feature_download.py \
        --output ${target_dir} cultural-extra cultural gshhs physical \
        --ignore-repo-data
)

# clean up
rm -rf ${tmp_dir}
