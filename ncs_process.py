# Arda Mavi

import mvnc.mvncapi as mvnc

# Devices List:
def get_devices_list():
    devices = mvnc.EnumerateDevices()
    if len(devices) == 0:
        print('Not found any Intel Movidius NCS device!')
        return None
    else:
        return devices

# Select Devices:
def get_device(which_device):
    device = mvnc.Device(which_device)
    return device

# Open-Close Device:
def open_device(device):
    device.OpenDevice()
def close_device(device):
    device.CloseDevice()

# Read Graph:
def get_graph_from_file(path):
    try:
        with open(path, 'rb') as graph_file:
            graph = graph_file.read()
    except:
        print('Graph file not exits!')
        return None
    return graph

# Allocate-Deallocate Model:
def get_ncs_model(device, graph):
    ncs_model = device.AllocateGraph(graph)
    return ncs_model
def drop_ncs_model(ncs_model):
    ncs_model.DeallocateGraph()

def ncs_predict(ncs_model, inputs):
    ncs_model.LoadTensor(inputs, 'inputs')
    outputs, userobj = ncs_model.GetResult()
    return outputs

### All in ones:

# Get ready NCS with model:
def ready_ai_ncs(graph_path, device_index=0):
    devices = get_devices_list()
    if devices == None:
        return None
    if device_index > len(devices) or device_index < 0:
        print('Device index out of range!')
        return None
    device = get_device(devices[device_index])
    device = open_device(device)
    graph = get_graph_from_file(graph_path)
    if graph == None:
        return None
    model = get_ncs_model(device, graph)
    return ncs_model, device # Ready for 'ncs_predict()' function!

# Release NCS with model:
def release_ai_ncs(device, ncs_model):
    drop_ncs_model(ncs_model)
    close_device(device)
