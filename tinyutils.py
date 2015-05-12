import subprocess


def main():

    output, err = \
        subprocess.Popen(['ip', 'a'], stdout=subprocess.PIPE).communicate()

    output_list = output.decode("utf-8").split("\n")
    interfaces = []

    for i in output_list:
        if i and i[0].isdigit():
            interfaces.append(i.split(': ')[1])

    print (interfaces)

if __name__ == "__main__":
    main()
