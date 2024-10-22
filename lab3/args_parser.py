import argparse


def arg_parser() -> tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument('pathtoimage', type=str, help='PATH to image,which will be processed')
    parser.add_argument('-ptf', '--pathtofolder', type=str, help='PATH to folder where will be save image')
    args = parser.parse_args()
    data = (args.pathtoimage, args.pathtofolder)
    return data
