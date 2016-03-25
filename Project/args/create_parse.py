import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("hp", help="The base number of HP.", type=int)
    h_pack = "How many hp the hp packs are restoring."
    parser.add_argument("stimpak_val", help=h_pack, type=int)
    return (parser)


def check_args():
    args = create_parser().parse_args()
    if args.hp is None or args.stimpak_val is None:
        return (False)
    if args.hp is not None:
        if args.hp <= 0:
            print("You can't have a negative hp count.")
    if args.stimpak_val is not None:
        if args.stimpak_val <= 0:
            print("Stimpacks are supposed to heal you. Not kill you.")

if __name__ == '__main__':
    check_args()
