import serial
import serial.tools.list_ports


class serialConn():
    def __init__(self):
        self.ports = []
        self.matched_device_count = 0
        pass

    def find_ports(self):
        pass

    def get_port_list(self):
        self.ports = serial.tools.list_ports.comports(include_links=True)
        print(f'found {len(self.ports)} devices')
        self.port_info()
        self.match_device_manufacturer("FTDI")
        port_links = []
        for each in self.ports:
            port_links.append(each.device)
        return port_links

    def port_info(self):
        for each in self.ports:
            print(f'{each}:')
            print(f'device: {each.device}')
            print(f'name: {each.name}')
            print(f'description: {each.description}')
            print(f'hardware id: {each.hwid}')
            print(f'vid: {each.vid}')
            print(f'pid: {each.pid}')
            print(f'serial number: {each.serial_number}')
            print(f'location: {each.location}')
            print(f'manufacturer: {each.manufacturer}')
            print(f'product: {each.product}')
            print(f'interface: {each.interface}\n')

    def match_device_manufacturer(self, target):
        self.matched_device_count = 0
        for each in self.ports:
            if each.manufacturer == target:
                self.matched_device_count += 1
        return self.matched_device_count

x = serialConn()

x.get_port_list()
