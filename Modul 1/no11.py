def apakahKabisat(tahun):
    if(tahun %4)== 0:
        if(tahun %100)== 0:
            if(tahun %400)== 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(apakahKabisat(1896))
print(apakahKabisat(1897))
print(apakahKabisat(1900))
print(apakahKabisat(2000))
print(apakahKabisat(2004))
print(apakahKabisat(2100))