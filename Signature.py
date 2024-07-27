from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def generate_keys():

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    pu_serialized = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    return private_key, pu_serialized


def sign(message, private_key):
    message = bytes(str(message), "utf-8")
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    return signature


def verify(message, signature, pu_serialized):
    loaded_pu = serialization.load_pem_public_key(
        pu_serialized, backend=default_backend()
    )
    message = bytes(str(message), "utf-8")
    try:
        loaded_pu.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )
        return True
    except InvalidSignature:
        return False
    except:
        print("Error executing public_key.verify")


def savePrivate(pr_key, filename):
    pem = pr_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    fp = open(filename, "wb")
    fp.write(pem)
    fp.close()


def loadPrivate(filename):
    fin = open(filename, "rb")
    pr_key = serialization.load_pem_private_key(
        fin.read(),
        password=None,
    )
    fin.close()
    return pr_key


def savePublic(pu_key, filename):
    fp = open(filename, "wb")
    fp.write(pu_key)
    fp.close()
    return True


def loadPublic(filename):
    fin = open(filename, "rb")
    pu_key = fin.read()
    fin.close()
    return pu_key


if __name__ == "__main__":
    pr, pu = generate_keys()
    # print(pr, pu)
    message = "this is a secret message"
    signature = sign(message, pr)
    # print(signature)
    correct = verify(message, signature, pu)

    if correct:
        print("Success! Good sig")
    else:
        print("ERROR! Signature is bad")

    pr2, pu2 = generate_keys()

    signature2 = sign(message, pr2)

    correct = verify(message, signature2, pu)
    if correct:
        print("Error! Bad signature checks out!")
    else:
        print("Success! Bad signature detected")

    badmess = message + "Q"

    correct = verify(badmess, signature, pu)
    if correct:
        print("Error! Tampered message checks out!")
    else:
        print("Success! Tampering detected")

    savePrivate(pr2, "private.key")
    pr_load = loadPrivate("private.key")
    sig3 = sign(message, pr_load)
    correct = verify(message, sig3, pu2)
    if correct:
        print("Success! Load private key is good")
    else:
        print("Error! Bad loaded private key")

    savePublic(pu2, "public.key")
    pu_load = loadPublic("public.key")
    correct = verify(message, sig3, pu_load)
    if correct:
        print("Success! Load public key is good")
    else:
        print("Error! Bad loaded public key")
