if [[ -n "$CARTOPY_OFFLINE_SHARED" ]]; then
    exit 0
fi

_FQDN=`hostname -f`

#if [[ ${_FQDN} == *".hlrn.de" ]]; then
    export _CONDA_SET_CARTOPY_OFFLINE_SHARED=1
    export CARTOPY_OFFLINE_SHARED=/home/b/shkifmwr/TM/data/cartopy_offline_data
#fi
