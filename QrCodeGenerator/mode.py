import util
from error_correction import ErrorCorrection

class ByteMode():
    def __init__(self, correctionLevel) -> None:
        self.errorCorrection = ErrorCorrection(correctionLevel)
        self.modeIndicator = '0100'
        self.numCharCountIndicator = 8
        self.terminator = '0000'
        self.terminalPadEven = '11101100' # hxEC
        self.terminalPadOdd = '00010001' # hx11
        super().__init__()

    def verify_length(self, data, encodedData) -> bool:
        # B = M + C + 8D
        return len(encodedData) == len(self.modeIndicator) + self.numCharCountIndicator + 8*len(data)
    
    def add_terminal_padding(self, encodedData) -> str:
        for i in range((self.errorCorrection.numDataBits - len(encodedData)) // 8):
            if i % 2 == 0:
                encodedData += self.terminalPadEven
            else:
                encodedData += self.terminalPadOdd
        return encodedData

    def add_padding(self, encodedData):
        if len(encodedData) < self.errorCorrection.numDataBits:
            encodedData += self.terminator
        encodedData += "0" * (len(encodedData) % 8)
        return self.add_terminal_padding(encodedData)

    def to_codewords(self, data):
        code_words = []
        for i in range(0, len(data), 8):
            word = data[i:i+8]
            code_words.append(int(word, 2))
        return code_words

    def encode(self, data) -> str:
        """
        encoded_data = mode + charCountIndicator + encodedData + 
        terminator + addition 0s to fill word + hxEC+hx11 till all code words exhaust
        """
        encodedData = ""
        for d in data:
            encodedData += f'{ord(d):08b}'
        res = self.modeIndicator + util.num_to_bits(len(data), self.numCharCountIndicator) + encodedData
        assert self.verify_length(data, res), "invalid encoded data length"
        res = self.add_padding(res)
        codewords = self.to_codewords(res)
        # print("CODEWORDS:", codewords)
        print("EDC:", self.errorCorrection.get_EDC(codewords))
        return res
