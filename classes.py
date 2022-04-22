class Television:
    '''
    Class to represent the television objects.
    '''
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        '''
        Method to set default state of the tv.
        '''
        self.__tv_channel: int = Television.MIN_CHANNEL
        self.__tv_volume: int = Television.MIN_VOLUME
        self.__tv_status: bool = False

        pass

    def power(self) -> None:
        '''
        Method to turn the TV on/off.
        '''
        self.__tv_status = not self.__tv_status

        pass

    def channel_up(self) -> None:
        '''
        Method to turn the TV channel up.
        '''
        if self.__tv_status and self.__tv_channel == 3:
            self.__tv_channel = 0
        elif self.__tv_status and self.__tv_channel < 3:
            self.__tv_channel += 1

        pass

    def channel_down(self) -> None:
        '''
        Method to turn the TV channel down.
        '''
        if self.__tv_status and self.__tv_channel == 0:
            self.__tv_channel = 3
        elif self.__tv_status and self.__tv_channel > 0:
            self.__tv_channel -= 1

        pass

    def volume_up(self) -> None:
        '''
        Method to turn the TV volume up.
        '''
        if self.__tv_status and self.__tv_volume == 2:
            pass
        elif self.__tv_status and self.__tv_volume < 2:
            self.__tv_volume += 1

        pass

    def volume_down(self) -> None:
        '''
        Method to turn the TV volume down.
        '''
        if self.__tv_status and self.__tv_volume == 0:
            pass
        elif self.__tv_status and self.__tv_volume > 0:
            self.__tv_volume -= 1

        pass

    def __str__(self) -> str:
        '''
        Method to return the TV status, channel, and volume.
        '''
        return 'TV status: Is on = ' + str(self.__tv_status) + ', Channel = ' + str(self.__tv_channel) + ', Volume = ' + str(self.__tv_volume)

        pass

