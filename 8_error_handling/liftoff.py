def step1():
    engines = {
        "engine1": "nominal",
        "engine2": "nominal",
    }

    print(engines["engine1"])
    print(engines["engine2"])
    print(engines["engine3"])


def step2():
    thrust = 0
    power = 10

    print(power / thrust)


def step3():
    thrust = 10

    print("Thrust: " + thrust)


def step4():
    confirmation = int(input("Confirm? 0/1"))

    print(f"Liftoff confirm: {confirmation}")

def step5():
    report = {
        "engine1": "nominal",
        "engine2": "nominal",
        "fuel": "full"
    }

    report.append("boosters", "ok")

def step6():
    boosters = ["booster1", "booster2"]
    print(boosters[2])

def step7():
    from liftoff.youdidit import step9

    step9()

def liftoff():
    step1()
    step2()
    step3()
    step4()
    step5()
    step6()

liftoff()