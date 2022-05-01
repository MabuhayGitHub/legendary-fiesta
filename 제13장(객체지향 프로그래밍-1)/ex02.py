from tv import tv

if __name__ == "__main__":
    tv1 = tv()
    tv2 = tv()

    tv1.color = "BLACK"
    tv1.powertv(True, "tv1")
    tv1.channelUp(9, "tv1")
    tv1.volumelUp(25, "tv1")
    tv1.printtv("tv1")
    tv1.channelDown(-20, "tv1")
    tv1.powertv(False, "tv1")
    tv1.printtv("tv1")

    tv1.color = "WHITE"
    tv1.powertv(True, "tv2")
    tv1.channelUp(11, "tv2")
    tv1.volumelUp(20, "tv2")
    tv1.printtv("tv2")
    tv1.channelDown(-30, "tv2")
    tv1.powertv(False, "tv2")
    tv1.printtv("tv2")
