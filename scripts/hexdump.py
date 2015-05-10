import argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The file to dump.")
    parser.add_argument("-o", "--output", help="Print output to Terminal." \
                            , action="store_true")
    args = parser.parse_args()
    if not args.file:
        print parser.usage
        return
    else:
        offset = 0
        with open(args.file, 'rb') as infile:
            with open(args.file+".dump", 'w') as outfile:
                while True:
                    chunk = infile.read(16)

                    if not chunk:
                        break

                    text = str(chunk)
                    text = ''.join([c if ord(c) < 128 and ord(c) > 32 \
                                    else "." for c in text])

                    output = "{:#08x}".format(offset)
                    output += ": "
                    output += ' '.join(["{:#02X}".format(ord(c))[2:] \
                                        for c in text[:8]])
                    output += ' | '
                    output += ' '.join(["{:#02X}".format(ord(c))[2:] \
                                        for c in text[8:]])
                    output += " "

                    if len(chunk) % 16 != 0:
                        output += "   "*(16-len(chunk))

                    output += text

                    outfile.write(output + "\n")

                    offset += 16

        if args.output:
            import os
            os.system("gedit %s.dump" % args.file)

if __name__ == "__main__":
    Main()
