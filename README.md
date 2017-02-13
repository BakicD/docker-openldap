# OpenLDAP docker image based on centos7     

The image produces immutable containers, i.e. data volumes are outside the
containers COW file system. A container can be removed and re-created
any time without loss of data, because data is stored on data volumes.

## Configuration

1. Clone this repository
2. Copy conf.sh.default to conf.sh
3. Run `git submodule init` and `git submodule update`
4. Modify conf.sh
5. dscripts/build.sh  # For local images only

## Usage

    cd <project root>
    dscript/run.sh [-p] # start slapd in daemon mode
    dscript/run.sh -ir /scripts/init_sample_config.sh    # initialize sample configuration, set root-pw
    dscript/exec.sh /scripts/init_sample_data_xxxx.sh    # initialize sample data, see install/scripts/
    dscript/run.sh -ir  # start interactive bash as root user  
    dscript/exec.sh -i  # open a second shell

## User Namespace Mapping

If the docker daemon does not support user namespace maaping, the image will run with the
default ldap uid/gid (55:55).