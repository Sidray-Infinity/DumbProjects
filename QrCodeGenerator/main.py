import mode
import util

if __name__ == "__main__":
    m = mode.ByteMode(correctionLevel='L')
    encoded_data = m.encode("https://www.qrcode.com/")
    # print(encoded_data)
    # code_words = []
    # for i in range(0, len(encoded_data), 8):
    #     word = encoded_data[i:i+8]
    #     code_words.append(int(word, 2))

    # print(len(code_words))
    # print(code_words)
    # print(len(encoded_data))
    # [1, 59, 13, 104, 189, 68, 209, 30, 8, 163, 65, 41, 229, 98, 50, 36, 59]
    # print(util.get_generator_poly(16))