import IPython
from vcd_pyutils import vcd_pyutils                            

name_2_vcdId, signals = vcd_pyutils.parse_vcd("xsim_dump.vcd")
my_map =  name_2_vcdId['exdes_tb']['exdes_top']
my_keys = list(signals.keys())

bus_width = int(signals[my_keys[15]]['width'])

for i in range(3):
    print("_________________")
    bus_data = signals[my_keys[15]]['data'][i][1]
    my_list = vcd_pyutils.bus_2_int_list(bus_data, bus_width,8)

    print(my_list)
