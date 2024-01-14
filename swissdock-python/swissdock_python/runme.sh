#!/bin/bash
#
# Should you have problems, just let us know: swissdock.team@gmail.com


PYTHONBIN=`which python2` # update according to your python setup

export PYTHONPATH=`pwd`/swissdock_ws

# for help
#$PYTHONBIN -u swissdock_ws/swissdock_ws/client/soappy/swissdock_client.py --help

# sample command line
$PYTHONBIN -u swissdock_ws/swissdock_ws/client/soappy/swissdock_client.py -i -H www.swissdock.ch/soap/wsdl -n testjob -e your.address@your.domain -w 50 -f 10 -N 10 -M 1 -m 1 -T ./example/input_files/target.psf,./example/input_files/target.crd -L ./example/input_files/lig.pdb,./example/input_files/lig.rtf,./example/input_files/lig.par -a


