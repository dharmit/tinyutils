import subprocess


def main():

    # Using subprocess.Popen() we can execute a Linux command from within
    # Python. The full command redirects the output in variable 'output' and
    # errors, if any, to 'err' variable

    output, err = \
        subprocess.Popen(['ip', 'a'], stdout=subprocess.PIPE).communicate()

    # 'output' variable has data in bytes. We want to have string. Using
    # decode() method we can convert it by specifying appropriate encoding

    output_list = output.decode("utf-8").split("\n")
    interfaces = []

    # The kind of output we are interested in is:
    #   1: lo: <LOOPB....
    #   2: eth0: <NO....
    # So if a line starts with a digit like 1, 2, 3, we split it. Else we
    # ignore it.

    for i in output_list:
        if i and i[0].isdigit():
            interfaces.append(i.split(': ')[1])

    # Finally we just print the interfaces

    print (interfaces)

if __name__ == "__main__":
    # Do not forget this! Otherwise, nothing will seem to be working. :)

    main()
