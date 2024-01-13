import util

class ErrorCorrection:
    def __init__(self, level) -> None:
        self.totalNumberOfCodeWords = {
            'L': 100,
            'M': 50,
            'Q': 50,
            'H': 25
        }[level]
        self.numErrorCorrectionCodeWords = {
            'L': 20,
            'M': 36,
            'Q': 52,
            'H': 64
        }[level]
        self.numCodeWords = {
            'L': 80,
            'M': 64,
            'Q': 48,
            'H': 36
        }[level]
        self.numDataBits = self.numCodeWords * 8
        # TODO: Make this mode agnostic, currenty it's byte mode
        self.dataCapacity = {
            'L': 78,
            'M': 62,
            'Q': 46,
            'H': 34
        }[level]
        self.errorCorrectionCapactiy = {
            'L': 10,
            'M': 9,
            'Q': 13,
            'H': 8
        }[level]

    def get_EDC(self, data):
        degree = self.totalNumberOfCodeWords - len(data)
        messagePoly = [0] * self.totalNumberOfCodeWords
        messagePoly[:len(data)] = data
        print(messagePoly)
        return util.poly_rest(messagePoly, util.get_generator_poly(degree))
        