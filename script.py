# ciphers are awesome!

# ciphers are awesome!

# catcatc atc atcatca

def caesar_decode(message, offset):
    decoded_message = ""
    for char in message:
        if char.isalpha():
            num = ord(char) - ord('a')
            shifted_num = (num - offset) % 26
            decoded_char = chr(shifted_num + ord('a'))
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message

def caesar_encode(message, offset):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            num = ord(char) - ord('a')
            shifted_num = (num + offset) % 26
            encoded_char = chr(shifted_num + ord('a'))
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message

# Vishal's encoded message
encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
offset = 10

# Decode the message
decoded_message = caesar_decode(encoded_message, offset)
print(decoded_message)

# First message
first_encoded_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
first_offset = 10
first_decoded_message = caesar_decode(first_encoded_message, first_offset)
print(first_decoded_message)

# Second message
second_encoded_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
second_offset = 10
second_decoded_message = caesar_decode(second_encoded_message, second_offset)
print(second_decoded_message)

def vigenere_encode(message, keyword):
    encoded_message = ""
    keyword_phrase = (keyword * (len(message) // len(keyword) + 1))[:len(message)]
    keyword_index = 0

    for char in message:
        if char.isalpha():
            message_num = ord(char.lower()) - ord('a')
            keyword_num = ord(keyword_phrase[keyword_index].lower()) - ord('a')
            shifted_num = (message_num + keyword_num) % 26
            encoded_char = chr(shifted_num + ord('a'))
            encoded_message += encoded_char
            keyword_index += 1

       

