def decrypt_cypher_text(encrypted_text, key):
    if key < 0:
        print("Key must be a positive number")
        return
    
    else:

        decrypted_text = ""

        for character in encrypted_text:
            ASCII_text = ord(character)
            x = (ASCII_text - key) % 256
            decrypted_text += chr(x)
#     # function implementation here...
    return decrypted_text


text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorsh"
print(decrypt_cypher_text(text, 3))