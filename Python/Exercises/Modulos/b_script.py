__name__  # __name__ es una variable:
# 1. Si __name__ se usa dentro del mismo archivo donde está escrita, entonces, tendrá el valor de "__main__". -> __name__ = "__main__".
# 2. Si __name__ se está declarada dentro de un archivo "A", y este archivo es importado y ejecutado, entonces, __name__ = "__nombre-del-archivo__".


def main():
    print("Se está usando main A.")


if __name__ == "__main__":  #
    main()
