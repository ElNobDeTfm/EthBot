def GetInHMS(seconds, hms, value):
    hours = seconds / 3600
    seconds -= 3600*hours
    minutes = seconds / 60
    seconds -= 60*minutes
    if value == 3:
        return hms % (hours, minutes, seconds)
    elif value == 2:
        return hms % (minutes, seconds)


def seen(user, seconds):
    hours = seconds / 3600
    seconds -= 3600*hours
    minutes = seconds / 60
    seconds -= 60*minutes
    if hours == 1:
        hrs = "hora"
    else:
        hrs = "horas"
    if seconds == 1:
        scs = "segundo"
    else:
        scs = "segundos"
    if minutes == 1:
        mns = "minuto"
    else:
        mns = "minutos"

    if hours == 0 and minutes == 0 and seconds != 0:
        return "He visto por ultima vez a %s hace %d %s." % (user, seconds, scs)
    elif hours == 0 and minutes != 0 and seconds == 0:
        return "He visto por ultima vez a %s hace %d %s." % (user, minutes, mns)
    elif hours != 0 and minutes == 0 and seconds == 0:
        return "He visto por ultima vez a %s hace %d %s." % (user, hours, hrs)
    elif hours == 0 and minutes != 0 and seconds != 0:
        return "He visto por ultima vez a %s hace %d %s y %d %s." % (user, minutes, mns, seconds, scs)
    elif hours != 0 and minutes != 0 and seconds != 0:
        return "He visto por ultima vez a %s hace %d %s, %d %s y %d %s." % (user, hours, hrs, minutes, mns, seconds, scs)
    elif hours != 0 and minutes == 0 and seconds != 0:
        return "He visto por ultima vez a %s hace %d %s y %d %s." % (user, hours, hrs, seconds, scs)
    elif hours != 0 and minutes != 0 and seconds == 0:
        return "He visto por ultima vez a %s hace %d %s y %d %s." % (user, hours, hrs, minutes, mns)
