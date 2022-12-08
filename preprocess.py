def success(ventas):
    if ventas < 250000:
        return "Bad seller"
    elif ventas >= 250000 and ventas < 500000:
        return "Good seller"
    elif ventas >= 500000 and ventas < 750000:
        return "Great seller"
    elif ventas >= 750000:
        return "Best seller"
    else:
        return "unknown"


def critic_success(critic):
    if critic < 2:
        return "Bad rating"
    elif critic >= 2 and critic < 3:
        return "Average rating"
    elif critic >= 3 and critic < 4:
        return "Good rating"
    elif critic >= 4 and critic <= 5:
        return "Great rating"
    else:
        return "unknown"
