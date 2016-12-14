default partial alphanumeric_keys modifier_keys
xkb_symbols "ox" {

    name[Group1]= "English (Ox Layout)";

    key <TLDE> {[ grave, asciitilde, U2713, exclam ] };
    key <AE01> {[ at, 1, exclam, exclam ]};
    key <AE02> {[ braceleft, 2, exclam, exclam ]};
    key <AE03> {[ braceright, 3, exclam, exclam ]};
    key <AE04> {[ dollar, 4, exclam, exclam ]};
    key <AE05> {[ percent, 5, exclam, exclam ]};
    key <AE06> {[ asciicircum, 6, exclam, exclam ]};
    key <AE07> {[ ampersand, 7, exclam, exclam ]};
    key <AE08> {[ asterisk, 8, exclam, exclam ]};
    key <AE09> {[ parenleft, 9, exclam, exclam ]};
    key <AE10> {[ parenright, 0, exclam, exclam ]};
    key <AE11> {[ minus, exclam, exclam, exclam ]};
    key <AE12> {[ equal, plus, U00A1, exclam ]};

    key <AD01> {[ semicolon, colon, exclam, exclam ]};
    key <AD02> {[ u, U, U00B5, exclam ]};
    key <AD03> {[ l, L, U03BB, exclam ]};
    key <AD04> {[ m, M, U2206, exclam ]};
    key <AD05> {[ w, W, U2126, exclam ]};
    key <AD06> {[ z, Z, exclam, exclam ]};
    key <AD07> {[ f, F, exclam, exclam ]};
    key <AD08> {[ r, R, exclam, exclam ]};
    key <AD09> {[ o, O, exclam, exclam ]};
    key <AD10> {[ apostrophe, quotedbl, exclam, exclam ]};
    key <AD11> {[ bracketleft, underscore, exclam, exclam ]};
    key <AD12> {[ bracketright, numbersign, U2605, U2606 ]};
    key <BKSL> {[ backslash, bar, U2600, exclam ]};

    key <AC01> {[ a, A, exclam, exclam ]};
    key <AC02> {[ i, I, exclam, exclam ]};
    key <AC03> {[ n, N, exclam, exclam ]};
    key <AC04> {[ t, T, exclam, exclam ]};
    key <AC05> {[ g, G, exclam, exclam ]};
    key <AC06> {[ b, B, exclam, exclam ]};
    key <AC07> {[ s, S, exclam, exclam ]};
    key <AC08> {[ h, H, exclam, exclam ]};
    key <AC09> {[ e, E, U2211, exclam ]};
    key <AC10> {[ p, P, U220F, exclam ]};
    key <AC11> {[ y, Y, exclam, exclam ]};

    key <AB01> {[ j, J, exclam, exclam ]};
    key <AB02> {[ x, X, exclam, exclam ]};
    key <AB03> {[ d, D, U2206, exclam ]};
    key <AB04> {[ k, K, exclam, exclam ]};
    key <AB05> {[ q, Q, exclam, exclam ]};
    key <AB06> {[ v, V, exclam, exclam ]};
    key <AB07> {[ c, C, exclam, exclam ]};
    key <AB08> {[ comma, less, U00AB, exclam ]};
    key <AB09> {[ period, greater, U00BB, exclam ]};
    key <AB10> {[ slash, question, U00BF, exclam ]};

    key <MENU> { [ Escape, Escape ]};

    include "level3(switch)"
    include "shift(both_shiftlock)"

    //key <SCLK> { [ISO_Next_Group] };

    //key <UP> { type[Group2]="ONE_LEVEL", symbols[Group2] = [ Down ] };
    //key <UP> = { [ Up ], [ at ] };
    //key <DOWN> = { [ Down ], [ at ] };
    //key <LEFT> = { [ Left ], [ at ] };
    //key <RGHT> = { [ Right ], [ at ] };


    // key <PRSC>
    // key <PAUS>
    // key <INS>
    // key <HOME>
    // key <PGUP>
    // key <PGDN>
    // key <END>
    // key <DELE>
    // key <BKSP>
    // key <MENU>
};
