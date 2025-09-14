from enum import Enum


class CallSessionStatus(Enum, str):
    HISTROY = "🏛️ История"


class CallSessionDuration(Enum, int):
    DURATION_20 = 20
    DURATION_30 = 30
    DURATION_40 = 40
    DURATION_60 = 60