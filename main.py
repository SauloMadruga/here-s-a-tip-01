# The "pylogix" library makes it possible to communicate with Rockwell Automation PLCs
from pylogix import PLC

IP_PLC = '192.168.1.100'  # Enter the IP Adrress of the PLC

# Write the values:
write_list = [('AI_MiliAmps', 17)]


def writeData(tags):
    with PLC() as comm:
        comm.IPAddress = IP_PLC
        comm.Micro800 = True
        comm.ConnectionSize = 508

        writeValues = comm.Write(tags)

        # print the status of the writes
        for r in writeValues:
            print(f"TAG Name: {r.TagName} | Status: {r.Status}")


writeData(write_list)


# read the values:
read_list = ['Tag_0', 'Tag_1', 'Coil_0', 'AI_MiliAmps', 'PercentValueOut']


def readData(tags):
    with PLC() as comm:
        comm.IPAddress = IP_PLC
        comm.Micro800 = True
        comm.ConnectionSize = 508

        # Read Data:
        readValues = comm.Read(tags)
        for r in readValues:
            print(
                f"TAG Name: {r.TagName} | Value = {r.Value} | Status: {r.Status}")


readData(read_list)
