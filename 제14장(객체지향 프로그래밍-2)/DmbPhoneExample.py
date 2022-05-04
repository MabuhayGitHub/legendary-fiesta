from DmbPhone import *

if __name__ == "__main__":
    dmbPhone = DmbPhone("파이썬폰", "검정", 10)
    print("모델", dmbPhone.model)
    print("색상", dmbPhone.color)
    print("채널", dmbPhone.channel)
    print()

    dmbPhone.powerOn()
    dmbPhone.bell()
    dmbPhone.sendVoice("여보세요")
    dmbPhone.recieveVoice("안녕하세요. 저는 홍길동입니다.")
    dmbPhone.sendVoice("안녕하세요. 반갑습니다.")
    dmbPhone.hangUp()
    print()
    
    dmbPhone.turnOnDmb()
    dmbPhone.changeChannelDmb(100)
    dmbPhone.turnOffDmb()

