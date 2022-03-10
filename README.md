# vcd_pyutils

## Tested on:

Ubuntu 20.04.1 LTS

Python version 3.8.10

## Quick Start:

setup the environment in the bash terminal

    git clone 

    cd vcd_pyutils

    python3.8 -m venv venv
    source venv/bin/activate

    pip install -e .

## Running the vcd parser

inside a python shell

    from vcd_pyutils import vcd_pyutils                            

    simulation_results = vcd_pyutils.vcd("vcd_file_name.vcd")

    #inspect the results
    print(simulation_results.keys())
    print(simulation_results['exdes_tb'])

    #retrieving the signal using the vivado heirarchy
    tdata = simulation_results['exdes_tb']['exdes_top']['m_axis_tdata']['data']

## TODO:
implement 