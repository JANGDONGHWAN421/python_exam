from serial.tools.list_ports import comports

from time import sleep

from e_drone.drone import *

from e_drone.protocol import *

nodes = comports()

count = 0;
for node in nodes:
    print("[{0}]".format(count))
    print("         device: ", node.device)
    print("    description: ", node.description)
    print("   manufacturer: ", node.manufacturer)
    print("           hwid: ", node.hwid)
    print("      interface: ", node.interface)
    print("       location: ", node.location)
    print("           name: ", node.name)
    count += 1


def eventAltitude(altitude):
    print("eventAltitude()")
    print("-  Temperature: {0:.3f}".format(altitude.temperature))
    print("-     Pressure: {0:.3f}".format(altitude.pressure))
    print("-     Altitude: {0:.3f}".format(altitude.altitude))
    print("- Range Height: {0:.3f}".format(altitude.rangeHeight))

if __name__ == '__main__':

    drone = Drone()       # 드론 객체 생성
    drone.open()    # 시리얼 포트 연결(내부에서 시리얼 포트 리스트를 읽어서 마지막 장치에 연결)

    print()          # 시리얼 포트 연결(내부에서 시리얼 포트 리스트를 읽어서 마지막 장치에 연결)
    drone.sendBuzzer(BuzzerMode.Scale, BuzzerScale.C4.value, 500)   # 버저에 4옥타브 도 소리를 500ms 동안 내라고 명령하기
    sleep(1)              # 1초간 sleep
    
    print(drone.isOpen())
    print(drone.setEventHandler(DataType.Altitude, eventAltitude))
    drone.sendTakeOff()
    sleep(2)
    print(drone.sendRequest(DeviceType.Drone, DataType.Altitude))

    drone.sendLanding()
    
    drone.close()         # 시리얼 포트 닫기 및 내부 데이터 수신 스레드 종료

