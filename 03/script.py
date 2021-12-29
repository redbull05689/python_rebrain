str1 = 'May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated'
str2 = 'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.'
str3 = 'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...'
str4 = 'May 20 11:01:12 PC-00102 PackageKit: daemon start'
str5 = 'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...'
str6 = 'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00'
str7 = 'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"'
str8 = 'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device'
str9 = 'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio'
str10 = 'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.'


list1 = [str1, str2 , str3, str4, str5, str6, str6, str7, str8, str8, str9, str10]
dict1 = {
    'string_1': {
        'time': list1[0][:15],
        'pc_name':list1[0].split(' ')[3],
        'service_name':list1[0].split(' ')[4],
        'message':list1[0].split(': ', maxsplit=1)[-1]
    }
}

print(dict1['string_1']['time'])

# 3 
inp1 = input("Введите номер строки:")
dict2 = {
    'string_1': {
        'time': list1[int(inp1)][:15],
        'pc_name':list1[int(inp1)].split(' ')[3],
        'service_name':list1[int(inp1)].split(' ')[4],
        'message':list1[int(inp1)].split(': ', maxsplit=1)[-1]
    }
}

# 4

print(dict2['string_1']['pc_name'], ": ", dict2['string_1']['message'])