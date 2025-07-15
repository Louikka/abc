import 'dart:math';



void main(List<String> argv) {

    if (argv.length == 0) return print('No CLI arguments provided (use \'-help\' for more information).\n');

    if (argv.contains('-info')) {

        print(
            'Build on Dart SDK v3.8.1\n\n'
            'Also, fun fact : when generating 8-symbols id using only lowercase letters\n'
            'the probability of getting two exactly identical id\'s is ~4.79e-12 (or\napprox. 0.0000000005%).\n'
        );

        return;

    }

    if (argv.contains('-help') || argv.contains('-elp')) {

        print(
            'CLI arguments :\n'
            '  -len [number] = length of the id\n'
            '  -mode [type] = type of included symbols\n'
            '  -info = print info about this program\n'
            '  -help / -elp = print this message\n\n'
            'The value of -mode [type] argument must be combination of flags as listed here\n'
            'below. If omitted, takes default (\'lLd\').\n'
            '  \'l\' = lower case letters\n'
            '  \'L\' = upper case letters\n'
            '  \'d\' = digits\n'
            '  \'h\' = hexidigits\n'
            '  \'o\' = octdigits\n'
            'for example :\n'
            '  flag \'lLh\' will generate an id with both case letters and hexidigits.\n'
        );

        return;

    }



    int len = 0;

    try {

        len = int.parse( getCLIArgumentValue(argv, 'len') );

    } catch (err) {

        print('-len parameter value is not a number (reading "${ getCLIArgumentValue(argv, 'len') }").\n');

        return;

    }


    String s = '';

    if (getCLIArgumentValue(argv, 'mode').contains('l')) s += 'abcdefghijklmnopqrstuvwxyz';
    if (getCLIArgumentValue(argv, 'mode').contains('L')) s += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (getCLIArgumentValue(argv, 'mode').contains('d')) s += '0123456789';
    if (getCLIArgumentValue(argv, 'mode').contains('h')) s += '0123456789abcdefABCDEF';
    if (getCLIArgumentValue(argv, 'mode').contains('o')) s += '01234567';

    if (getCLIArgumentValue(argv, 'mode') == '') s += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';

    if (s.length == 0) {

        print('Mode "${ getCLIArgumentValue(argv, 'mode') }" is not defined.\n');

        return;

    }


    String a = '';

    for (int i = 0; i < len; i++) {

        a += getIterableRandomPositionValue(s);

    }

    print(a);

}



String getCLIArgumentValue(List<String> args, String key) {

    if (args.indexOf('-$key') == -1) return '';

    return args[args.indexOf('-$key') + 1];

}

dynamic getIterableRandomPositionValue(iterable) {

    int i = Random().nextInt(iterable.length - 1);

    return iterable[i];

}
