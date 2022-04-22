class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        self.__tv_channel = 0
        self.__tv_volume = 0
        self.__tv_status = False

        pass

    def power(self):
        self.__tv_status = not self.__tv_status

        pass

    def channel_up(self):
        if self.__tv_status and self.__tv_channel == 3:
            self.__tv_channel = 0
        elif self.__tv_status and self.__tv_channel < 3:
            self.__tv_channel += 1

        pass

    def channel_down(self):
        if self.__tv_status and self.__tv_channel == 0:
            self.__tv_channel = 3
        elif self.__tv_status and self.__tv_channel > 0:
            self.__tv_channel -= 1

        pass

    def volume_up(self):
        if self.__tv_status and self.__tv_volume == 2:
            pass
        elif self.__tv_status and self.__tv_volume < 2:
            self.__tv_volume += 1

        pass

    def volume_down(self):
        if self.__tv_status and self.__tv_volume == 0:
            pass
        elif self.__tv_status and self.__tv_volume > 0:
            self.__tv_volume -= 1

        pass

    def __str__(self):
        return 'TV status: Is on = ' + str(self.__tv_status) + ', Channel = ' + str(self.__tv_channel) + ', Volume = ' + str(self.__tv_volume)

        pass

