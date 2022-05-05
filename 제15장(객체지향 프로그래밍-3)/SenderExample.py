# ContentSender, KakaoSender, SmsSender

from KakaoSender import *
from SmsSender import *

if __name__ == "__main__":
    
    cs1 = KakaoSender("카카오톡", "이재훈", "100만원 내놔")
    cs1.sendMsg("채무자")

    cs2 = SmsSender("단문 문자", "김연아", "땡큐")
    cs2.sendMsg("고마운분")