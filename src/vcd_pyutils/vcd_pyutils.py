"""
Generic VCD parser.

    Copyright (C) 2022  Sioan Zohar

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from collections import UserDict

def parse_vcd(file_name):

    vcdId_signals = {}
    curr_node = {}

    fp = open(file_name)

    for line in fp:
        line = line.split(" ")
        
        #TODO: implement full suite of scope types 
        if "$enddefinitions" == line[0]:
            break

        if "$scope" == line[0] and "module" == line[1] and "$end\n" == line[-1]:
            parent_node = curr_node
            curr_node = {'parent':parent_node,'name':line[2]}

        if "$upscope" == line[0] and "$end\n" == line[-1]:
            curr_node['parent'][curr_node.pop('name')] = curr_node
            curr_node = curr_node.pop('parent')

        if "$var" == line[0] and "$end\n" == line[-1]:
            vcdId_signals[line[3]]={"width":int(line[2]),"type":line[1],"data":[], "time":[]}
            curr_node[line[4]]=line[3]


    for line in fp:
        if "#" == line[0]:
            current_time =int(line[1:])

        elif "0" == line[0] or "1" == line[0]:
            data = line[0]
            vcdId = line[1:-1]
            vcdId_signals[vcdId]['time'].append(current_time)
            vcdId_signals[vcdId]['data'].append( data)

        elif "b" == line[0] or "B" == line[0]:
            data, vcdId = line.split(" ")
            vcdId = vcdId[:-1]
            vcdId_signals[vcdId]['time'].append(current_time)
            vcdId_signals[vcdId]['data'].append( data)


    return curr_node, vcdId_signals


def bus_2_int_list(bus_data, bus_width, data_width):
    assert not bus_width%data_width, "bus size needs to be integer multiple of data_width"

    my_list = []

    bus_data = bus_data[1:].zfill(bus_width)

    for i in range(0, bus_width, data_width):
        my_list.append(int(bus_data[i:i+data_width],2))

    return my_list

def bus_trace_to_int_array(bus_data, bus_width, data_width):
    return list(map(lambda p: bus_2_int_list(p,bus_width,data_width),bus_data))


class vcd():
    def __init__(self,*args, file_name = None):

        if file_name is not None:
            mapping, self._signals =  parse_vcd("xsim_dump.vcd")

        else:
            mapping, self._signals = args[0], args[1]

        self.mapping = dict()
        if type(mapping) is dict:
            for key in mapping:
                self.mapping[key] =  vcd(mapping[key],self._signals)
        else:
            self.mapping = self._signals[mapping]

    def __getitem__(self,key):
        return self.mapping[key]
        
    def __contains__(self, name):
        if name in self.mapping:
            return True
        else:
            return False

    def __str__(self):
        s = f'({self.mapping.keys()})'
        return s
    
    def __repr__(self):
        s = f'({self.mapping.keys()})'
        return s
        
    def keys(self):
        return self.mapping.keys()
