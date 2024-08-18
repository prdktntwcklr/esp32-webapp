import esptool

def main():
    cmd = ["image_info", "--version", "2", "bin/hello_world.bin"]
    esptool.main(cmd)

if __name__ == "__main__":
    main()
