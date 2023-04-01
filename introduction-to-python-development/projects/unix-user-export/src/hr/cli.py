from argparse import ArgumentParser, Namespace


def create_parser():
    parser = ArgumentParser()

    parser.add_argument(
        '--format',
        type=str.lower,
        choices=['json', 'csv'],
        default='json',
        help='specify output format: json or csv (default: json)'
    )

    parser.add_argument(
        '--path',
        type=str,
        help='specify path to output file'
    )

    return parser


def main():
    import hr.format_data as format_data

    args: Namespace = create_parser().parse_args()

    if args.path:
        if args.format == 'csv':
            format_data.write_csv_file(args.path)
        else:
            format_data.write_json_file(args.path)
    else:
        if args.format == 'csv':
            format_data.print_csv()
        else:
            format_data.print_json()

